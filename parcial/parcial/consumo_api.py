import json
import requests

def ordenar_nombre(peronaje):
    return peronaje['name']

def altura(item):
    # print(item, type(item))
    if(item['height'].isdecimal()):
        return int(item['height'])
    else:
        return -1

def peso(item):
    if(item['mass'].isdecimal()):
        return float(item['mass'])
    else:
        return -1

def color_pelo(item):
    return item['hair_color'] + item['name']

def consumo_api(id):
    respuesta = requests.get('https://swapi.dev/api/people/'+str(id))
    if respuesta.status_code == 200:
        dic = json.loads(respuesta.text)
        return dic


# personaje = consumo_api(2)

# print(personaje['name'],personaje['species'])
# del personaje['episode']
# personaje.pop('episode')
# for clave in personaje.keys():
#     if(clave == 'episode'):
#         print(clave)
#         for episode in personaje[clave]:
#             print(episode)
#     else:
#         print(clave, personaje[clave])



def get_docs(ruta):
    req = requests.get(ruta)
    # Imprimimos el resultado si el código de estado HTTP es 200 (OK):
    if req.status_code == 200:
        dic = json.loads(req.text)
        return dic


def get_charter_by_id(id):
    data = get_docs("https://swapi.dev/api/people/"+str(id))
    return data


def search_characters_by_name(name):
    data = get_docs("https://swapi.dev/api/people?search="+str(name))
    return data['results']


