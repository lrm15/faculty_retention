import pandas as pd
from pathlib import Path 

df = pd.read_csv('faculty20-21.csv')
df.drop("Unnamed: 0", inplace=True, axis=1)

print(df)