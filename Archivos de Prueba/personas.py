from Personaje import Personaje
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
        None





        


#Función tech
#db_personaje=initial_data_base("https://www.swapi.tech/api/people?page=2&limit=10000")
#personajes=db_personaje["results"]
#for personaje in personajes:
    #caracteristicas_personajes=personaje["url"]
    #caracteristicas_personajes_db=initial_data_base(caracteristicas_personajes)
    #caracteristicas=caracteristicas_personajes_db["results"]
    #personaje_obj.append(Personaje(caracteristicas["name"],initial_data_base(caracteristicas["url"])["properties"]["name"],"titulo episodio",caracteristicas["gender"],"especie","nave","vehiculos"))
#buscar_personaje=input("Ingrese el nombre del personaje que desee buscar: ")