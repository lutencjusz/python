a = 2
b = 20
while a < 10:
    print (str(a) + "<")
    a +=1
    if a%2 == 0:
        print (str(a) + "> jest parzyste")
        continue # idzie od razu do końca pętli i sprawdza else
    else:
        print (str(a) + ">") # nie idzie do konca, tylko bada następny warunek
    if a > b:
        print (str(a) + "> większe od 5")
        break # przerywa pętle i nie wykonuje else:
else:
    print ("Nie udało się ur. pętli")
print ("Koniec bloku")
print ("****************")
wyraz = ['ala', "ma", ['kota', 'psa']]

for w in wyraz:
    for l in w:
        print(l)
    print ('Koniec wyrazu') # wykonuje po każdym zakończeniu pętli
print('Koniec pętli')

litery = ['a', 'b', 'c', 'd']
liczby = [20, 21, 22, 23, 24]
print("*** pętle ***")

from itertools import *

for i in repeat("czesc", 4): # powtrza element określoną ilość razy; cycle i count pokazują w nieskończoność
    print(i)

for i, (lit, licz) in enumerate(product(litery, liczby), 1): # enumerator jest licznikiem
    # product tworzy iloczyn katerzjański
    print (i, lit, licz)

print("***permutacje z powtórzeniami***")
print(list(enumerate(product (range(2), repeat=4),1))) # pokazuje liste wartości 2 i ich reprezentacje 10

print("***permutacje***")
for i,(lit) in enumerate(permutations(litery, 2),1): # mozliwe permutacje 2 elementowe np. mecze z rewanżami
    print(i, lit)
print(i)

print("***kombinacje***")
for i,(lit) in enumerate(combinations(litery, 2),1): # mozliwe kombinacje, np. mecze grupowe
    print(i, lit)
print(i)

print('***chain***')
for i in chain(litery, liczby): # najpierw i z jednej kolekcji, potem następna
    print(i)

print('***słownik***')
for i in zip(litery, liczby): # słownik
    print(i)

print('***zip***')
z = dict(zip(litery, liczby))
print(z) # w formacie json
print([*z])

print('***unzip***')
i = [*zip(litery, liczby)]
print(i)
print('***i z * ***')
print(*i)
x, y = zip(*i)
print(x)
print(y)



