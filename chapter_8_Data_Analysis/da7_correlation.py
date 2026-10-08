import seaborn as sns
import pandas as pd
import numpy as np

dataFrame = np.random.randn(6,6)
flights = sns.heatmap(dataFrame,center=1)

from scipy import stats
flights = sns.load_dataset("flights") 

pearson_correlation = stats.pearsonr(flights['year'], flights['passengers'])
print(pearson_correlation) # it will show the correlation coefficient and p-value.
