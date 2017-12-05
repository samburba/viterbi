import sys, datetime
import pandas_datareader as pdr
import pandas as pd
import matplotlib.pyplot as plt
from viterbi import Viterbi
from config import initial, trans, emiss
from datetime import timedelta
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Invalid usage. (python run.py STOCK START_DAY END_DAY)")
        sys.exit(0)
    stock_name = sys.argv[1]
    #dates MUST be in mm/dd/yyyy in order for this to work
    try:
         start = datetime.datetime.strptime(sys.argv[2], "%m/%d/%Y")
         end = datetime.datetime.strptime(sys.argv[3], "%m/%d/%Y")
         if start.weekday() >= 5:
             print("Error: Starting date cannot be during the weekend. " + str(start) + " is on a weekend.")
             sys.exit(1)
         if end.weekday() >= 5:
            print("Error: Ending date cannot be during the weekend. " + str(end) + " is on a weekend.")
            sys.exit(1)
    except ValueError:
        print("All dates must be in mm/dd/yyyy format")
        sys.exit(1)
    try:
        hist_prices = pdr.DataReader(stock_name, "yahoo", start, end)
    except:
        print("There was a problem getting the data from Yahoo finance API.")
        sys.exit(1)
    #Set up the VITERBI
    states = ["Buy", "Sell"]
    obs = []
    obs_prices = []
    obs_delta = []
    prev_price = hist_prices["Adj Close"][0]
    for price in hist_prices["Adj Close"]:
        if price >= prev_price:
            obs.append("Up")
        else:
            obs.append("Down")
        obs_prices.append(price)
        obs_delta.append(price - prev_price)
        prev_price = price
    possible_obs = ["Up", "Down"]
    v = Viterbi(initial, states, obs, possible_obs, trans, emiss)
    v.run()
    #v.print_table()
    #v.print_backtrack_table()
    #v.print_backtrack()

    #make a graph
    backtrack = v.get_backtrack()
    backtrack.pop(0)
    to_print = pd.DataFrame(hist_prices['Adj Close'])
    to_print["Delta"] = obs_delta
    to_print["Output"] = backtrack
    print(to_print)
    fig = hist_prices['Adj Close'].plot(grid="True")
    i = start
    tmp_backtrack = backtrack
    prev_state = ""
    while i < end:
        if i.weekday() < 5:
            if tmp_backtrack:
                if tmp_backtrack[0] == "Buy":
                    plt.axvspan(i, i + timedelta(days=1), facecolor='g', alpha=0.5)
                else:
                    plt.axvspan(i, i + timedelta(days=1), facecolor='r', alpha=0.5)
                tmp_backtrack.pop(0)
        i += timedelta(days=1)
    plt.title(stock_name + " from " + start.strftime("%B %d, %Y") + " to " + end.strftime("%B %d, %Y"))
    plt.show()
