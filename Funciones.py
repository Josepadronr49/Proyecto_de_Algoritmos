import requests as rq
def cargar_API(link):
    if link==None: #Solucion a los links vacios del api, para que devuelva un diccionario iterable.
        informacion={'name':'Desconocido','title':'Desconocido'}
    else:informacion=rq.get(link).json()
    return informacion


def cargar_informacion(link):
    lista_de_informacion=[]
    pagina_actual=cargar_API(link)
    while pagina_actual["next"]!=None:
        lista_de_informacion.append(pagina_actual["results"])
        pagina_actual=cargar_API(pagina_actual["next"])
    else:
        lista_de_informacion.append(pagina_actual["results"])
    return lista_de_informacion
        
        