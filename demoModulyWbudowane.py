import sys

print (sys.version) # wersja pythona
for i in sys.builtin_module_names: # wbudowane moduły
    print(i) 

print (sys.getwindowsversion()) # wersja windowsów

import random as r

a = 2
b = 10
lista = [1, 2, 3, 4, 5, 6, 7]

def funkcja_losowa (f, args):
    print ("Początek funkcji: " + str (f))
    for i in range(1,10):
        print (f(*args))
    print ("Koniec funkcji: " + str (f))

funkcja_losowa(r.randint, (1,10))
funkcja_losowa(r.random, ())
print(r.choice('abcdefg'))
print(r.choice([1, 2, 5, 4]))

print("lista: " + str(lista))
r.shuffle(lista)
print("lista po shuffle: " + str(lista))
funkcja_losowa(r.sample, (lista, 3))

print ("***count***")
import itertools
for i in itertools.count(0.524):
    print (i)
    if i >= 10:
        break

print ("***datetime***")
import datetime as dt
funkcja_losowa(dt.date, (r.randint(2011,2012), r.randint(1,12), r.randint(1,31))) 
# argumnty są brane tylko na początku
print(str(dt.datetime.today()))
print(str(dt.datetime.now()))
print(str(dt.datetime.now().strftime("%d %b %Y")))