from google.cloud import storage

def premier_csv(blob, counter):
    return blob.name

def selection(bucket_name):

    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)
   
    # Choisi le premier fichier csv du bucket

    csv_file = [blob.name for blob in blobs if ".csv" in blob.name]
    
	# print("First csv File name : ", csv_file[0])
    
    return csv_file
