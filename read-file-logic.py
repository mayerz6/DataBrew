import pandas as pd
import numpy as np
import csv
import os

# rooms_dataset = pd.read_csv(file_path, encoding="utf-8-sig", low_memory=False)
# print(rooms_dataset.head(8))

file_path = f"./datasets/csv/rooms.csv" # Define path to your dataset file

# Examine the file's contents via CSV reader
with open(file_path, 'r', encoding="utf-8-sig", errors='strict') as infile:
    dialect = csv.excel
    dialect.delimiter = ','
    reader = csv.reader(infile, dialect)
    os.makedirs(os.path.dirname(f"./datasets/csv/rooms_processed.csv"), exist_ok=True)
    os.makedirs(os.path.dirname(f"./datasets/csv/rooms_garbage.csv"), exist_ok=True)
    
    with open(f"./datasets/csv/rooms_processed.csv", 'w', newline='', encoding='utf-8') as outfile, \
         open(f"./datasets/csv/rooms_garbage.csv", 'w', newline='', encoding='utf-8') as gfile:

        processed_writer = csv.writer(outfile)
        garbage_writer = csv.writer(gfile)    
        for row in reader:
            if row[1] == '1':
                processed_writer.writerow(row)
                print(row)
            else:
                garbage_writer.writerow(row)

