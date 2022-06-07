import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('fake_job_postings.csv')

plt.plot()

# print(df.head())

# print(df.info())
# print(df.fraudulent.value_counts())
# print(df.nunique())

x = df.groupby("industry")["fraudulent"].sum()
print(x)
x.plot( kind="bar", color="purple")

# plt.xticks(rot=45)
# plt.show()

plt.bar(x, [1,1000])
plt.show()