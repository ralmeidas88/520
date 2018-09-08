#!/usr/bin/python3

convidados = ['daniel', 'maria', 'joao']

try:
    pos = int(input('Digite a posicao do convidado '))
    print(convidados[pos -1])
except ValueError:
    print ('so é valido numeros')
except IndexError:
    print ('a lista tem {} convidados'.format(len(convidados)))
except Exception as e:
    print("Erro:{}".format(e))
