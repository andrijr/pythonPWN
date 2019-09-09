import time, datetime, math


print((((time.time()/60)/60)/24)/365.25)

t = time.time()
lista = []
for x in range(1, 10000):
    lista.append(x**2)
print("czas trwania programu" , time.time()-t)

t = time.time()
lista = []
for x in range(1, 10000):
    lista.append(math.pow(x,2))
print("czas trwania programu" , time.time()-t)

# time.clock()
# lista = []
# # # for x in range(1, 10000):
# # #     lista.append(math.pow(x,2))
# # # print("czas trwania programu" , time.clock())

for x in range(0,5):
    print(5-x)
    time.sleep(0.5)

aktualnyCzas = datetime.datetime.now()
print(aktualnyCzas)
print(aktualnyCzas.day)
print(aktualnyCzas.month)
print(aktualnyCzas.year)