import pandas as pd


# df = pd.read_csv("~/PycharmProjects/pythonPWN/d8/pokemon.csv", header =[1, 2])
# print(df)

# df = pd.read_csv("~/Downloads/pokemon.csv")
# df = pd.read_csv("~/PycharmProjects/pythonPWN/d8/pokemon.csv")
df = pd.read_csv("pokemon.csv")
print(df)
print(df.groupby('Type').count().sort_values('Pokemon'))
print(df.describe())


