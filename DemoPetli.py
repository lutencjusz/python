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
