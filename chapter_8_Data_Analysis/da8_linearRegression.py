import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression

dataFrame = np.random.randn(6,6)
flights = sns.heatmap(dataFrame,center=1)

from scipy import stats
flights = sns.load_dataset("flights") 


lm = LinearRegression()

x = flights['year']
y = flights['passengers']

Yhat = lm.predict(x)
print(Yhat)

lm.intercept_

lm.coef_