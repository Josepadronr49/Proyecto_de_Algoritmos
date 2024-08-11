import pandas as pd
import matplotlib.pyplot as ptl

db_naves=pd.read_csv('csv/starships.csv',sep=",")


db_naves['hyperdrive_rating']=pd.to_numeric(db_naves['hyperdrive_rating'],errors='coerce')
db_naves['MGLT']=pd.to_numeric(db_naves['MGLT'],errors='coerce')
db_naves['max_atmosphering_speed']=pd.to_numeric(db_naves['max_atmosphering_speed'],errors='coerce')
db_naves['cost_in_credits']=pd.to_numeric(db_naves['cost_in_credits'],errors='coerce')

agrupado_por_clase=db_naves.groupby('starship_class')

print(f'Estadística de los costos\n{agrupado_por_clase['cost_in_credits'].describe()} \nmoda: \n{db_naves['cost_in_credits'].mode()}')
print()
print(f'Estadística de los hyperpropulsores\n{agrupado_por_clase['hyperdrive_rating'].describe()}\nmoda:\n{db_naves["hyperdrive_rating"].mode()}')
print()
print(f'Estadística de la máxima velocidad atmosférica\n{agrupado_por_clase['max_atmosphering_speed'].describe()}\nmoda:\n{db_naves['max_atmosphering_speed']}')
print()
print(f'Estadística de MGLT por clase\n{agrupado_por_clase['MGLT'].describe()}\nmoda:\n{db_naves['MGLT']}')
print()