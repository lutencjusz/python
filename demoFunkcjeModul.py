def suma (a,b):
    return a + b

def roznica (a,b):
    return a - b

def dzielenie (a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print ("próba dzielenia przez 0")
        return 0

def mnozenie (a,b):
    return a * b