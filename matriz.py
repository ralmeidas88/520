#!/usr/bin/python3
#...
#dado a matriz, calcular a soma das diagonais

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

a = 0
b = 0
cont = 0

for x in matriz:
    a += (x[cont])
    cont += 1
    b += (x[-cont])
print(a+b)