from Personaje import Personaje
import requests 
def initial_data_base(link):
    resp=requests.get(link)
    return resp.json()

personaje_obj=[]

def buscar_personaje():
    db_personaje=initial_data_base("https://www.swapi.tech/api/people?page=2&limit=10000")
    personajes=db_personaje["results"]
    for personaje in personajes:
        caracteristicas_personajes=personaje["url"]
        caracteristicas_personajes_db=initial_data_base(caracteristicas_personajes)
        caracteristicas=caracteristicas_personajes_db["results"]
        personaje_obj.append(Personaje(caracteristicas["name"],initial_data_base(caracteristicas["url"])["properties"]["name"],"titulo episodio",caracteristicas["gender"],"especie","nave","vehiculos"))
        buscar_personaje=input("Ingrese el nombre del personaje que desee buscar: ")
        #print(personaje_caracteristicas_db)
        #print(personaje_caracteristica)
        #personaje_caracteristica=initial_data_base("https://www.swapi.tech/api/people/uid")
        #print(personaje_caracteristica)
        #personaje_obj.append(Personaje(personaje_caracteristica["name"],personaje_caracteristica["name"],personaje_caracteristica["name"],personaje_caracteristica["name"],personaje_caracteristica["name"],personaje_caracteristica["name"],personaje_caracteristica["name"]))
        
buscar_personaje()