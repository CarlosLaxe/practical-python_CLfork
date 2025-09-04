# fileparse.py
#
# Exercise 3.10

import csv

def parse_csv(filename, select=None, types=None, has_headers=True,delimiter=',',silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    try:
        if select and not has_headers:
            raise RuntimeError('select argument requires column headers')
        
        with open(filename) as f:
            rows = csv.reader(f,delimiter=delimiter)

            # Read the file headers (if any)
            headers = next(rows) if has_headers else []

            # If a column selector was given, find indices of the specified columns.
            # Also narrow the set of headers used for resulting dictionaries
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select

            records = []
            for row_number, row in enumerate(rows, start=1):
                if not row: # Skip rows with no data
                    continue

                # Filter the row if specific columns were selected
                if select:
                    row = [row[index] for index in indices]

                # Apply type conversion to the row
                if types:
                    try:
                        row = [func(val) for func, val in zip(types,row)]
                    except ValueError as e:
                        if not silence_errors:
                            print(f'Row {row_number}: Couldn\'t convert {row}')
                            print(f'Row {row_number}: Reason {e}')
                        continue

                # Make a dictionary or a tuple
                if headers:   
                    record = dict(zip(headers, row))
                else:
                    record = tuple(row)
                records.append(record)
        return records

    except RuntimeError as e:
        if not silence_errors: print(e)

    
