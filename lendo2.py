#!/usr/bin/python3

# with open ('nomes.txt', 'a') as arquivo:
#     arquivo.write('terra\n')
#     arquivo.write('polvo\n')


#adicionando lista no arquivo 
nomes = ['yasmin', 'rafael', 'jessica']
with open('nomes.txt', 'a') as arquivo:
    arquivo.seek(0)
    arquivo.writelines(nomes)
