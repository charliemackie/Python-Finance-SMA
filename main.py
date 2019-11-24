import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
import functools
import matplotlib as mpl

# Initialize and set the time periods that we want to analyze
start = datetime.datetime(2017, 1, 1)
end = datetime.datetime(2019, 11, 2)

# make a list of companies that should be tested
# Apple: AAPL, Microsoft: MSFT, Netflix: NFLX
stock_tickers = ['AAPL', 'MSFT', 'NFLX']

# Iterate over each company in the list and produce:
# 1. Graph of Moving average vs stick price
# 2. Average of the residual for each day moving average can be calculated
for i in range(len(stock_tickers)):
    # Read our data from Yahoo Finance
    df = web.DataReader(stock_tickers[i], 'yahoo', start, end)
    df.tail()

    # Create a list of the closing prices for each day within the time period
    close_price = df['Adj Close']

    # Calculate the moving average for each ticker with a 20 day period
    moving_avg = close_price.rolling(window=20).mean()

    # Adjusting the size of matplotlib
    mpl.rc('figure', figsize=(8, 7))

    # Adjusting the style of matplotlib
    style.use('ggplot')

    # Plot the Moving Average vs. Closing Price
    close_price.plot(label=stock_tickers[i])
    moving_avg.plot(label='moving_avg')
    plt.legend()
    plt.show()

    # Finally, Sum the the Residuals of Moving Average ~ Closing Price
    differences = []
    # Iterate over each list and calculate differences
    for j in range(len(close_price)):
        x = abs(moving_avg[j] - close_price[j])
        differences.append(x)

    # Eliminate the values that are of type 'nan'
    cleanedList = [x for x in differences if str(x) != 'nan']

    # Use the Reduce method and a short form function 'lambda' combine all elements of the list
    combined_value = functools.reduce(lambda a, b: a + b, cleanedList)

    # Calculate the average of the residuals
    average = combined_value / len(cleanedList)
    print("The residual average of " + stock_tickers[i] + " is: " + str(average))
