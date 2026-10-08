import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


path = "C:/Users/Ayush/Downloads/Book2.xlsx"
df = pd.read_excel(path)
print(df)

# SCATTER PLOT.

x = df["Name"]
y = df["Marks"]
plt.scatter(x,y)
plt.title("Scatter Plot - student with markls")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.show()



# BOX PLOT

a = sns.boxplot(x="Name", y="Marks", data=df)
plt.title("Box plot")
plt.xlabel("Name")
plt.show()