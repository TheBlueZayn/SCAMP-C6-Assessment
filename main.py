# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
x.plot(kind="barh",color="purple")
plt.xlabel("Number of fraudulent job postings")
plt.title("Number of Fraudulent job postings per industry")
plt.show()

# Look up the unique values of "salary-range"
df["salary_range"].unique()

# Replace all non number ranges to null values, set inplace=True
df["salary_range"].replace(["9-De", "3-Apr", "4-Apr", "Oct-15", "4-Jun", "10-Oct", "Jun-18", "11-Nov", "10-Nov", "11-Dec", "2-Apr", "2-Jun", "Dec-25"], np.nan, inplace=True)

# Get a look into the info to confirm the change, a reduction in non-null values
print(df.info())


# Looking into the null values in each column and plotting 
df.isna().sum().sort_values()[:10].plot(kind="bar", rot=45)
plt.xlabel("Count")
plt.title("Distribution of null values")
plt.show()

df["department"].unique()


print(df['department'].where(df['fraudulent'] == 1))








