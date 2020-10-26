import pandas as pd
from google.api_core.exceptions import NotFound, PermissionDenied
from google.cloud import datacatalog_v1
from transformation import underscore_add

def gcp_datacatalog(tab_column, tab_types, bucket_name):

    project_id = 'lisea-mesea-sandbox-272216'
    location = 'us-central1'
    datacatalog = datacatalog_v1.DataCatalogClient()

    entry_group = datacatalog.list_entry_groups(
        parent=datacatalog.location_path(project_id, location)
        )
    
    '''
    for i in entry_group:
        print(i.display_name)

    entry_group_id = input("Veuillez créer ou update le nom du groupe d'entré : ")
    entry_id = input("Veuillez créer ou update le nom de l'entré : ")
    '''

    entry_group_id = "fileset_entry_group"
    entry_id = 'fileset_entry_id'

    entry_name = datacatalog.entry_path(project_id, location, entry_group_id, entry_id)
    entry_group_name = datacatalog.entry_group_path (project_id, location, entry_group_id)

    try:
        datacatalog.delete_entry(name=entry_name)
    except (NotFound, PermissionDenied):
        pass

    try:
        datacatalog.delete_entry_group(name=entry_group_name)
    except (NotFound, PermissionDenied):
        pass

    # -------------------------------
    # 2. Create an Entry Group.
    # -------------------------------
    entry_group_obj = datacatalog_v1.types.EntryGroup()

    # entry_group_obj.display_name = input("Entrez le nom du groupe d'entrée a afficher : ")
    # entry_group_obj.description = input("Entrez une description du groupe d'entrée : ")

    entry_group_obj.display_name = 'My filsetettttt'
    entry_group_obj.description = 'Description of fileset'

    entry_group = datacatalog.create_entry_group(
        parent=datacatalog_v1.DataCatalogClient.location_path(project_id, location),
        entry_group_id=entry_group_id,
        entry_group=entry_group_obj)
    print('Created entry group: {}'.format(entry_group.name))

    # -------------------------------
    # 3. Create a Fileset Entry.
    # -------------------------------

    entry = datacatalog_v1.types.Entry()

    entry.display_name = 'My Fileset'
    entry.description = 'This fileset consists of ....'
    # entry.display.name = input()
    # entry.description = input()

    entry.gcs_fileset_spec.file_patterns.append('gs://'+bucket_name+'/*')
    #entry.gcs_fileset_spec.file_patterns.append('gs://test-datapod/*')

    entry.type = datacatalog_v1.enums.EntryType.FILESET

    # Ajout underscore pour les fichiers sans header

    tab_column = underscore_add(tab_column)

    columns = []
    for i in range(len(tab_column)):
    # Create the Schema, for example when you have a csv file.
    
        columns.append(datacatalog_v1.types.ColumnSchema(
            column=tab_column[i],
            description='',
            type=tab_types[i]))

    entry.schema.columns.extend(columns)

    entry = datacatalog.create_entry(
        parent=entry_group.name,
        entry_id=entry_id,
        entry=entry)
    print('Created entry: {}'.format(entry.name))
