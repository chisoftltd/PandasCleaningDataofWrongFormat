# Pandas - Cleaning Data of Wrong Format
import pandas as pd 
df = pd.read_csv('data.csv')
print(df.to_string())
print()
try:
    df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
    print(df.to_string())
except NameError as error:
    print("Format error")
print()

try:
    print(df.dropna(subset=['Transaction Date'], inplace = True))
except NameError as error:
    print(error)
    