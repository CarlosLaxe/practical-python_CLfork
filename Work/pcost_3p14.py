# pcost.py
#
# Exercise 3.14

import sys
from report_3p12 import read_portfolio

def portfolio_cost(filename):
    'Calculate portfolio value'

    Total_cost = 0
    portfolio = read_portfolio(filename)
    for stock in portfolio:
        nshares = stock['shares']
        price = stock['price']
        Total_cost += nshares * price 
    return Total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)