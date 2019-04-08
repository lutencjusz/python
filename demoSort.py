class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
    
    def __repr__(self): # zwraca to co ma zostać przekształcone na string
        return f'Osoba({self.imie}, {self.nazwisko})'
    
    def __lt__(self, other): # pokazuje wartości do sortowania
        return self.imie + self.nazwisko < other.imie + other.nazwisko

ludzie = [
    Osoba('Jan', 'Kowalski'),
    Osoba('Michał', 'Sobieraj'),
    Osoba('John', 'Rambo'),
    Osoba('Michał', 'Alabaster')
]

print (ludzie[0])
print(list(sorted(ludzie)))