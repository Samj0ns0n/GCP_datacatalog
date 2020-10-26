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

pattern_float = '[+-]?([0-9]*[.])?[0-9]+'
pattern_string = '[a-z]'
pattern_non_number = '[^a-zA-Z0-9]'
pattern_date = r'^(\d{4})-(0[1-9]|1[0-2]|[1-9])-([1-9]|0[1-9]|[1-2]\d|3[0-1])'
pattern_time = '^(0[1-9]|1[0-9]|2[0-3]):(0[0-9]|[0-5][0-9]):(0[0-9]|[0-5][0-9])'
pattern_date_time =  r'^(\d{4})-(0[1-9]|1[0-2]|[1-9])-([1-9]|0[1-9]|[1-2]\d|3[0-1]) (0[1-9]|1[0-9]|2[0-3]):(0[0-9]|[0-5][0-9]):(0[0-9]|[0-5][0-9]).(\d{6}) (UTC)'
pattern_bool = '(VRAI|vrai|Vrai|FAUX|Faux|faux|OUI|Oui|oui|NON|Non|non|YES|Yes|yes|NO|No|no|TRUE|True|true|FALSE|False|false)'

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

    for i in range(len(dataframe.columns)):

        # print("pattern  = ",dataframe[tab_column[i]].values)

        date = find_pattern(dataframe[tab_column[i]], pattern_date)
        time = find_pattern(dataframe[tab_column[i]], pattern_time)
        datetime = find_pattern(dataframe[tab_column[i]], pattern_date_time)
        floating = find_pattern(dataframe[tab_column[i]], pattern_float)
        boolean = find_pattern(dataframe[tab_column[i]], pattern_bool)

        if datetime or dataframe[tab_column[i]].dtypes == 'datetime64[ns]' :
            tab_types[i] = DATETIME
        elif time:
            tab_types[i] = TIME
        elif date:
            tab_types[i] = DATE
        elif floating or dataframe[tab_column[i]].dtypes == 'float64':
            tab_types[i] = FLOAT
        elif dataframe[tab_column[i]].dtypes == 'Int64':
            tab_types[i] = INTEGER
        elif boolean or dataframe[tab_column[i]].dtypes == 'bool':
            tab_types[i] = BOOLEAN
        else:
            tab_types[i] = STRING

    # print("Table des colonnes apres pattern matching : "tab_types)
    return tab_types