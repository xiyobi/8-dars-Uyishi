from os import system
from json import dumps



system("cls")
natija ={}
lst = []
lst2 = []
son = int(input("son kiriting: "))
son = list(str(son))

for i in son:
   natija[i] =  son.count(i)
new=sorted(natija.keys())
for i in new:
   print(i,"-",natija[i])

