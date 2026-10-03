# NORMALIZATION OF DATA : ALL METHODS BELOW : 

import pandas as pd

path = "C:/Users/Ayush/Downloads/Book1.xlsx"

df = pd.read_excel(path)
print(df.head())

# =========================================================================================

# 1) SIMPLE FEATURE SCALING MEHTOD : 
# formula : x(new) = x(old)/x(max)

print("====================SIMPLE FEATURE SCALING METHOD=====================\n")
df["length"] = pd.to_numeric(df["length"], errors='coerce')
df["length"] = df["length"] / df["length"].max()
print(df.head())

print(df.columns)
print(df["length"].dtype)

# 2) MIN-MAX METHOD :
# formula : x(new) =  x(old) - x(min) / x(max) - x(min)

print("\n====================MIN-MAX METHOD=====================\n")
df["length"] = (df["length"] - df["length"].min()) / (df["length"].max() - df["length"].min())
print(df.head())

# 2) Z-SCORE METHOD :
# FORMULA :  x(new) = x(old) - μ / σ

print("\n====================Z-SCORE METHOD=====================\n")
df["length"] = (df["length"] - df["length"].mean()) / df["length"].std();
print(df.head())