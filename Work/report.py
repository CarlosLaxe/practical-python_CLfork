# report.py
# Exercise 6.2

import fileparse as fp
from stock import Stock
import tableformat
from portfolio import Portfolio

def read_portfolio(filename, **opts):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        portdicts = fp.parse_csv(lines, 
                                 select=['name','shares','price'], 
                                 types=[str,int,float],
                                 **opts)

    portfolio = [Stock(**d) for d in portdicts]
    return Portfolio(portfolio)

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    with open(filename) as lines:
        return dict(fp.parse_csv(lines, types=[str,float], has_headers=False))

def make_report_data(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock.name]
        change        = current_price - stock.price
        summary       = (stock.name, stock.shares, current_price, change)
        rows.append(summary)
    return rows

def print_report(report, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files 
    portfolio = read_portfolio(portfolio_filename)
    prices    = read_prices(prices_filename)
    # Generate the report data
    report    = make_report_data(portfolio, prices)
    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report,formatter)

def main(argv):

    if len(argv) < 3 or len(argv) > 4:
        raise SystemExit(f'Usage: {argv[0]} ''portfolio pricefile format(optional)')
    portfolio_file = argv[1]
    prices_file = argv[2]
    fmt = argv[3] if len(argv) == 4 else 'txt'
    portfolio_report(portfolio_file, prices_file, fmt)

if __name__ == '__main__':
    import sys
    main(sys.argv)
