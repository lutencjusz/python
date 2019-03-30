import tkinter as tk
from tkinter import messagebox as mb # musi być tak zrobione, bo samo tk nie działa
from tkinter import filedialog as fd

def zamknij_app():
    ex = mb.askyesno(title="Zamknij aplikację", message="Czy na pewno chcesz zamknąć?")
    if ex > 0:
        oGui.destroy()
        return

def otworz():
    fd.askopenfile()

oGui = tk.Tk() # tworzy obiekt okna
oGui.geometry('600x400') # parametry początkowe
oGui.title("Hello")

# przyciski
tk.Button(text="Otworz", command=otworz).place(x=100,y=350)
tk.Button(text="Zrób coś").place(x=200,y=350)
tk.Button(text="Zamknij", command=zamknij_app).place(x=300,y=350)

#Wtykiety
tk.Entry().place(x=10, y=40)
tk.Label(text="Podaj numer").place(x=10, y=10)

#Menu
pasekMenu = tk.Menu(oGui)

plikMenu = tk.Menu(pasekMenu, tearoff=0) # tearoff blokuje możliwość odpinania menu
plikMenu.add_command(label='Otworz', command=otworz)
plikMenu.add_command(label='Zrób coś')
plikMenu.add_command(label='Zamknij', command=zamknij_app)

pasekMenu.add_cascade(label='Plik', menu=plikMenu)

oGui.config(menu=pasekMenu)
oGui.mainloop() # pętla główna potrzebna w Windows, musi być na końcu
