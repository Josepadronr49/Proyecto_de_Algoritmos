import pandas as pd
planetas=[]
planeta_archivos=pd.read_csv("csv/characters.csv")
planetas.append(planeta_archivos["name"])
print(f"Lista de planetas a seleccionar:\n{planetas}") #Se muestra al usuario la lista de planetas que puede elegir para su misión


planeta_de_la_mision=[]

print(planetas)

while len(planeta_de_la_mision)< 1:
    planeta_destino_mision=(input("Ingrese el nombre del planeta destino de la misión: "))
    if planeta_destino_mision.isnumeric() and int(planeta_destino_mision) < 60:
        for elemento in planetas:
            planeta_de_la_mision.append(elemento[int(planeta_destino_mision)])
    else:
        print("Ingrese un índice válido")
        
    #for planeta in elemento:
        #print(planeta)
print(planeta_de_la_mision)


"""if planeta_destino_mision:
            planeta_de_la_mision.append(planetas[planeta_destino_mision])
        else:
            break
                
print(planeta_de_la_mision)"""
