# report.py
# exercise 3.15

import fileparse_3p10 as fp

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = fp.parse_csv(filename, select=['name','shares','price'], types=[str,int,float])
    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    pricelist = fp.parse_csv(filename, types=[str,float], has_headers=False)
    prices = dict(pricelist)
    return prices

def make_report_data(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change        = current_price - stock['price']
        summary       = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows

def print_report(report):
    # Output the report
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        print('%10s %10d %10.2f %10.2f' % row)

def portfolio_report(portfolio_filename, prices_filename):
    # Read data files and create the report data        
    portfolio = read_portfolio(portfolio_filename)
    prices    = read_prices(prices_filename)
    # Generate the report data
    report    = make_report_data(portfolio, prices)
    print_report(report)

def main(argv):

    if len(argv) != 3:
        raise SystemExit(f'Usage: {argv[0]} ''portfolio pricefile')
    portfolio_file = argv[1]
    prices_file = argv[2]
    portfolio_report(portfolio_file, prices_file)

if __name__ == '__main__':
    import sys
    main(sys.argv)
