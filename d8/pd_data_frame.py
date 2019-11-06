import pandas as pd
import numpy as np


df = pd.DataFrame({
     'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
     'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
     'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])
})

print('df\n',df)
print('head\n', df.head(3))
print('tail\n', df.tail(3))
print('count\n', df.count())
print('mean\n', df.mean())
print('median\n',df.median())
print('max\n', df.max())
print('min\n', df.min())
print('std\n', df.std())
print('corr\n', df.corr())

print('sort_values\n', df.sort_values('one'))
print('sort_values\n', df.sort_values('two', ascending=False))
print('sort_values\n', df.sort_values(['one', 'two'], ascending=[True, False]))
print('sort_index\n', df.sort_index())

print('groupby\n', df.groupby(['one']).mean())
print('drop_duplicates\n',df.drop_duplicates())

print('dropna\n', df.dropna())
print('dropna1\n', df.dropna(axis=0)) # usuń wiersze wktórych brakuję co najmniej jednego elementu
print('dropna2\n', df.dropna(axis=1)) # usuń kulumny wktórych brakuję co najmniej jednego elementu
print('dropna3\n', df.dropna(how='all')) # usuń wierszy/kolumny w których brakuję wszystkich elementów
print('dropna4\n', df.dropna(thresh=2)) # pozostaw elementy o co najmniej  n wartościach innych od NA
print('dropna5\n', df.dropna(subset=['one', 'three'])) # okreśł na podstawie któych kolumn usuwać brakujące elementy
# print('dropna6\n', df.dropna(inplace=True)) # zapisz DataFrame z poprawnymi danymi w tej samej zmiennej df


print('fillna\n', df.fillna(0)) # zamień wszystkie elementy NaN na 0
print('fillna1\n', df.fillna(df.mean()))
print('fillna2\n', df.fillna(method='ffill')) # zamień brakujące elementy z poprzedniego rekordu nie NaN
values = {'one': 0, 'two': 1, 'three': 2}
print('fillna3\n', df.fillna(value=values)) # zamień brakujące elementy z poprzedniego rekordu nie NaN

print('notna\n', df.notna()) # Wykryj istniejące  wartości.
print('isna\n', df.isna()) # Wykryj  brakujące wartości.


df1 = pd.DataFrame( {'one': pd.Series(np.random.randn(3)) } )
print(df1)
print('append\n', df1.append(df, sort=True)) # dodać df do df

# print(df.concat([df1, df], axis=1))
# doc string wytłumaczenie o klasie


df = pd.DataFrame([ [np.nan, 2, np.nan, 0],
                    [3, 4, np.nan, 1],
                    [np.nan, np.nan, np.nan, 5],
                    [np.nan, 3, np.nan, 4]],
                    columns=list('ABCD'))
print(df)
print(df.shape)