from collections import Counter
from PIL import Image
from matplotlib.pyplot import barh

s = 'aaabbbccaa1122'
c = Counter(s)
print(c) # podaje ilość występujących elementów
for i in s:
    c[i] += 1 
print(c) #zsumował wcześnejsze klucze, jezęli pokazuje nie istniejący klucz, to ma wartość 0
print(list(c.elements())) # pokazuje jako tablicę znaków
print("most_common: " + str(c.most_common(3))) # pokauje trzy najbardziej popularne
