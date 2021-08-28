import pandas as pd

data = pd.read_csv('./data/test_data.csv')

print(data.head())

def stat(x):
    return x

temp = stat("Hello World")
print(temp)