# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    '''Reads and stores the portfolio in a list'''
    # portfolio = []
    types = [str, int, float]
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
    #     for row in rows:
    #         holding = dict(zip(headers,row))
    #         portfolio.append(holding)
        # portfolio = [dict(zip(headers,row)) for row in rows]
        # Previous line but now converting the values in row to the right data type:
        portfolio = [dict(zip(headers,[func(val) for func, val in zip(types, row)])) for row in rows]
        # Alternative:
        # portfolio = [{name: func(val) for name, func, val in zip(headers, types, row)} for row in rows]

    return portfolio

def read_prices(filename):
    '''Reads and stores prices for a list of stocks'''
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print('Found an empty row')
            
            
    return prices

def make_report(portfolio,prices):
    # report_table = []
    # for row in portfolio:
    #     stock_details = (row['name'],int(row['shares']),prices[row['name']],prices[row['name']]-float(row['price']))
    #     report_table.append(stock_details)
    report_table = [(row['name'],row['shares'],prices[row['name']],prices[row['name']]-row['price']) for row in portfolio]
    return report_table

# Data files
import sys
if len(sys.argv) == 3:
    filename = sys.argv[1]
    pricesfile = sys.argv[2]
else:
    sys.exit('Error with file names')

portfolio = read_portfolio(filename)
prices = read_prices(pricesfile)

# Calculate Portfolio Current Value and Gain/Loss Current Result
Value = sum([d['shares'] * prices[d['name']] for d in portfolio])
Gain = sum([d['shares'] * (prices[d['name']]-d['price']) for d in portfolio])

print('Portfolio Value:', Value)
print('Portfolio Gain',Gain)

# Creating formatted table
headers = ('Name','Shares','Price','Change')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
separator = '-'
print(f'{separator:->10s} {separator:->10s} {separator:->10s} {separator:->10s}')
report = make_report(portfolio, prices)
for name, shares, price, change in report:
    price = '$'+f'{price:0.2f}'
    # print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
    print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')