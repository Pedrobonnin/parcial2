# from random import randint
# lista = []

# for i in range (0,78):
#     nummero1 = randint(1,134000)
#     lista.append(nummero1)

# lista.sort()

# print ("El menor es ",lista[0])
# print ("El mayor es ",lista[77])

# print(lista)
# for lista in range (0,78):
#     if (lista % 2==0):
#         print(lista)

from random import randint
lista = []

for i in range (0,78):
    num1 = randint(1,1200)
    lista.append(num1)

lista.sort()

print ("El menor es ",lista[0])
print ("El mayor es ",lista[77])

print(lista)
for lista in range (0,78):
    if (lista % 2==0):
        print(lista)