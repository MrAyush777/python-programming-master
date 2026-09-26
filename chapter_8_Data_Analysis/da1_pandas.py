# pandas library is used for data structure and data frames. It helps us to read the data that we want to get 

import pandas as pd

path = "C:/Users/Ayush/Downloads/sample-simple.csv"
data = pd.read_csv(path, header = None)
# print(data)

# head() : read first 6 lines of the file. By default returns first 5 lines 
print(data.head())
# print(data.head(6))

# tail() : read last 5 lines of the file. By default returns 5 last lines
# print(data.tail())
print(data.tail(5))

# data.to_csv(path) # to save the file on the specified path

print("DESCRIBE\n",data.describe())
# data.describe(include=all)

print("\nINFO",data.info())

print("COLUMNS : \n",data.columns)

print("DATATYPES USED IN THIS FILE : \  n",data.dtypes)
