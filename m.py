from os import system

system("cls")
s = input("0 va 1 qilib str son kiriting: ")
n = list(s)
count = 0
for i in n:
    if int(i) >= 1:
            break
    if int(i) == 0:
        count += 1
print(count)

 