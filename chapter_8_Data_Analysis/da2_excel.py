import pandas as pd
import numpy as np

path = "C:/Users/Ayush/Downloads/Book1.xlsx"

df = pd.read_excel(path)
print(df)

# preprocessing the data : convergint the raw data into summarized form of data. You need to clean the data 

print(df.head())
# You can change headers shown in the output.

headers = ["--","Sr. No.","Even","Odd","Multiples of 5","Multiples of 3","Multiples of 4"]
df.columns = headers
print(df.head())

df["Odd"] = df["Odd"] + 1
print(df)

# while we run this file and if data of any cell in the file is empty than it will show NaN(Not a Number) instead that.

# =============================

# To remove and column :

# 1) First method :
# It will remove 10th raw
# removeRaw_1 = df.drop([10],axis=0)
# print(removeRaw_1)

# 2) Second method :
# it will remove all rows and columns
# removeRaw_2 = df.dropna()
# print("Using dropna : \n",removeRaw_2)

# 3) Third scenario :
# remove for specif row or column
# for column : it will delete 

# removeRow_3 = df.dropna(subset=["Sr. No."], axis=0)
# print(removeRow_3)


# YOU ALSO CAN REPLACE THE NaN WITH ANOTEHR VALUE. To do that you need to import the numpy library in your python working file LIKE THIS :

replace_NaN = df["Sr. No."].replace(np.nan,333)
print(replace_NaN)

# formatting columns :

df["Multiples of 3"] = df["Multiples of 3"]/2   
print(df.head()) 

# rename the column name : 

df.rename(columns={"Multiples of 3" : "Multiples of 2"})
print(df.head())

# know the data types 

print(df.dtypes)

# converting the datatype of a column : 

df["Multiples of 3"] = df["Multiples of 3"].astype("int")
print(df.head())
