import sys, datetime
import pandas_datareader as pdr
import pandas as pd
import matplotlib.pyplot as plt
from viterbi import Viterbi
from config import initial, trans, emiss

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Invalid amount of arguments")
        sys.exit(0)
    stock_name = sys.argv[1]
    #dates MUST be in mm/dd/yyyy in order for this to work
    try:
         start = datetime.datetime.strptime(sys.argv[2], "%m/%d/%Y")
         end = datetime.datetime.strptime(sys.argv[3], "%m/%d/%Y")
    except ValueError:
        print("All dates must be in mm/dd/yyyy format")
    try:
        hist_prices = pdr.DataReader(stock_name, "yahoo", start, end)
    except:
        print("There was a problem getting the data from Yahoo finance. (I swear this isn't my fault - Yahoo changed their API to only work like a third the time)")
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
    # # print(obs)
    possible_obs = ["Up", "Down"]
    v = Viterbi(initial, states, obs, possible_obs, trans, emiss)
    v.run()
    #v.print_table()
    #v.print_backtrack_table()
    #v.print_backtrack()

    #LONG
    #print(v.get_backtrack())
    #print(obs_prices)
    #END LONG


    #hist_prices = hist_prices['Adj Close']
    #make a graph
    backtrack = v.get_backtrack()
    backtrack.pop(0)
    #backtrack_prob = v.get_backtrack_probabilites()
    #backtrack_prob.pop(0)
    to_print = pd.DataFrame(hist_prices['Adj Close'])
    to_print["Delta"] = obs_delta
    to_print["Output"] = backtrack
    #to_print["Probabilities"] = backtrack_prob
    print(to_print)
    hist_prices['Adj Close'].plot(grid="True")
    # fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1)
    # ax.plot(hist_prices.index, hist_prices['Adj Close'], label=stock_name)
    # ax.set_xlabel('Date')
    # ax.set_ylabel('Adjusted closing price ($)')
    # ax.legend()
    #plt.show()
