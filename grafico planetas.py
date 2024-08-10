
import pandas as pd
import matplotlib.pyplot as plt

#Se accede al archivo utilizando la librería pandas
db_archivo_planeta = pd.read_csv("csv/planets.csv")

db_archivo_planeta["residents"]=db_archivo_planeta["residents"].fillna("") #Reemplaza el NaN por cadena vacía
db_archivo_planeta["residents"]=db_archivo_planeta["residents"].apply(lambda x: len(x.split(",")) if x else 0) #Cuenta a los residentes
print(db_archivo_planeta[["name","residents"]].head()) #Se verifican los datos

#Con las funciones de la librería marplotlib se puede crear un gráfico 
#Se escoge un gráfico de barras para que la comparación sea más cómoda a nivel visual 
plt.figure(figsize=(12,8))
plt.bar(db_archivo_planeta["name"],db_archivo_planeta["residents"],color=["deeppink","hotpink","fuchsia","violet"])
plt.title("Cantidad de personajes nacidos en cada planeta") #Se escoge el título del gráfico
plt.xlabel("Planetas") #Leyenda del eje "x"
plt.ylabel("Cantidad de personajes nacidos") #Leyenda del eje "y"
plt.xticks(rotation=45)
plt.tight_layout()  
plt.show()  #Se muestra el gráfico

