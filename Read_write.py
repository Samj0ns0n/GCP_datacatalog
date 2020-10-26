from google.cloud import storage

def selection(bucket_name):

    counter = True
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)
   
    # Choisi le premier fichier csv du bucket
    for blob in blobs:
        if ".csv" in blob.name and counter == True:
            path_to_csv = blob.name
            counter = False
            print(path_to_csv)
    return path_to_csv
