import pandas as pd
import numpy as np


data_tiroid = pd.read_csv("data_tiroid_missing.csv")
data_tiroid.columns = ["a", "b", "c", "d", "e", "label"]
print(data_tiroid)
data = data_tiroid.replace("?", np.nan)
data = pd.DataFrame(data)
data['a'] = pd.to_numeric(data_tiroid['a'], errors='coerce') 
data['b'] = pd.to_numeric(data_tiroid['b'], errors='coerce') 
data['c'] = pd.to_numeric(data_tiroid['c'], errors='coerce') 
data['d'] = pd.to_numeric(data_tiroid['d'], errors='coerce') 
data['e'] = pd.to_numeric(data_tiroid['e'], errors='coerce') 

#mencari mean
mean = data.groupby("label").mean()
mean = mean.round(1)
print(mean)

data['a'] = data['a'].fillna(data.groupby(['label'])['a'].transform('mean'))
data['b'] = data['b'].fillna(data.groupby(['label'])['b'].transform('mean'))
data['c'] = data['c'].fillna(data.groupby(['label'])['c'].transform('mean'))
data['d'] = data['d'].fillna(data.groupby(['label'])['d'].transform('mean'))
data['e'] = data['e'].fillna(data.groupby(['label'])['e'].transform('mean'))

data['a'] = data['a'].round(1) 
data['b'] = data['b'].round(1)
data['c'] = data['c'].round(1)
data['d'] = data['d'].round(1)
data['e'] = data['e'].round(1)
np.savetxt("new_data_tiroid.csv",data, delimiter=",", fmt="%7.3f")
print(data)