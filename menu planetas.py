from Planetas import Planetas 
from Funciones import cargar_API,cargar_informacion
planetas_obj=[]

db_planetas=cargar_informacion('https://swapi.dev/api/planets/?format=json') #Recorrer toda la base de datos del api y devolverlo como un json
for planetas in db_planetas:
    for planeta in planetas:
        lista_episodios=[]
        for episodio in planeta["films"]: #Recorre la lista de las peliculas
            cada_episodio=cargar_API(episodio)
            lista_episodios.append(cada_episodio["title"]) #Busca los nombre de cada pelicula
        personajes_en_episodio=[]
        for personaje in planeta['residents']: #Recorre la lista de los personajes del planeta
            cada_personaje=cargar_API(personaje)
            personajes_en_episodio.append(cada_personaje['name']) #Les encuentra los nombre de cada personaje del planeta
        planetas_obj.append(Planetas(planeta['name'],planeta['orbital_period'],planeta['rotation_period'],planeta['population'],planeta['climate'],lista_episodios,personajes_en_episodio)) #Se convirtio a un objeto clase Planeta

for clase_planeta in planetas_obj:
    clase_planeta.mostrar_planeta()