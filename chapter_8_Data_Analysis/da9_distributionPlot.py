import seaborn as sns
import numpy as np

np.random.seed(0)
X = np.random.randn(100)
ax_1 = sns.displot(X)