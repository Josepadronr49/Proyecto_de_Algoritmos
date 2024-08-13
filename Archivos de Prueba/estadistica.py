import pandas as pd
import numpy as np

db_naves=pd.read_csv('csv/starships.csv',sep=",")


db_naves['hyperdrive_rating']=pd.to_numeric(db_naves['hyperdrive_rating'],errors='coerce')
db_naves['MGLT']=pd.to_numeric(db_naves['MGLT'],errors='coerce')
db_naves['max_atmosphering_speed']=pd.to_numeric(db_naves['max_atmosphering_speed'],errors='coerce')
db_naves['cost_in_credits']=pd.to_numeric(db_naves['cost_in_credits'],errors='coerce')

agrupado_por_clase=db_naves.groupby('starship_class')
stats_hyperdrive=pd.DataFrame()
stats_costos=pd.DataFrame()
stats_MGLT=pd.DataFrame()
stats_max=pd.DataFrame()

stats_hyperdrive=agrupado_por_clase['hyperdrive_rating'].describe()
stats_hyperdrive['moda'] = agrupado_por_clase['hyperdrive_rating'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan)
print(f'Las estadisticas de hiperdrive:\n{stats_hyperdrive}')
print()
stats_costos=agrupado_por_clase['cost_in_credits'].describe()
stats_costos['moda'] = agrupado_por_clase['cost_in_credits'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan)
print(f'Estadística de los costos:\n{stats_costos}')
print()
stats_MGLT=agrupado_por_clase['MGLT'].describe()
stats_MGLT['moda'] = agrupado_por_clase['MGLT'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan)
print(f'Estadística de MGLT:\n{stats_MGLT}')
print()
stats_max=agrupado_por_clase['max_atmosphering_speed'].describe()
stats_max['moda'] = agrupado_por_clase['max_atmosphering_speed'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else np.nan)
print(f'Estadistica de Velocidad maxima en la atmosferica:\n{stats_max}')
print()

