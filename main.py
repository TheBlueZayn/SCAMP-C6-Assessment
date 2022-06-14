# Import libraries
from bs4 import Stylesheet
from matplotlib import style
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# Load CSv into a DataFrame
df = pd.read_csv('fake_job_postings.csv')

# Check out the first few rows
print(df.head())

# Get insights on the Data
print(df.info())

# Subset industry by the sum of fraudulent jobs and select the first 15 values
x = df.groupby("industry")["fraudulent"].sum().sort_values(ascending=False)[:15]

# View the subset
print(x)

# Plot, label accordingly and show the series
#fig, ax = plt.subplots(figsize=(15, 6))
plt.style.use("seaborn-pastel")
x.plot(kind="barh",
       color="purple",
       fontsize=8)
plt.xlabel("Number of fraudulent job postings")
plt.title("Fraudulent Job Postings Per Industry")
plt.show()

# Look up the unique values of "salary-range"
df["salary_range"].unique()

# Replace all non number ranges to null values, set inplace=True
df["salary_range"].replace(["9-De", "3-Apr", "4-Apr", "Oct-15", "4-Jun", "10-Oct", "Jun-18", "11-Nov", "10-Nov", "11-Dec", "2-Apr", "2-Jun", "Dec-25"], np.nan, inplace=True)

# Get a look into the info to confirm the change, a reduction in non-null values
print(df.info())


# Looking into the null values in each column and plotting it out
df.isna().sum().sort_values()[:10].plot(kind="bar", 
                                        rot=45, 
                                        figsize=(15,6), 
                                        logx=True)
plt.xlabel("Count")
plt.title("Distribution of null values")
plt.show()




print(df['department'].where(df['fraudulent'] == 1))








