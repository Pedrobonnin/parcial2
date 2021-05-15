
# 1. Utilizando la función get_charter_by_id consuma los datos de dos personajes de la
# api de Star Wars de manera aleatoria para resolver los siguiente:
# a. cual es el personaje más alto (indicar el nombre)
# b. cual es el personaje más pesado (indicar el nombre)
# c. cual personaje participó en más películas (si los dos participaron en la misma
# cantidad indicarlo) (indicar el nombre)
# d. determinar si alguno de los personajes aleatorios se llama Yoda o Grievous
# 2. Utilizando la función get_all_sw_characters consuma los datos de todos los
# personajes de SW y resuelva lo siguiente:
# a. Listado ordenado de manera creciente por nombre, mostrando nombre,
# especie y planeta natal
# b. Indicar los personajes que aparecieron en las 7 películas
# 3. Generar una lista de 77 números aleatoriamente resolver lo siguiente:
# a. indicar el valor menor
# b. indicar el valor mayor
# c. ordenar la lista de manera creciente y mostrar dichos valores
# d. eliminar de la lista los valores pares (o en su defecto hacer un barrido que
# solo muestre los pares)

# from consumo_api import get_charter_by_id

# from random import randint
# sw_data= get_charter_by_id



# num1= randint(1,83),
# num2= randint(1,83),

# print(num1)
# print(num2)

from consumo_api import get_charter_by_id

from random import randint
sw_data= get_charter_by_id

id1 = randint(1,83)
id2 = randint(1,83)

personaje1 = get_charter_by_id(id1)
personaje2 = get_charter_by_id(id2)


print(id1, personaje1)
print(id2,personaje2)



sw_data= get_charter_by_id

    

