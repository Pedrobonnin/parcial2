import json
import requests

def consultar_personajes(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        diccionario = json.loads(respuesta.text)
        
        return diccionario
    else:
        print('nope')


urlbase = consultar_personajes('https://swapi.dev/api/people/')


sw_data = []

while(urlbase['next'] is not None):
    for doc in urlbase['results']:
        sw_data.append(doc)
    urlbase = consultar_personajes(urlbase['next'])


def nombre (item):
    '''sirve para ordenar por  altura '''
    return (item['name'])

sw_data.sort(key=nombre)

for index, character in enumerate(sw_data):
    
    print(character['name'],'su raza es: ', character['species'],'Su planeta de origen es :', character['homeworld'])



    
for character in sw_data:
    if(len(character['films'])== 6):
        print('El personaje',character['name'],'aparece en 6 peliculas')