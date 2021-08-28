import pandas as pd

data = pd.read_csv('./data/dementia_dataset.csv')

print(data.head())

def stat(x):
    return x

temp = stat("Hello World")
print(temp)