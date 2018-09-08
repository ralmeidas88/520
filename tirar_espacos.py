#!/usr/bin/python3

with open ('espacos.txt', 'r') as arq:
    conteudo = arq.readlines()

aux = []
for x in conteudo:
    if x == '\n':
        continue
    aux.append(x)

print(aux)
