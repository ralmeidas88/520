#!/usr/bin/python3
#...
#dado a matriz, calcular a soma das diagonais

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

soma = 0

for cont,x in enumerate(matriz):
    soma += x[cont]
    soma += x[-(cont+1)]

print(soma)