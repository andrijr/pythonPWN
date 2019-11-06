import pandas as pd
import numpy as np


lista = np.random.randn(2)
print(lista)
df = pd.DataFrame(lista)
print(df)
print()

df = pd.Series(lista)
print(df)
print()

df = pd.DataFrame( {'kolumna': pd.Series(lista) } )
print(df)
print()



df = pd.DataFrame({'kolumna': pd.Series(lista, index=['a','b']) } )
print(df)

df = pd.DataFrame([lista, lista, ], columns=list('AB'))
print(df)


df = pd.read_csv('pokemon.csv')
print(df)

print(df.shape)
print(df.groupby(['Type']).count())
print(df.describe())
print( )
print(df.info())















