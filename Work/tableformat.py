# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()
    
    def row(self, rowdata):
        '''
        Emit a single rown of table data
        '''
        raise NotImplementedError()
    
class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print (f'{h:>10s}',end=' ')
        print()
        print(('-'*10+' ')*len(headers))
    
    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}',end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''
    def headings(self,headers):
        # Create opening <tr> tag, wrap each header in <th> tags, then closing </tr>
        th_tags = ''.join(f'<th>{h}</th>' for h in headers)
        print(f'<tr>{th_tags}</tr>')

    def row(self, rowdata):
        # Create opening <tr> tag, wrap each data item in <td> tags, then closing </tr>
        td_tags = ''.join(f'<td>{d}</td>' for d in rowdata)
        print(f'<tr>{td_tags}</tr')