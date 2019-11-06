import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = [(x, x**2) for x in np.arange(10)]
x = [x[0] for x in data]
y = [x[1] for x in data]
print(x,y)


plt.figure(1)
plt.plot(x, y, 'bo', y, x, 'rx')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('do kwadratu')
# plt.legend(title='Test')


plt.figure(2)
plt.bar(x, y)


plt.figure(3)
plt.barh(x, y, color='red', label='red')


plt.figure(4)
index = np.arange(5)
width = 0.3
plt.bar(index, [1,2,3,4,5], width, color='red', label='x')
plt.bar(index + width, [1,2,3,4,5], width, color='black', label='y')
plt.title('Divisions')


plt.figure(5)
plt.scatter(x,y)


plt.figure(6)
plt.hist(y,10)


plt.figure(7)
explode = [0.3, 0, 0, 0.3, 0]
plt.pie([10,20,20,20,30], explode=explode,  shadow=True, startangle=45)


# plt.figure(8)
# plt.box(x)

plt.figure(9)
plt.subplot(2,2,1)
plt.plot(x,y, 'ro')
plt.subplot(2,2,2)
plt.plot(x,y, 'bx')
plt.subplot(2,2,4)
plt.bar(x,y)

# plt.show()
######################


df = pd.read_csv('movie_metadata.csv', index_col='movie_title')

df = df[df['budget'] < 10000]
# print(df.columns)
df.plot(kind='sacatter', x='imdb_score', y='budget')
plt.show()

