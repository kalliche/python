# leer archivo grande

import pandas as pd

def read_csv_in_chunks(file_name):
    for i, chunk in enumerate(pd.read_csv(file_name, chunksize=1000)):
        print("Chunk #{}".format(i))
        print(chunk)

read_csv_in_chunks('big_file.csv')

# leer archivo por lotes
import csv

def read_csv_in_chunks(file_name):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for i, chunk in enumerate(reader):
            print("Chunk #{}".format(i))
            print(chunk)

read_csv_in_chunks('big_file.csv')