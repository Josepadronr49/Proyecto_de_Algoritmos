#from Personaje import Personaje
import requests 
def initial_data_base(link):
    resp=requests.get(link)
    return resp.json()

personaje_obj=[]


def cargar_informacion(link):
    lista_de_informacion=[]
    pagina_actual=initial_data_base(link)
    while pagina_actual["next"]!=None:
        lista_de_informacion.append(pagina_actual["results"])
        pagina_actual=initial_data_base(pagina_actual["next"])
    else:
        lista_de_informacion.append(pagina_actual["results"])
    return lista_de_informacion
    

personaje_informacion=cargar_informacion("https://swapi.dev/api/people/?format=json")
for personajes in personaje_informacion:
    for personaje in personajes:
        lista_peliculas=[]
        for pelicula in personaje["films"]:
            cada_pelicula=initial_data_base(pelicula)
            lista_peliculas.append(cada_pelicula["title"])
        lista_especies=[]
        for especie in personaje["species"]:
            cada_especie=initial_data_base(especie)
            lista_especies.append(cada_especie["name"])
        lista_naves=[]
        for nave in personaje["starships"]:
            cada_nave=initial_data_base(nave)
            lista_naves.append(cada_nave["name"])
        lista_vehiculos=[]
        for vehiculo in personaje["vehicles"]:
            cada_vehiculo=initial_data_base(vehiculo)
            lista_vehiculos.append(cada_vehiculo["name"])
        personaje_obj.append("Personaje"(personaje["name"],initial_data_base(personaje["homeworld"])["name"],lista_peliculas,personaje["gender"],lista_especies,lista_naves,lista_vehiculos))

while True:
    opcion=input("""Igrese la opción que desee:
1-Buscar personaje
2-Salir
--->""")
    if opcion=="1":
        personaje_buscar=input("Ingrese el nombre del personaje que desee buscar: ")
        contador=0
        for personaje in personaje_obj:
            if personaje_buscar in personaje.nombre:
                personaje.mostrar_personaje()
                contador+=1
        if contador==0:
            print("No se encontraron resultados")
    elif opcion=="2":
        break
    else:
        print("Ingrese una opcion válida")




        


#Función tech
#db_personaje=initial_data_base("https://www.swapi.tech/api/people?page=2&limit=10000")
#personajes=db_personaje["results"]
#for personaje in personajes:
    #caracteristicas_personajes=personaje["url"]
    #caracteristicas_personajes_db=initial_data_base(caracteristicas_personajes)
    #caracteristicas=caracteristicas_personajes_db["results"]
    #personaje_obj.append(Personaje(caracteristicas["name"],initial_data_base(caracteristicas["url"])["properties"]["name"],"titulo episodio",caracteristicas["gender"],"especie","nave","vehiculos"))
#buscar_personaje=input("Ingrese el nombre del personaje que desee buscar: ")