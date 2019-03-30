print ("***funkcja podstawowa***")
def funkcja(lista, a=1, **poz): # kolejność argumentów obowiazkowe, nieobowiązkowe, opcjonalne
    print ('a: ' + str(a))
    for i in range (*lista): # dobieranie się do środka listy
        print (i)
    print ('pozostałe argumnety: ' + str(poz))
    return {poz['nazwa']: a * poz['cena']}

print("Wartość funkcji: " + str(funkcja(lista=[3, 10], cena=10, nazwa='chleb')))
print("***lambda***")
wl = lambda a, b: a * b # wl jest tak naprawdę nazwą funkcji lamdba
y = wl(2,3)
print('wl: ' + str(y))

print ("***generator***")
def generator_iterable (pocz=0, kon=10): # generator Iterable
    i = pocz
    while i <= kon:
        yield i # gromadzi wyniki i pzeakzuje jako iterable
        i += 1

for j in generator_iterable (kon=10, pocz=5):
    print(str(j))

print ("***funkcje argumenty***")
def suma (a, b):
        return a + b

def iloczyn (a, b, c=1):
        return a * b * c

def operacja_artm (f,args):
        print (str(f))
        return f(*args)

print(operacja_artm (suma, (2, 3)))
print(operacja_artm (iloczyn, (2, 3, 4)))

print("***moduły***")
import demoFunkcjeModul as dFM
print(operacja_artm(dFM.dzielenie, (2, 0)))
print(operacja_artm(dFM.suma, (2, 9)))


