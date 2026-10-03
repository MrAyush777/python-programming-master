# BINNING IN PYTHON

import pandas as pd
import numpy as np

path = "C:/Users/Ayush/Downloads/Book1.xlsx"

df = pd.read_excel(path)

# 1) NUMERICAL TO CATEGORICAL DATA CONVERSION :

df["length"] = pd.to_numeric(df["length"], errors='coerce')
bins = np.linspace(min(df["length"]), max(df["length"]),4)

group_names = ["small","medium","large"]

df["length-binned"] = pd.cut(df["length"], bins, labels=group_names, include_lowest=True)

print(df.head())

# 2) CATEGORICAL TO NUMERICA DATA CONVERSION :

print(pd.get_dummies(df["length"]))
# it will convert a categorical data into binary data. like True/False or 1/0. It will create a new column for each category and assign 1 or 0 based on the presence of that category in the original column.

# ================================================

print("Description:\n", df.describe())
# it will give the statistical summary of the data. It will give the count, mean, std, min, 25%, 50%, 75% and max values of the data.

# ===============================================

index = pd.Index(df["length"])
print(index)

print(index.value_counts())
# this was used to count the repetition of the values in the column. It will give the count of each unique value in the column.
