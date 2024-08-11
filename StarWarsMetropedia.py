from Funciones import cargar_API, cargar_informacion
from Pelicula import Pelicula
from Especies import Especies
from Planetas import Planetas
from Personaje import Personaje
import pandas as pd
import matplotlib.pyplot as ptl

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
        self.convertir_personajes()
        
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
8- Salir
--->""")
            if menu=="1":
                self.mostrar_lista_peliculas() #La primera función mostrará la lista de películas de la saga

            elif menu=="2":
                self.mostrar_especies() #La segunda opción mostrará la lista las especies de la saga

            elif menu=="3":
                self.mostrar_planetas() #La tercera opción mostrará la lista de planetas de la saga

            elif menu=="4":
                self.buscar_personaje() #La cuarta opción funcionará como un buscador de personajes

            elif menu=="5":
                self.crear_grafico_comparacion_personajes_planeta() #La quinta opción mostrará el gráfico para comparar personajes nacidos en cada planeta

            elif menu=="6":
                self.opciones_nave() #La sexta opcion mostrará un menu que permitirá que el usuario vea la estadistica o los graficos de la informacion de las naves 

            elif menu=="7":
                None

            elif menu=="8":
                break

            else:
                print("Opción no válida. Por favor, vuelva a intentarlo.")
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

#Se crea la función para convertir la información de la Api a objeto y guardarla como objeto en una lista
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
        #Para buscar a los personajes se crea un sub-menú
        while True:
            opcion=input(
"""Ingrese la opción que desee:
1-Buscar personaje
2-Salir
--->""")
            if opcion=="1": 
                personaje_buscar=input("Ingrese el nombre del personaje que desee buscar: ")
                contador=0
                for personaje in self.personaje_obj:
                    if personaje_buscar in personaje.nombre: #Se buscan los caracteres en los nombres de los personajes para buscar coincidencias
                        personaje.mostrar_personaje() #Si se encuentran coincidencia se muestran los personajes
                        contador+=1
                if contador==0:
                    print("No se encontraron resultados") #Si no hay coincidencias se muestra que el sistema no pudo encontrar resultados 
                    #Se podrá buscar personajes hasta que el usuario decida salir
            elif opcion=="2":
                break
            else:
                print("Ingrese una opción válida")
    
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

    #Se crea una función para poder hacer el gráfico que compare los personajes por planeta, obteniendo información de un archivo csv
    def crear_grafico_comparacion_personajes_planeta(self):
        #Se accede al archivo utilizando la librería pandas
        db_archivo_planeta= pd.read_csv("csv/planets.csv")
        db_archivo_planeta["residents"]=db_archivo_planeta["residents"].fillna("") #Reemplaza el NaN por una cadena vacía
        db_archivo_planeta["residents"]=db_archivo_planeta["residents"].apply(lambda x: len(x.split(",")) if x else 0) #Para contar a los personajes del planeta
        print(db_archivo_planeta[["name","residents"]].head()) #Para verificar los datos

        #Con las funciones de la librería matplotlib se puede crear un gráfico
        #Se escoge un gráfico de barras para que la comparación sea más cómoda a nivel visual
        ptl.figure(figsize=(12,8))
        ptl.bar(db_archivo_planeta["name"],db_archivo_planeta["residents"], color=["deeppink","hotpink","fuchsia","violet"])
        ptl.title("Cantidad de personajes nacidos en cada planeta") #Se escoge el título del gráfico
        ptl.xlabel("Planetas") #Leyenda del eje "x"
        ptl.ylabel("Cantidad de personajes nacidos") #Leyenda del eje "y"
        ptl.xticks(rotation=45)
        ptl.tight_layout()
        ptl.show()

    def crear_grafico_comparacion_caracteristicas_naves(self):
        #Se accede a la base de datos
        db_archivo_naves = pd.read_csv('csv/starships.csv')
        while True:
            option = input("1- Longitud de nave\n2- Capacidad de carga\n3- Clasificación de hiperimpulsor\n4- Clasificación de hiperimpulsor\n5- Salir\n--->")
            if option =="1":
            # Crear gráficos comparativos
             # 1. Longitud de la nave
                ptl.figure(figsize=(12, 6))
                ptl.bar(db_archivo_naves['name'], db_archivo_naves['length'], color='Blue')
                ptl.xlabel('Nave')
                ptl.ylabel('Longitud (m)')
                ptl.title('Longitud de las Naves Espaciales')
                ptl.xticks(rotation=90)
                ptl.tight_layout()
                ptl.show()
            elif option =="2":
                ptl.figure(figsize=(12, 6))
                ptl.bar(db_archivo_naves['name'], db_archivo_naves['cargo_capacity'], color=['Orange','Yellow','Red'])
                ptl.xlabel('Nave')
                ptl.ylabel('Capacidad de Carga (kg)')
                ptl.title('Capacidad de Carga de las Naves Espaciales')
                ptl.xticks(rotation=90)
                ptl.tight_layout()
                ptl.show()
            elif option =="3":
            # 3. Clasificación de hiperimpulsor
                ptl.figure(figsize=(12, 6))
                ptl.bar(db_archivo_naves['name'], db_archivo_naves['hyperdrive_rating'], color='coral')
                ptl.xlabel('Nave')
                ptl.ylabel('Clasificación de Hiperimpulsor')
                ptl.title('Clasificación de Hiperimpulsor de las Naves Espaciales')
                ptl.xticks(rotation=90)
                ptl.tight_layout()
                ptl.show()

            elif option =="4":
             # 4. MGLT (Modern Galactic Light Time)
                ptl.figure(figsize=(12, 6))
                ptl.bar(db_archivo_naves['name'], db_archivo_naves['MGLT'], color='purple')
                ptl.xlabel('Nave')
                ptl.ylabel('MGLT')
                ptl.title('MGLT de las Naves Espaciales')
                ptl.xticks(rotation=90)
                ptl.tight_layout()
                ptl.show()

            elif option =="5":
                print ()
                break
            else:  print("Ponga una opcion valida")          # Asegurar el funcionamiento del menu cuando se coloca opciones no validas.
    
    def crear_estadisticas_naves(self):
        db_naves=pd.read_csv('csv/starships.csv',sep=",")


        db_naves['hyperdrive_rating']=pd.to_numeric(db_naves['hyperdrive_rating'],errors='coerce')
        db_naves['MGLT']=pd.to_numeric(db_naves['MGLT'],errors='coerce')
        db_naves['max_atmosphering_speed']=pd.to_numeric(db_naves['max_atmosphering_speed'],errors='coerce')
        db_naves['cost_in_credits']=pd.to_numeric(db_naves['cost_in_credits'],errors='coerce')

        agrupado_por_clase=db_naves.groupby('starship_class')

        print(f'Estadística de los costos\n{agrupado_por_clase['cost_in_credits'].describe()} \nmoda: \n{db_naves['cost_in_credits'].mode()}')
        print()
        print(f'Estadística de los hyperpropulsores\n{agrupado_por_clase['hyperdrive_rating'].describe()}\nmoda:\n{db_naves["hyperdrive_rating"].mode()}')
        print()
        print(f'Estadística de la máxima velocidad atmosférica\n{agrupado_por_clase['max_atmosphering_speed'].describe()}\nmoda:\n{db_naves['max_atmosphering_speed']}')
        print()
        print(f'Estadística de MGLT por clase\n{agrupado_por_clase['MGLT'].describe()}\nmoda:\n{db_naves['MGLT']}')
        print()
    
    def opciones_nave(self):
        while True:
            mini_menu=input('Ingrese la opción de su preferencia:\n1-Mostrar gráficos de las características de las naves\n2-Estadística sobre las naves\n3-Salir')
            if mini_menu=='1':
                self.crear_grafico_comparacion_caracteristicas_naves()
            elif mini_menu=='2':
                self.crear_estadisticas_naves() 
            elif mini_menu=='3':
                break
            else: print('Ingrese una opción válida')
            