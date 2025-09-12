# pcost.py
#
# Exercise 3.15

from report_3p15 import read_portfolio

def portfolio_cost(filename):
    'Calculate portfolio value'

    Total_cost = 0
    portfolio = read_portfolio(filename)
    for stock in portfolio:
        nshares = stock['shares']
        price = stock['price']
        Total_cost += nshares * price 
    return Total_cost

def main(argv):
    
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} ''portfolio')
    cost = portfolio_cost(argv[1])
    print('Total cost:', cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)