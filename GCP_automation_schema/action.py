from transformation import transformation_dataframe
from transformation import transformation_colonne
from transformation import transformation_type

from pattern_matching import pattern_match

from datacatalog import gcp_datacatalog
from datacatalog_update import gcp_datacatalog_update

import pandas as pd


def actions (bucket_name, blob_name):
    """Prints out a blob's metadata."""

    # transformation time 

    df = pd.DataFrame()
    df = transformation_dataframe(bucket_name, blob_name)

    # print("df = ",df)

    tab_types = transformation_type(df)
    tab_column = transformation_colonne(df)

    # print("tab_type = ",tab_types)
    # print("tab_colonne = ", tab_column)

    # pattern matching time 
    
    tab_types_test = pattern_match(tab_types, tab_column, df)
    
    # print(tab_types_test)

    # GCP datacatalog 
    
    gcp_datacatalog(tab_column, tab_types_test, bucket_name)
    # gcp_datacatalog_update(tab_column, tab_types_test, bucket_name)

 
