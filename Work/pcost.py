# pcost.py
#
# Exercise 6.2

from report import read_portfolio

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = read_portfolio(filename)
    return portfolio.total_cost

def main(argv):
    
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} ''portfolio')
    cost = portfolio_cost(argv[1])
    print('Total cost:', cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)