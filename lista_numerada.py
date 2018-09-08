#!/usr/bin/python3

with open('nomes.txt','r') as arquivo:  
    conteudo = arquivo.readlines()

with open('nomes1.txt','w') as arquivo:
    for cont ,x in enumerate(conteudo):
        arquivo.write('{} -{}'.format(cont +1,x))
   