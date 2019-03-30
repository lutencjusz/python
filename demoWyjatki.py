try:
    from datetime import time as t
except ImportError as iE:
    print ("Błąd: " + str(iE))
else:
    print("Zaimportowano time: " + str(t()))

a = 3
b = 0
try:
    print (a/b)
    if a/b < 0:
        raise ValueError
except ZeroDivisionError as e:
    print ("Wyjątek: " + str(e))
except ValueError as lU:
    print ("inny Wyjątek: " + str(lU))
else:
    print ("Ok, można dzielić przez "+ str(b))
finally:
    print ("Zawsze jest dzielenie")
print ("Koniec.")