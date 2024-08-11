import pandas as pd
import matplotlib.pyplot as ptl

db_naves=pd.read_csv('csv/starships.csv',sep=",")

db_naves['hyperdrive_rating']=pd.to_numeric(db_naves['hyperdrive_rating'],errors='coerce')
db_naves['MGLT']=pd.to_numeric(db_naves['MGLT'],errors='coerce')
db_naves['max_atmosphering_speed']=pd.to_numeric(db_naves['max_atmosphering_speed'],errors='coerce')
db_naves['cost_in_credits']=pd.to_numeric(db_naves['cost_in_credits'],errors='coerce')

db_naves['cost_in_credits'].describe()