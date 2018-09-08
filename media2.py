#!/usr/bin/python3
#Faça um programa que leia duas notas e calcule a media - quantas notas forem necessárias
# - notas maiores que 7 - aprovado. 
#entre 3 e 7 recuperacao, menor ou igual a 3 reprovado

qtd = int (input('Quantas notas deseja inserir? '))

soma = 0

for x in range(qtd):
    nota = int(input('Digite nota '))
    if nota > 10:
        print ('nota invalida')
        continue
    soma += nota
    #soma incrementa nota que é digitada
    
media = soma / qtd


if media >= 7:
    print('media {} , aprovado'.format(media))
elif media <= 3:
    print('media {} , reprovado'.format(media))
else:
    print('media  {} , recuperacao'.format(media))