#!/usr/bin/python3
#Faça um programa que leia duas notas e calcule a media - notas maiores que 7 - aprovado. 
#entr 3 e 7 recuperacao, menor ou igual a 3 reprovado
nota1 = int (input ('Digite sua primeira nota:'))
nota2 = int (input ('Digite sua segunda nota:'))
media = (nota1 + nota2) / 2
if media >= 7:
    print('media {} , aprovado'.format(media))
elif media <= 3:
    print('media {} , reprovado'.format(media))
else:
    print('media  {} , recuperacao'.format(media))
