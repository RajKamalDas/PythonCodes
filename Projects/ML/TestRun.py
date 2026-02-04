#Importing Necessary Libraries.
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Fetch Data
df = pd.read_csv("https://rcs.bu.edu/examples/python/DataAnalysis/Salaries.csv")

#pd.cut(df.salary, bins=) #Figure out binning.

sns.scatterplot(y=df.service, x=df['salary'])
plt.show()