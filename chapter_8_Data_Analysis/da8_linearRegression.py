import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

dataFrame = np.random.randn(6,6)
flights = sns.heatmap(dataFrame,center=1)

from scipy import stats
flights = sns.load_dataset("flights") 


# SIMPLE LINEAR REGRESSION
lm = LinearRegression()

x = flights['year']
y = flights['passengers']

Yhat = lm.predict(x)
print(Yhat)

lm.intercept_

lm.coef_

# MULTIPLE LINEAR REGRESSION
print(dataFrame)

x = dataFrame[['A',"B","C"]]
y = dataFrame['D']

lm.fit(x,y)

Yhat =  lm.predict(x)
print(Yhat)

lm.intercept_

lm.coef_


# REGRESSION PLOT : it is similer to the scatter plot but it also includes the regression line
# vertical axis = dependent 
# horizontal axis = independent 
# -> it needs seaborn and matplotlib library

sns.regplot(x="year",y="passengers", data=flights)
plt.ylim(0,500) # limiyt of y axis





