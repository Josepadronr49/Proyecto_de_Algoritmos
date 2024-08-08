from Funciones import cargar_API
from Especies import Especies
especies_obj=[]
dict_especies=cargar_API('https://www.swapi.tech/api/species?page=2&limit=10000')
for propiedades_especies in dict_especies['results']:
    propiedad=cargar_API(propiedades_especies['url'])
    dict_propiedades=propiedad['result']['properties']
    especies_obj.append(Especies(dict_propiedades['name'],dict_propiedades['average_height'],dict_propiedades['classification'],cargar_API(str(dict_propiedades['homeworld']))['result']['properties']['name'],dict_propiedades['language'],dict_propiedades['people'],'pelicula')) #hay que arreglar lista de personas y pelicula
    
for clase_planeta in especies_obj:
    clase_planeta.mostrar_especies()
