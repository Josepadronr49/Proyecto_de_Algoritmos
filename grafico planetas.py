
import pandas as pd
import matplotlib.pyplot as plt

db_archivo_planeta = pd.read_csv('csv/planets.csv')

db_archivo_planeta["residents"]=db_archivo_planeta["residents"].fillna("")
db_archivo_planeta["residents"]=db_archivo_planeta["residents"].apply(lambda x: len(x.split(",")) if x else 0)
print(db_archivo_planeta[["name","residents"]].head())

plt.figure(figsize=(12,8))
plt.bar(db_archivo_planeta["name"],db_archivo_planeta["name"],color="deeppink")
plt.title("Cantidad de personajes nacidos en cada planeta")
plt.xlable("Planetas")
plt.ylable("Cantidad de personajes nacidos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

