from Personaje import Personaje
import requests 
def initial_data_base(link):
    resp=requests.get(link)
    return resp.json()

personaje_obj=[]

#def buscar_personaje
db_personaje=initial_data_base("https://www.swapi.tech/api/people?page=2&limit=10000")
personajes=db_personaje["results"]
