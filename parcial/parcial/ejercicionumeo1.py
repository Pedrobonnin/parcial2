from random import randint
from consumo_api import altura
from consumo_api import get_charter_by_id
from consumo_api import peso



id1 = randint(1,83)
id2 = randint(1,83)

personaje1 = get_charter_by_id(id1)
personaje2 = get_charter_by_id(id2)


print(id1, personaje1)
print(id2,personaje2)




if (altura(personaje1) < altura(personaje2)) :
   print ("El mas alto es",personaje1["name"],"su altura es", altura(personaje1))

else:
    print ("El mas alto es",personaje2["name"],"su altura es", altura(personaje2))


if (peso(personaje1)) > (peso(personaje2)):

   print ("El personaje mas pesado es",personaje1["name"],"el peso es", altura(personaje1))

else:
    print ("El personaje mas pesado es",personaje2["name"],"el peso es", altura(personaje2))

print(personaje1["name"])
catidad_de_peliculas1 = len(personaje1["films"])
print(len(personaje1["films"]))

print(personaje2["name"])
catidad_de_peliculas2 = len(personaje1["films"])
print(len(personaje2["films"]))
if(catidad_de_peliculas1 > catidad_de_peliculas2):
    print("Personaje numero 1 participo en mas peliclas " )
else:
    print("Personaje numero 2 participo en mas peliclas " )




if (personaje1 == "Yoda" or personaje1 == "Grievous" or  personaje1 == "Grievous" or personaje2 == "Yoda" or  personaje2 == "Grievous"):
    print("esta en la lista")
    



   