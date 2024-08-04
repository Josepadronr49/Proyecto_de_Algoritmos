import requests as rq
def cargar_API(link):
    informacion=rq.get(link).json()
    return informacion