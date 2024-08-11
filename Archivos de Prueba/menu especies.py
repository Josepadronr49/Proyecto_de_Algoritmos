from Funciones import cargar_API,cargar_informacion
from Especies import Especies
especies_obj=[]


db_especies=cargar_informacion('https://swapi.dev/api/species/?format=json')


for especies in db_especies:
    for especie in especies:
        lista_personajes=[]
        lista_peliculas=[]
        for personaje in especie["people"]:
            cada_personaje=cargar_API(personaje)
            lista_personajes.append(cada_personaje["name"])
        for peliculas in especie['films']:
            cada_pelicula=cargar_API(peliculas)
            lista_peliculas.append(cada_pelicula['title'])      
        especies_obj.append(Especies(especie['name'],especie['average_height'],especie['classification'],cargar_API(especie["homeworld"])['name'],especie['language'],lista_personajes,lista_peliculas)) #Conversion de los objetos a clase Especie
for clase_planeta in especies_obj:
    clase_planeta.mostrar_especies()
