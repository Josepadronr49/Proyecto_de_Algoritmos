from Funciones import cargar_API
from Pelicula import Pelicula

#Se crea una clase en la que va a estar el código del menú del programa
class StarWarsMetropedia:
    pelicula_obj=[]

    def start(self):
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
                None

            elif menu=="3":
                None

            elif menu=="4":
                None

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
        print("¡Hasta luego!")


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

      