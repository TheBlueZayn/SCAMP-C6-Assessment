import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import 

df = pd.read_csv('fake_job_postings.csv')
print(df.head())

print(df.info())
print(df.fraudulent.value_counts())
print(df.nunique())
df.plot(x="industry", y="fraudulent", kind="bar", color="purple")
plt.show()