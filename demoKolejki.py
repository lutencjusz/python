from collections import defaultdict

mq = defaultdict()
mq['1']='123'
mq['2']='234'
mq['3']='567'
mq['4']='567'
mq['5']='577'
print(list(mq.items())) # prezentuje zawartość
mq['1']='1221' # naspisuje zmienną o kluczu '1'
print(list(mq.items()))
print(mq.popitem()) # bierze ze stosu, !!! nie działa false
print(list(mq.items()))
print(mq.popitem()) 
print(list(mq.items()))
print(list(mq.keys())) # pokazuje tablice kluczy
print(list(mq.values())) # pokazuje tablice wartości
print(mq.pop('2')) # zdejmule z listy elemenent o kluczu 2 i pokazuje wartość
print(list(mq.items()))


lista = [] # ze wzgledów pamięciowych nie jest optymalna
lista.append(3)
lista.append(4)
lista.append(7)
lista.append(6)
lista.append('a')
print(list(lista))
print(lista.pop()) # pobiera z końca
lista.reverse() # odwraca listę
print(list(lista))
print(lista.pop(False)) #pobiera z początku
lista.sort(reverse=True) # sortuje liste w odwrotnym porządku
print(list(lista)) 

from collections import deque

kolejka = deque(maxlen=3) # tworzy kolejkę ograniczoną do trzech elementów
kolejka.append('ala')
kolejka.append('ma')
kolejka.append('kota')
kolejka.append('a')
print(list(kolejka)) # nie starczyło miejsca, więc wypchnął element
print(kolejka.popleft())
print(list(kolejka))
kolejka.append('kot')
print(list(kolejka))
kolejka.appendleft('ma') # wszedł z lewej, ale wypchnął tego z prawej
print(list(kolejka))