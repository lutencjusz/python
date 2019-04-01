licznik_linii = 0

def czytanie_pliku_generator (plik):
    global licznik_linii
    for linia in plik:
        if not linia.startswith('#'): # jeśli nie rozpoczyna się od komentarza
            licznik_linii += 1
            yield linia # zwraca linie jako generator

with open('parametryCz.json') as parametryPlik:
    for l in czytanie_pliku_generator(parametryPlik):
        print ("linia(" + str(licznik_linii) + "): " + l)

