#!/usr/bin/python3
numeros = [2,5,9,8,6,3,10]
par = []
impar = []

for x in numeros:
    if x % 2 == 0:
        continue
    impar.append(x)

print(impar)