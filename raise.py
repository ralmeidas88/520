#!/usr/bin/python3

try:
    ling = input('qual a melhor linguagem de programacao? ')
    if ling != 'python':
        raise ValueError("linguagem errada")
except ValueError as e:
    print(e)