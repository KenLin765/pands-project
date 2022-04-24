## Kenneth Linehan, 2022

#Analysis of Iris Data set

import pandas as pd
import numpy as np
import seaborn as sns

# This is used to read in the data:
data = pd.read_csv("iris.csv")

# This prints what the data compromises of:
print("Describes the data:")
data.describe()

print("\nInformation on the data:")
data.info()