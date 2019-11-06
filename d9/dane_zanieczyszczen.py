import pandas as pd


# KpWloclOkrze-PM10-1g
data = pd.read_excel('~/Downloads/Wyniki pomiarów z 2018 roku/2018_PM10_1g.xlsx')[21]
data = data[5:]
data = pd.Series([int(x.replace(',', '.')) if type(x) == str else 0 for x in data])
print(data.dtypes)

# TODO plot, porownac dwie stacje, zbadac wszystkie stacje w zaleznosci miesiecy

# mnist