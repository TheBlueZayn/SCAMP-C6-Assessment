from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('fake_job_postings.csv')
print(df.head())
print(df.info())
df["location"].isin(["..."]).sum()

df["salary_range"].unique()
df["salary_range"].replace(["9-De", "3-Apr", "4-Apr", "Oct-15", "4-Jun", "10-Oct", "Jun-18", "11-Nov", "10-Nov", "11-Dec", "2-Apr", "2-Jun", "Dec-25"], np.nan, inplace=True)
df["salary_range"].unique()
print(df.info())

df.isna().sum().plot(kind="bar", rot=45)

plt.show()


plt.style{"white-grid"}
x = df.groupby("industry")["fraudulent"].sum().sort_values(ascending=False)[:15].reverse()
print(x)
x.plot(kind="barh",color="purple")
plt.xlabel("Number of fraudulent job posting")
plt.title("Number of Fraudulent job posting per industry")
plt.show()







