import pandas as pd
import numpy as np
import csv

file_path = f"./datasets/csv/rooms.csv"
rooms_dataset = pd.read_csv(file_path, encoding="utf-8-sig", low_memory=False)
print(rooms_dataset.head(8))


