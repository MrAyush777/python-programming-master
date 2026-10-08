import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -------------------------------
# Generate sample data
# -------------------------------
# Create a DataFrame with random values
np.random.seed(42)  # For reproducibility
data = np.random.rand(6, 6)  # 6x6 matrix
df = pd.DataFrame(data, 
                  columns=['A', 'B', 'C', 'D', 'E', 'F'],
                  index=['Row1', 'Row2', 'Row3', 'Row4', 'Row5', 'Row6'])


# Create the heatmap

plt.figure(figsize=(8, 6))  # Set figure size
sns.heatmap(df, 
            annot=True,        # Show values in cells
            fmt=".2f",         # Format numbers
            cmap="YlGnBu",     # Color map
            linewidths=0.5)    # Line between cells

# Display the plot

plt.title("Sample Heatmap", fontsize=16)
plt.tight_layout()
plt.show()

data2 = np.random.randn(6,6)
print(data2)
# sns.heatmap(data2,center=0)

# =======================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

dataFrame = np.random.randn(6,6)
print(dataFrame)

heat_map = sns.heatmap(dataFrame, center=1)

flights = sns.load_dataset("flights")
flights = flights.pivot("month","year","passengers")
heat_map_2 = sns.heatmap(flights, annot=True, fmt=".1f")

heat_map_3 = sns.heatmap(flights, cmap = 'RdBu')

heat_map_4 = sns.heatmap(flights, cbar = False)

flights = sns.load_dataset("flights")
sns.regplot(x="passengers", y="year", data=flights)