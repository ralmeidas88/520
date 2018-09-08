#!/usr/bin/python3
numeros = [2,5,9,8,6,3,10]
#par = []

# for x in numeros:
#     if x%2 == 0:
#         par.append(x)
# print(par)

#OU 

par = [x for x  in numeros if x % 2 ==0]
print(par)

