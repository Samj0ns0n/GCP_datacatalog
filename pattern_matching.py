import pandas as pd
import re

DATETIME = "DATETIME"
TIME = "TIME"
DATE = "DATE"
INTEGER = "INTEGER"
FLOAT = "FLOAT"
BOOLEAN = "BOOLEAN"
NUMERIC = "NUMERIC"
GEOGRAPHY = "GEOGRAPHY"
STRING = "STRING"

PATTERN_FLOAT = '[+-]?([0-9]*[.])?[0-9]+'
PATTERN_STRING = '[a-z]'
PATTERN_NON_NUMBER = '[^a-zA-Z0-9]'
PATTERN_DATE = r'^(\d{4})-(0[1-9]|1[0-2]|[1-9])-([1-9]|0[1-9]|[1-2]\d|3[0-1])'
PATTERN_TIME = '^(0[1-9]|1[0-9]|2[0-3]):(0[0-9]|[0-5][0-9]):(0[0-9]|[0-5][0-9])'
PATTERN_DATETIME =  r'^(\d{4})-(0[1-9]|1[0-2]|[1-9])-([1-9]|0[1-9]|[1-2]\d|3[0-1]) (0[1-9]|1[0-9]|2[0-3]):(0[0-9]|[0-5][0-9]):(0[0-9]|[0-5][0-9]).(\d{6}) (UTC)'
PATTERN_BOOL = '(VRAI|vrai|Vrai|FAUX|Faux|faux|OUI|Oui|oui|NON|Non|non|YES|Yes|yes|NO|No|no|TRUE|True|true|FALSE|False|false)'

def find_pattern(date, pattern):

    c_true = 0 

    if date.dtypes == 'object': 
        date_test = date.str.contains(pattern, regex = True, na=True)
        c_true = date_test.astype(str).tolist().count('True')

    if c_true == len(date):
        return True
    else:
        return False


def pattern_match(tab_types, tab_column, dataframe):
    # pattern matching
	
	
	'''
    print("type de tab_column ",type(tab_column))
    print("type de tab_type ",type(tab_types))
    print("type de dataframe ",type(dataframe))
      
    print("tab_column dans pattern_matching = ",tab_column)
    print("tab_type dans pattern_matching = ",tab_types)
    print("dataframe dans pattern_matching = ",dataframe)
	'''
	
    for elements in tab_column:

        # print("pattern  = ",dataframe[elements].values)

        date = find_pattern(dataframe[elements],PATTERN_DATE)
        time = find_pattern(dataframe[elements], PATTERN_TIME)
        datetime = find_pattern(dataframe[elements], PATTERN_DATETIME)
        floating = find_pattern(dataframe[elements], PATTERN_FLOAT)
        boolean = find_pattern(dataframe[elements], PATTERN_BOOL)

        if datetime or dataframe[elements].dtypes == 'datetime64[ns]' :
            tab_types[elements] = DATETIME
        elif time:
            tab_types[elements] = TIME
        elif date:
            tab_types[elements] = DATE
        elif floating or dataframe[elements].dtypes == 'float64':
            tab_types[elements] = FLOAT
        elif dataframe[elements].dtypes == 'Int64':
            tab_types[elements] = INTEGER
        elif boolean or dataframe[elements].dtypes == 'bool':
            tab_types[elements] = BOOLEAN
        else:
            tab_types[elements] = STRING
    # print("Table des colonnes apres pattern matching : ", tab_types)
	
    return tab_types