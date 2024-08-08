import requests as rq
def cargar_API(link):
    informacion=rq.get(link).json()
    return informacion


def cargar_informacion(link,lista_de_informacion):
    lista_de_informacion=[]
    pagina_actual=cargar_API(link)
    while pagina_actual["next"]!=None:
        lista_de_informacion.append(pagina_actual["results"])
        pagina_actual=cargar_API(pagina_actual["next"])
    else:
        lista_de_informacion.append(pagina_actual["results"])
        
        