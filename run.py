import sys, datetime
import pandas_datareader as pdr
import pandas as pd
import matplotlib.pyplot as plt
from viterbi import Viterbi

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
    initial = [0.5, 0.5]
    states = ["Buy", "Sell"]
    obs = ["Up", "Up", "Down"]
    prev_price = 0
    for price in hist_prices["Adj Close"]:
        if price >= prev_price:
            obs.append("Up")
        else:
            obs.append("Down")
        prev_price = price
    # # print(obs)
    possible_obs = ["Up", "Down"]
    trans = [[0.5, 0.5], [0.5, 0.5]]
    emiss = [[0.5, 0.5], [0.5, 0.5]]
    v = Viterbi(initial, states, obs, possible_obs, trans, emiss)
    v.run()
    v.print_table()
    v.print_backtrack_table()
    v.print_backtrack()


    #hist_prices = hist_prices['Adj Close']
    #make a graph
    hist_prices['Adj Close'].plot(grid="True")
    # fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1)
    # ax.plot(hist_prices.index, hist_prices['Adj Close'], label=stock_name)
    # ax.set_xlabel('Date')
    # ax.set_ylabel('Adjusted closing price ($)')
    # ax.legend()
    # plt.show()
