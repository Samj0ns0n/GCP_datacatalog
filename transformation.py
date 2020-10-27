from google.cloud import storage
import pandas as pd
import numpy as np
import chardet
import gcsfs
import csv
import re
import io


def transformation_dataframe(bucket_name, blob_name):

    fs = gcsfs.GCSFileSystem(project_id="lisea-mesea-sandbox-272216")
    path_to_csv = "gs://" + bucket_name + "/" + blob_name

    # project = fs.ls(bucket_name)
    # print(project)
    with fs.open(path_to_csv, "rb") as csvfile:

        csv_test_bytes = csvfile.read(1024)
        infer_encoding = chardet.detect(csv_test_bytes)["encoding"]
        # print(infer_encoding)

    with fs.open("test-datapod/Test_header.csv", "rt") as csvfile:

        csv_test_bytes = csvfile.read(1024)
        csvfile.seek(0)

        has_header = csv.Sniffer().has_header(csv_test_bytes)
        dialect = csv.Sniffer().sniff(csv_test_bytes)

        csvfile.seek(0)
        # print(has_header, infer_encoding , dialect.delimiter)

        if dialect.delimiter == ";":
            dial_sep = ",|" + dialect.delimiter
        else:
            dial_sep = dialect.delimiter
        # print("Delimiter : ",dial_sep)

        if has_header:
            dataframe = pd.read_csv(
                csvfile,
                header=0,
                sep=dial_sep,
                engine="python",
                encoding=infer_encoding,
                quoting=csv.QUOTE_NONE,
            )
        else:
            dataframe = pd.read_csv(
                csvfile,
                header=None,
                sep=dial_sep,
                engine="python",
                encoding=infer_encoding,
                quoting=csv.QUOTE_NONE,
            )
        csvfile.close()

    # print("transformation dataframe = ",dataframe)

    # Conversion des types des colonnes

    dataframe_verif = dataframe.infer_objects()
    dataframe_verif = dataframe_verif.convert_dtypes()

    # print("types des colonnes : ", dataframe_verif.dtypes)
    # print("dataframe verif apres inferences des types : ", dataframe_verif)

    dataframe_verif = dataframe.apply(verification, axis=0)

    # print("types des colonnes après vérification : ", dataframe_verif.dtypes)
    # print("dataframe apres vérification : ", dataframe_verif)

    return dataframe_verif


def transformation_colonne(dataframe):

    # liste des colonnes

    tab_column = dataframe.columns.values.tolist()

    return tab_column


def underscore_add(list_colonne):

    tab_column = [str(i) for i in list_colonne]
    tab_column = ["_" + suit for suit in tab_column]

    return tab_column


def transformation_type(dataframe):

    # print("types des colonnes : ", dataframe.dtypes)

    tab_types_dtypes = dataframe.dtypes.tolist()
    tab_types = [str(i) for i in tab_types_dtypes]

    # print("tab_type = ", tab_types)
    return tab_types


def verification(x):
    if x.dtypes == type(str):
        return x.str.strip('"')
    else:
        return x
