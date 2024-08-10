
from os import system
from json import dumps
system("cls")
def bigger_price(son, narx):
    s = sorted(narx, key=lambda x: x['price'], reverse=True)
    
    return s[:son]
son = int(input("son kiriting: "))

natija = (bigger_price(son,
 [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1},
]
))
print(dumps(natija,indent=4))
 