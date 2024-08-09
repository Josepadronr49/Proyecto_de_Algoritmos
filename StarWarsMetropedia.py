from Funciones import cargar_API, cargar_informacion
from Pelicula import Pelicula
from Especies import Especies
from Planetas import Planetas
from Personaje import Personaje

#Se crea una clase en la que va a estar el código del menú del programa
class StarWarsMetropedia:
    #Se crean listas en las que estarán los datos covertidos en objetos
    pelicula_obj=[]
    especies_obj=[]
    planetas_obj=[]
    personaje_obj=[]

    #Se crea una función que iniciará el programa con todas las opciones requeridas
    def start(self):
        self.convertir_peliculas()
        #Función de especies
        #Función de planetas
        #self.convertir_personajes()
        
        print("¡Sea bienvenido a la Metropedia de Star Wars!")
        while True:
            menu=input("""
Ingrese una opción: 
1- Lista de películas
2- Lista de especies de seres vivos de la saga 
3- Lista de planetas
4- Buscar personaje
5- Ver gráfico de cantidad de personajes nacidos en cada planeta 
6- Naves
7- Misiones
8- Volver al menú
9-Salir
--->""")
            if menu=="1":
                self.mostrar_lista_peliculas()

            elif menu=="2":
            self.mostrar_especies()

            elif menu=="3":
                self.mostrar_planetas()

            elif menu=="4":
                None #self.buscar_personaje()

            elif menu=="5":
                None

            elif menu=="6":
                None

            elif menu=="7":
                None

            elif menu=="8":
                continue

            elif menu=="9":
                break
        print("¡Hasta luego! \n¡Que la fuerza te acompañe!")


#Se crean todas las funciones que ejecutarán las acciones de cada opción del menú
#Se crea una función para convertir las peliculas en objetos
    def convertir_peliculas(self):
        db_peliculas=cargar_API("https://www.swapi.tech/api/films")
        peliculas=db_peliculas["result"]
        for pelicula in peliculas:
            pelicula_propiedades=pelicula["properties"]
            self.pelicula_obj.append(Pelicula(pelicula_propiedades["title"],pelicula_propiedades["episode_id"],pelicula_propiedades["release_date"],pelicula_propiedades["opening_crawl"],pelicula_propiedades["director"]))

#Se crea una función que permita mostrar las películas en la primera opción del menú            
    def mostrar_lista_peliculas(self): 
        #Se ordena la lista por número de episodio y se usa una función para mostrar la lista de películas
        lista_ordenada=sorted(self.pelicula_obj, key=lambda x: x.numero_episodio)
        for peli in lista_ordenada:
            peli.mostrar_pelicula()

    def convertir_personajes(self):
        #Se utiliza la función para guardar en una lista toda la información de los personajes
        db_personajes=cargar_informacion("https://swapi.dev/api/people/?format=json")  
        #Recorremos la lista dentro de la lista
        for personajes in db_personajes:
            for personaje in personajes:
                #Se realizan varios "for" para acceder a información de los personajes que dentro tiene listas y se debe acceder a un link
                lista_peliculas=[]
                for pelicula in personaje["films"]:
                    cada_pelicula=cargar_API(pelicula)
                    lista_peliculas.append(cada_pelicula["title"])
                lista_especies=[]
                for especie in personaje["species"]:
                    cada_especie=cargar_API(especie)
                    lista_especies.append(cada_especie["name"])
                lista_naves=[]
                for nave in personaje["starships"]:
                    cada_nave=cargar_API(nave)
                    lista_naves.append(cada_nave)
                lista_vehiculos=[]
                for vehiculo in personaje["vehicles"]:
                    cada_vehiculo=cargar_API(vehiculo)
                    lista_vehiculos.append(cada_vehiculo["name"])
            self.personaje_obj.append(Personaje(personaje["name"],cargar_API(personaje["homeworld"])["name"],lista_peliculas,personaje["gender"],lista_especies,lista_naves,lista_vehiculos))

    def buscar_personaje(self):
        personaje_buscar=input("Ingrese el nombre del personaje que desee buscar: ")
        for personaje in self.personaje_obj:
            if personaje_buscar in personaje.nombre:
                personaje.mostrar_personaje()
    def mostrar_especies(self):
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
                self.especies_obj.append(Especies(especie['name'],especie['average_height'],especie['classification'],cargar_API(especie["homeworld"])['name'],especie['language'],lista_personajes,lista_peliculas)) #Conversion de los objetos a clase Especie
        for clase_planeta in self.especies_obj:
            clase_planeta.mostrar_especies()
    
    def mostrar_planetas(self):
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
                self.planetas_obj.append(Planetas(planeta['name'],planeta['orbital_period'],planeta['rotation_period'],planeta['population'],planeta['climate'],lista_episodios,personajes_en_episodio)) #Se convirtio a un objeto clase Planeta
        for clase_planeta in self.planetas_obj:
            clase_planeta.mostrar_planeta() 


