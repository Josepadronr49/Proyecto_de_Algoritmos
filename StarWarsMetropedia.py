from Funciones import cargar_API, cargar_informacion
from Pelicula import Pelicula
from Especies import Especies
from Planetas import Planetas
from Personaje import Personaje
from Mision import Mision
import pandas as pd
import matplotlib.pyplot as ptl
import json
import numpy as np

#Se crea una clase en la que va a estar el código del menú del programa
class StarWarsMetropedia:
    #Se crean listas en las que estarán los datos covertidos en objetos
    pelicula_obj=[]
    especies_obj=[]
    planetas_obj=[]
    personaje_obj=[]
    mision_obj=[]

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
                self.opciones_nave() #La sexta opcion mostrará un sub-menú que permitirá que el usuario vea la estadistica o los graficos de la informacion de las naves 

            elif menu=="7":
                self.opciones_mision() #La séptima opción mostrará un sub-menú que permitirá que el usuario cree sus misiones, las modifique, guarde, visualice y las cargue

            elif menu=="8":
                print("¡Hasta luego! \n¡Que la fuerza te acompañe!") #Con esta opción el usuario podrá salir del programa
                break

            else:
                print("Opción no válida. Por favor, vuelva a intentarlo.") #Se coloca esta opción en caso de que algún usuario coloque una opción incorrecta en su selección
            


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
                    lista_naves.append(cada_nave["name"])
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
                    if personaje_buscar.lower() in personaje.nombre.lower(): #Se buscan los caracteres en los nombres de los personajes para buscar coincidencias
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
            option = input("1- Longitud de nave\n2- Capacidad de carga\n3- Clasificación de hiperimpulsor\n4- MGLT\n5- Salir\n--->")
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
        db_naves=pd.read_csv('csv/starships.csv',sep=",") #Extraer la informacion de la base de datos, indicando que se separa con una , los datos

        #Transformar los datos a numeros de las columnas relevantes, y si hay valores en blanco indicarlo para que no influya en el analisis de datos:
        db_naves['hyperdrive_rating']=pd.to_numeric(db_naves['hyperdrive_rating'],errors='coerce') 
        db_naves['MGLT']=pd.to_numeric(db_naves['MGLT'],errors='coerce')
        db_naves['max_atmosphering_speed']=pd.to_numeric(db_naves['max_atmosphering_speed'],errors='coerce')
        db_naves['cost_in_credits']=pd.to_numeric(db_naves['cost_in_credits'],errors='coerce')
        
        agrupado_por_clase=db_naves.groupby('starship_class') #Agrupar los datos por su clase de nave
        #Realizar una matriz alterable para cada una de las columnas a analizar de la base de datos:
        stats_hyperdrive=pd.DataFrame()
        stats_costos=pd.DataFrame()
        stats_MGLT=pd.DataFrame()
        stats_max=pd.DataFrame()
        #Se repite el procedimiento de la primera columna en todas las demas
        stats_hyperdrive=agrupado_por_clase['hyperdrive_rating'].describe() #La base de la matriz es una estadistica descriptiva dada por .describe()
        stats_hyperdrive['moda'] = agrupado_por_clase['hyperdrive_rating'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan) #Anexar una columna que muestra la moda por cada clase de nave, empleando .agg, con lambda se consigue identificar que se busca la moda, iloc hace que se escoja el primero si hay varias modas. Sino devuelve NaN
        print(f'Las estadisticas de hiperdrive:\n{stats_hyperdrive}') #imprime la matriz
        print() #espaciado para mayor legibilidad
        stats_costos=agrupado_por_clase['cost_in_credits'].describe()
        stats_costos['moda'] = agrupado_por_clase['cost_in_credits'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan)
        print(f'Estadística de los costos:\n{stats_costos}')
        print()
        stats_MGLT=agrupado_por_clase['MGLT'].describe()
        stats_MGLT['moda'] = agrupado_por_clase['MGLT'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan)
        print(f'Estadística de MGLT:\n{stats_MGLT}')
        print()
        stats_max=agrupado_por_clase['max_atmosphering_speed'].describe()
        stats_max['moda'] = agrupado_por_clase['max_atmosphering_speed'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan)
        print(f'Estadistica de Velocidad maxima en la atmósfera:\n{stats_max}')
        print()
    
    def opciones_nave(self):
        while True:
            mini_menu=input('Ingrese la opción de su preferencia:\n1-Mostrar gráficos de las características de las naves\n2-Estadística sobre las naves\n3-Salir\n-->')
            if mini_menu=='1':
                self.crear_grafico_comparacion_caracteristicas_naves()
            elif mini_menu=='2':
                self.crear_estadisticas_naves() 
            elif mini_menu=='3':
                break
            else: print('Ingrese una opción válida')

