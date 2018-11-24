import variables_eshop
import csv
import os

class LoadCSV(object):
    """
    Simple library for loading .csv files. Useful for loading test data.

    = Table of content =

    - Keywords
    """

    ROBOT_LIBRARY_VERSION = 1.0
    ROBOT_LIBRARY_SCOPE = 'TEST CASE'

    def get_all_rows(self, file=None, delimiter=';', header=True):   
        """
        Loads data from .csv file and returns a list of rows where every row is represented as a list of values.
        If there is an empty row in .csv file, the resulting list representing usch a row will be ''. It's useful if there is a need to test empty values in fields on a webpage.
        It's possible to specify a delimiter and whther or not the .csv file has a header.
        
        Example:
        | ${all_rows_from_csv} | Get All Rows | my_test_data.csv | ; | True |
        | ${all_rows_from_csv} | Get All Rows | my_test_data.csv | , | True |
        | ${all_rows_from_csv} | Get All Rows | my_test_data.csv | ; | False |
        """     
        all_rows = list()
        variables = variables_eshop.get_variables()
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), variables['REL_DATA'] + file)), 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=delimiter)
            for row in reader:
                if len(row) > 0:
                    all_rows.append(row)
                else:
                    all_rows.append([''])
        if header and len(all_rows) > 0:
            all_rows.pop(0)
        return all_rows
