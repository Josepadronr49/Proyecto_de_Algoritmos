import requests as rq
from Funciones import cargar_API,cargar_informacion
from Especies import Especies
especies_obj=[]


db_especies=cargar_informacion('https://swapi.dev/api/species/?format=json')
#print(cargar_API(None))
#print(db_especies)

for especies in db_especies:
    for especie in especies:
        lista_personajes=[]
        for personaje in especie["people"]:
            cada_personaje=cargar_API(personaje)
            lista_personajes.append(cada_personaje["name"])     
        especies_obj.append(Especies(especie['name'],especie['average_height'],especie['classification'],"planeta",especie['language'],lista_personajes,'pelicula')) #hay que arreglar lista de personas y pelicula
    
for clase_planeta in especies_obj:
    clase_planeta.mostrar_especies()
