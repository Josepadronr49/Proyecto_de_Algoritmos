#from Pelicula import Pelicula
import requests 
def initial_data_base(link):
    resp=requests.get(link)
    return resp.json()

pelicula_obj=[]

#def mostrar_lista_peliculas():
    #db_peliculas=initial_data_base("https://www.swapi.tech/api/films")
    #peliculas=db_peliculas["result"]
    #for pelicula in peliculas:
        #pelicula_propiedades=pelicula["properties"]
        #pelicula_obj.append(Pelicula(pelicula_propiedades["title"],pelicula_propiedades["episode_id"],pelicula_propiedades["release_date"],pelicula_propiedades["opening_crawl"],pelicula_propiedades["director"]))
    #for peli in pelicula_obj:
        #peli.mostrar_pelicula()

#mostrar_lista_peliculas()







