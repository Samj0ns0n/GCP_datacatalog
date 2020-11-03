import pandas as pd
from google.api_core.exceptions import NotFound, PermissionDenied
from google.cloud import datacatalog_v1
from transformation import underscore_add

import google.auth
import google.oauth2.credentials
import google_auth_oauthlib


def gcp_datacatalog_update(tab_column, tab_types, bucket_name):

    project_id = 'lisea-mesea-sandbox-272216'
    location = 'us-central1'
    # project_id = input("Insérez l'id du projet : ")
    # location = input("Insérez la location : ")

    
    # credentials = google_auth_oauthlib.get_user_credentials(scopes, client_id, client_secret)

    credentials = google.oauth2.credentials.Credentials('')
    datacatalog = datacatalog_v1.DataCatalogClient(credentials=credentials)
    
    entry_group = datacatalog.list_entry_groups(
        parent=datacatalog.location_path(project_id, location)
        )

    entry_group_id = "fileset_entry_group"
    entry = datacatalog.list_entries(parent='projects/'+project_id+'/locations/'+location+'/entryGroups/'+entry_group_id)
    
    first_entry = [i.name for i in entry]

    # print(first_entry)
    
    entry_test = datacatalog.get_entry(first_entry[0])

    # print(entry_test)

    del entry_test.schema.columns[:]

    tab_column = underscore_add(tab_column)
    
    # print(tab_column)

    entry = datacatalog_v1.types.Entry()

    columns = []

    for i in range(len(tab_column)):
    
        columns.append(datacatalog_v1.types.ColumnSchema(
            column=tab_column[i],
            description='',
            type=tab_types[i]))

    
    entry_test.schema.columns.extend(columns) 

    entry = datacatalog.update_entry(entry_test)

    # print('Udated schema: {}'.format(entry.schema))

