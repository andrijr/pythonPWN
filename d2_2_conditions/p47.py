# p47

# Używając kaskady instrukcji if sprawdź czy dwa pierwsze elementy listy przyjmują wartości dodatnie.
# Dodatkowo wypisz komunikaty w przypadku gdy tylko jeden z elementów listy spełnia ten warunek


lista = [-2,1,3,4,6,7,8]
if lista[0] > 0 and lista[1] >0:
    print("pierwsze dwa elementy są dodatnie")
elif lista[0] > 0 or lista[1] >0:
    print("tylko jeden element z pierwszego i drugego elementu są dodatnie")
else:
    print("Zaden z dwóch pierwszych elementó listy nie są dodatnie")