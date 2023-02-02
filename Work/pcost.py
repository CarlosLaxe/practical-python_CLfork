# pcost.py
#
# Exercise 1.27
import sys

def portfolio_cost(filename):
    'Calculate portfolio value'

    import csv
    Total_cost = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno,row in enumerate(rows,start=1):
            record = dict(zip(headers,row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                Total_cost += nshares * price
            # This catches errors in int() and float() convertions above
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    
    return Total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)