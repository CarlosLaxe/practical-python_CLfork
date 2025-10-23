# fileparse.py
#
# Exercise 3.17

import csv
import logging
log = logging.getLogger(__name__)

def parse_csv(lines, select=None, types=None, has_headers=True,delimiter=',',silence_errors=False):
    '''
    Parse a file-like iterable object into a list of records
    '''
    try:
        if select and not has_headers:
            raise RuntimeError('select argument requires column headers')
        
        if isinstance(lines, str): raise RuntimeError('Input must be an iterable object, e.g. the file rows not the file name')

        rows = csv.reader(lines, delimiter=delimiter)
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
                        log.warning("Row %d: Couldn't convert %s", row_number, row)
                        log.debug("Row %d: Reason %s", row_number, e)
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
