# Pandas - Cleaning Data of Wrong Format
import pandas as pd 
df = pd.read_csv('data.csv')
print(df.to_string())
print()
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())