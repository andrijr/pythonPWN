import matplotlib.pyplot as plt
import numpy as np


plt.figure(1, figsize=(15, 5))
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.figure(2, figsize=(15, 5))
plt.plot([1, 2, 3, 4], [1, 4, 9, 25], 'go')


x = np.arange(1, 5)
y = x**3

plt.figure(3, figsize=(10, 10))
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'go', x, y, 'rx')

plt.figure(4)
plt.subplot(2, 3, 1)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('1 plot')


plt.subplot(2, 3, 5)
plt.plot(x, y, 'rx')
plt.title('5 plot')
plt.suptitle('Sub title')

plt.figure(6)
divisions = ['A', 'B', 'C', 'D', 'E']
divisions_average = [70, 82, 73, 65, 68]
variance = [4, 6, 7, 8, 10]

plt.bar(divisions, divisions_average, yerr=variance, color='blue')

plt.figure(7)
plt.barh(divisions, divisions_average, xerr=variance, color='green')


plt.figure(8)
next_divisions_average = [69, 70, 75, 69, 72]

index = np.arange(5)
width = 0.3
plt.bar(index, divisions_average, width, color='red', label='Divisions')
plt.bar(index + width, next_divisions_average, width, color='black', label='Next divisions')
plt.title('Divisions')

plt.xlabel('First division')
plt.ylabel('Next division')
plt.legend()


plt.figure(9)
firms = ['Google', 'Amazon', 'PWN', 'ABC', 'SpaceX']
market_share = [35, 25, 10, 10, 20]
explode = [0.1, 0, 0, 0, 0]
plt.pie(market_share, explode=explode, labels=firms, shadow=True, startangle=45)
plt.axis('equal')
plt.legend(title='Firms')


plt.figure(10)
x = np.random.randn(100)
plt.hist(x, 10)


plt.figure(11)
y = np.random.randn(100)
plt.scatter(x, y)

plt.show()

