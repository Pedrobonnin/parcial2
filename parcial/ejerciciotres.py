from random import randint
for i in range (0,78):
    numero= randint (0,10000000)

lista = []

for i in range (0,78):
    numero_1 = randint(1,10000000)
    lista.append(numero_1)

lista.sort()

print ("El menor es ",lista[0])
print ("El mayor es ",lista[77])

print(lista)
for lista in range (0,78):
    if (lista % 2==0):
        print(lista)