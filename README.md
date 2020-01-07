# SMA Trading Strategy

This is a basic Financial Analysis with Python. It uses a Simple Moving Average Concept to estimate the volatility of different Securities.

## Simple Moving Average:

The strategy being used will not tell you exactly which stock to pick or what price a stock will be at in the future. It is simply a way of comparing companies that are similar.

We will be using a SMA (Simple Moving Average) to determine how volatile a stock is. A Simple moving average can be calculated by taking any number of consecutive closing prices and dividing them by the period you chose.

The period of the SMA can be any natural number really (N > 0), but the most useful SMA values fall between 20–200 depending on the timeframe that is being used. A lower SMA value will respond faster to changes in the underlying price.
It is important to note that because our number of daily closing prices is finite there will be instances where the SMA cannot be calculated (i.e.; there are not enough future underlying prices to calculate the appropriate SMA). We will have to take this into account when writing the code.

## Residual:

In order to turn the SMA values calculated into a data that is interpretable, we will be calculating the difference between the underlying and the SMA value at each point where both are defined.
Then we can sum the differences and divide the sum by the number of values we found. This will give us a raw value that could potentially be compared to those of other similar companies.
