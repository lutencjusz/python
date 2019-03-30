class Alerty:
    'komunikaty sygnalizujące aktualną sytuację lub zdarzenia nadzwyczajne'

    licznikAlertow = 0 # zmienna klasy dotyczy wszystkich instancji,
                       # w tym również dziedziczonych

    def __init__(self, n, o):
        self.naglowek = n
        self.opis = o 
        Alerty.licznikAlertow += 1
        print("Utworzono: " + str(Alerty.licznikAlertow) + " alerty")

    def string(self):
        print("nagłówek: " + self.naglowek + "; opis: " + self.opis) 

class Alerty_sterownika(Alerty):
    'Dziedziczy po alertach'
    def __init__(self, n, o, k, p):
        super().__init__(n, o) # odwołuje się do klasy bazowej
        self.klucz = k 
        self.priorytet = p
    
    def string(self): # przykrywa metodę klasy bazowej, klasą potomka
        super().string() # odwołuje się do klasy bazowej
        print("A z klasy Alert_sterownika:")
        print("klucz: " + self.klucz + "; priorytet " + str(self.priorytet)) 

print(Alerty.__doc__) # pokazuje to co jest w opisie
a1 = Alerty('naglowek', 'opis') # użycie konstruktora
a2 = Alerty('naglowek2', 'opis2') # użycie konstruktora
print(a1)
print(type(a1))
print("Nagłówek: " + a1.naglowek)
a1.string()
print(Alerty.licznikAlertow)

print('***klasa: Alerty_sterwnika***')
as1 = Alerty_sterownika("nagłówekS", "OpisS", "KluczS", 3)
as1.string()
