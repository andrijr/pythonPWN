import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

n = 10
# data = [(i, x **2, x**x) for i, x in enumerate(range(n))]
data = [(x, x **2) for x in range(n) ]
print(data)

x = [x[0] for x in data]
y = [x[1] for x in data]
print(x)
print(y)
plt.plot(x, y)
plt.title='asd1'
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(title='Firms')
plt.show()

plt.plot(data)
plt.title='asd2'
plt.show()




print('###########')
df = pd.read_csv('movie_metadata.csv', index_col='movie_title')

df = df[df['budget'] < 500000]
df.plot(kind='scatter', x='imdb_score', y='budget', title='rating vs budged')
plt.show()

df['imdb_score'].plot(kind='hist', title='Score')
plt.show()

df['imdb_score'].plot(kind='box')
plt.show()

df['imdb_score'].plot(kind='bar')
plt.show()

df['imdb_score'].plot(kind='pie')
plt.show()




hist_2008 = df[df['title_year'] == 2008]['imdb_score']
hist_2009 = df[df['title_year'] == 2009]['imdb_score']
hist_2010 = df[df['title_year'] == 2010]['imdb_score']
hist_2011 = df[df['title_year'] == 2011]['imdb_score']

fig, axes = plt.subplots(nrows=2, ncols=2)

hist_2008.plot(ax=axes[0, 0], kind='hist')
hist_2009.plot(ax=axes[0, 1], kind='hist')
hist_2010.plot(ax=axes[1, 0], kind='hist')
hist_2011.plot(ax=axes[1, 1], kind='hist')
plt.show()