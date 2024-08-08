import requests
from Planetas import Planetas 
planetas_obj=[]
def initial_data_base(link):
    resp=requests.get(link)
    return resp.json()

dbplanetas=initial_data_base('https://www.swapi.tech/api/planets?page=2&limit=1000')
for planetas in dbplanetas['results']:
    planetas=initial_data_base(planetas['url'])
    lista_planeta=planetas['result']['properties']
    planetas_obj.append(Planetas(lista_planeta['name'],lista_planeta['orbital_period'],lista_planeta['rotation_period'],lista_planeta['population'],lista_planeta['climate'],'1','Georges'))
for clase_planeta in planetas_obj:
    clase_planeta.mostrar_planeta()