#Se crea una función para poder mostrar en un sub-menú lo que se puede hacer con las misiones
    def opciones_mision(self):
        while True:
            sub_menu=input("""
Ingrese la opción que desee: 
1- Crea tus misiones
2- Modificar misiones
3- Visualiza tus misiones
4- Guarda tus misiones
5- Carga tus misiones
6- Salir                          
--->""")
            if sub_menu=="1":
                self.crear_misiones()
            if sub_menu=="2":
                self.modificar_misiones()
            if sub_menu=="3":
                self.visualizar_misiones()
            if sub_menu=="4":
                archivo=input('Ingrese el nombre del archivo que desea cargar: ')
                self.guardar_misiones(archivo)
            if sub_menu=="5":
                archivo=input("Ingrese el nombre del archivo que desea cargar: ")
                self.cargar_misiones(archivo)
            if sub_menu=="6":
                break
            else:
                print("Ingrese una opción válida")
    
    def crear_misiones(self):
        if len(self.mision_obj)< 5: #Se coloca el límite de hasta 5 misiones
            nombre_de_la_mision=input("Ingrese el nombre de la misión: ") #El usuario ingresa el nombre de su misión
            planetas=[]
            planeta_archivos=pd.read_csv("csv/planets.csv")
            planetas.append(planeta_archivos["name"])
            print(f"Lista de planetas a seleccionar:\n{planetas}") #Se muestra al usuario la lista de planetas que puede elegir para su misión
            planeta_de_la_mision=[]
            while len(planeta_de_la_mision)< 1:
                planeta_destino_mision=input("Ingrese el índice del planeta destino de la misión: ")
                if planeta_destino_mision.isnumeric() and int(planeta_destino_mision) < 13:
                    for elemento in planetas:
                        planeta_de_la_mision.append(elemento[int(planeta_destino_mision)])
                else:
                    print("Ingrese un índice válido")
            nave=[]
            nave_archivos=pd.read_csv("csv/starships.csv")
            nave.append(nave_archivos["name"])
            print(f"Lista de naves a seleccionar:\n{nave}") #Se muestran al usuario la lista de naves a seleccionar
            nave_de_la_mision=[]
            while len(nave_de_la_mision)< 1:
                nave_mision=input("Ingrese el índice de la nave de la misión: ")
                if nave_mision.isnumeric() and int(nave_mision) < 60:
                    for elemento_nave in nave:
                        nave_de_la_mision.append(elemento_nave[int(nave_mision)])
                else:
                    print("Ingrese un índice válido")
            armas_mision=[]
            integrantes_mision=[]
            armas=[]
            armas_archivos=pd.read_csv("csv/weapons.csv")
            armas.append(armas_archivos["name"])
            print(f"Lista de armas a seleccionar:\n{armas}") #Se muestran al usuario la lista de armas que puede seleccionar
            while len(armas_mision)< 7: #Se coloca el límite para que seleccionen y agreguen hasta 7 armas
                arma=input("Ingrese el índice del arma que desee utilizar: ")
                if arma.isnumeric() and int(arma) < 60:
                    for elemento_arma in armas:
                        armas_mision.append(elemento_arma[int(arma)])
                    ocurrencia_armas=input("""
1-Agregar otra arma:
2-Continuar construyendo la misión: 
--->""")
                    if ocurrencia_armas=="1":
                        continue
                    elif ocurrencia_armas=="2":
                        break
                    else:
                        print("Ingrese una opción válida")
                else:
                    print("Ingrese un índice válido")
            integrantes=[]
            integrantes_archivos=pd.read_csv("csv/characters.csv")
            integrantes.append(integrantes_archivos["name"])
            print(f"Lista de integrantes a seleccionar:\n{integrantes}") #Se muestra la lista de los integrantes a seleccionar
            while len(integrantes_mision)< 7: #Se coloca un límite para que seleccionen y agreguen hasta 7 integrantes
                integrante=input("Ingrese los índices de los integrantes de su misión: ")
                if integrante.isnumeric() and int(integrante) < 96:
                    for elemento_integrante in integrantes:
                        integrantes_mision.append(elemento_integrante[int(integrante)])
                    ocurrencia=input("""
1-Agregar otro integrante:
2-Finalizar construcción de la misión: 
--->""")
                    if ocurrencia=="1":
                        continue
                    elif ocurrencia=="2":
                        break
                    else:
                        print("Ingrese una opción válida")
                else:
                    print("Ingrese un índice válido")
            self.mision_obj.append(Mision(nombre_de_la_mision,planeta_de_la_mision,nave_de_la_mision,armas_mision,integrantes_mision)) #Se guarda la misión como objeto
            print("¡Su misión ha sido creada con éxito!")
        else:
            print("Solo se pueden definir hasta 5 misiones")

    #Se crea una función que permita listar misiones para mostrar cuáles existen y así elegir una para modificarla
    def listar_misiones(self):
        if self.mision_obj:
            for i, mision in enumerate(self.mision_obj):
                print(f"{i}:{mision.nombre_mision}")
        else:
            print("No hay misiones definidas aún")

    #Se crea una función que permita modificar las misiones que ya existen
    def modificar_misiones(self):
        self.listar_misiones()
        seleccion=int(input("""
Seleccion el número de la misión que desee modificar 
--->"""))
        if 0 <= seleccion < len(self.mision_obj):
            mision_modificar=self.mision_obj[seleccion]
            print(f"Modificando mision: {mision_modificar.nombre_mision}")

            while True:
                elegir=input("""
Seleccione la característica de la misión que desee modificar:
1- Modificar nombre de la misión
2- Modificar planeta destino de la misión
3- Modificar la nave de la misión
4- Agregar arma
5- Eliminar arma
6- Agregar integrante
7- Eliminar integrante
8- Salir                           
--->""") 
                if elegir =="1":
                    mision_modificar.nombre_mision=input("Ingrese el nombre modificado de la misión: ")

                elif elegir =="2":
                    planetas=[]
                    planeta_archivos=pd.read_csv("csv/planets.csv")
                    planetas.append(planeta_archivos["name"])
                    print(f"Lista de planetas a seleccionar:\n{planetas}")
                    nuevo_planeta_de_la_mision=[]
                    while len(nuevo_planeta_de_la_mision)< 1:
                        nuevo_planeta_mision=input("Ingrese el índice del planeta de la misión: ")
                        if nuevo_planeta_mision.isnumeric() and int(nuevo_planeta_mision) < 60:
                            for elemento_planeta in planetas:
                                nuevo_planeta_de_la_mision.append(elemento_planeta[int(nuevo_planeta_de_la_mision)])
                        else:
                            print("Ingrese un índice válido")
                    mision_modificar.planeta_destino=nuevo_planeta_de_la_mision

                elif elegir =="3":
                    nave=[]
                    nave_archivos=pd.read_csv("csv/starships.csv")
                    nave.append(nave_archivos["name"])
                    print(f"Lista de naves a seleccionar:\n{nave}")
                    nueva_nave_de_la_mision=[]
                    while len(nueva_nave_de_la_mision)< 1:
                        nueva_nave_mision=input("Ingrese el índice de la nave de la misión: ")
                        if nueva_nave_mision.isnumeric() and int(nueva_nave_mision) < 60:
                            for elemento_nave in nave:
                                nueva_nave_de_la_mision.append(elemento_nave[int(nueva_nave_mision)])
                        else:
                            print("Ingrese un índice válido")
                    mision_modificar.nave=nueva_nave_de_la_mision

                elif elegir =="4":
                    armas=[]
                    armas_archivos=pd.read_csv("csv/weapons.csv")
                    armas.append(armas_archivos["name"])
                    print(f"Lista de armas a seleccionar:\n{armas}")
                    nueva_arma=input("Ingrese la nueva arma que desea agregar: ")
                    mision_modificar.agregar_arma(nueva_arma,self.mision_obj,armas)

                elif elegir =="5":
                    contador=0
                    for elemento in self.mision_obj:
                        print(f"{contador}--{elemento.armas}")
                        contador+=1
                    arma_eliminada=input("Ingrese el número del arma que desea eliminar: ")
                    mision_modificar.eliminar_arma(arma_eliminada,self.mision_obj)

                elif elegir =="6":
                    integrantes=[]
                    integrantes_archivos=pd.read_csv("csv/characters.csv")
                    integrantes.append(integrantes_archivos["name"])
                    print(f"Lista de integrantes a seleccionar:\n{integrantes}")
                    nuevo_integrante=input("Ingrese el nombre del integrante que desea eliminar: ")
                    mision_modificar.agregar_integrante(nuevo_integrante,self.mision_obj,integrantes)

                elif elegir =="7":
                    contador=0
                    for elemento in self.mision_obj:
                        print(f"{contador}--{elemento.integrantes}")
                        contador+=1
                    integrante_eliminado=input("Ingrese el nombre del integrante que desea eliminar: ")
                    mision_modificar.eliminar_integrante(integrante_eliminado, self.mision_obj)

                elif elegir =="8":
                    break

                else:
                    print("Ingrese una opción válida")
        
    #Se crea una función para agregar armas manteniendo el límite de hasta 7 armas
    """def agregar_arma(self,arma,lista): 
        for elemento in self.mision_obj:
            if len(elemento.armas) < 7:
                for elemento_arma in lista:
                        if arma.isnumeric() and int(arma) < 60:
                            elemento.armas.append(elemento_arma[int(arma)])
            else:
                print("No se pueden agregar más de 7 armas")"""
    
    #Se crea una función para eliminar armas
    """def eliminar_arma(self,arma):
        for elemento in self.mision_obj:
            if int(arma) in len(elemento.armas):
                elemento.armas.remove(elemento.armas[int(arma)])
        else:
            print("El arma que quiere eliminar no está en la lista")"""

    #Se crea una función para agregar integrantes manteniendo el límite de hasta 7 integrantes
    """def agregar_integrante(self,integrante,lista):
        for elemento in self.mision_obj:
            if len(elemento.integrantes) < 7:
                for elemento_integrante in lista:
                        if integrante.isnumeric() and int(integrante) < 96:
                            elemento.armas.append(elemento_integrante[int(integrante)])
        else:
            print("No se pueden agregar más de 7 integrantes")"""
    
    #Se crea una función para eliminar integrantes
    """def eliminar_integrante(self, integrante):
        for elemento in self.mision_obj:
            if int(integrante) in len(elemento.integrantes):
                elemento.integrantes.remove(elemento.integrantes[int(integrante)])
        else:
            print("El integrante que quiere eliminar no está en la lista")"""

    #Se crea una función para visualizar las misiones
    def visualizar_misiones(self):
        self.listar_misiones()
        indice = int(input("Seleccione el índice de la misión a visualizar: "))
        if 0 <= indice < len(self.mision_obj):
            print("\nDetalles de la misión:")
            print(self.mision_obj[indice].mostrar_mision())
        else:
            print("Índice de misión inválido.")

    #Se crea una función con la que se puede guardar las misiones
    def guardar_misiones(self,archivo):
        with open(archivo, 'w') as f:
            json.dump([m.__dict__ for m in self.mision_obj], f, indent=4)
        print("Misiones guardadas en", archivo)

    #Se crea una función para cargar las misiones
    def cargar_misiones(self,archivo):
        try:
            with open(archivo,"r") as info:
                informacion_misiones= json.load(info)
                self.mision_obj=[Mision(**m) for m in informacion_misiones]
            print(f"Sus misiones han sido cargadas desde el archivo: {archivo}")
        except FileNotFoundError: #Función de json por si el archivo no se encontró
            print("El archivo que desea cargar no se ha encontrado")
        except json.JSONDecodeError: #Por si hay errores la escritura del archivo
            print("Hay un error al leer el archivo")



    
            