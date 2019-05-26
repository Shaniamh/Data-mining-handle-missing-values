import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data_ruspini = pd.read_csv("data_ruspini_missing.csv")
data_ruspini.columns = ["x", "y", "label"]
print(data_ruspini)
data = data_ruspini.replace("?", np.nan)
data = pd.DataFrame(data)
data['x'] = pd.to_numeric(data_ruspini['x'], errors='coerce') 
data['y'] = pd.to_numeric(data_ruspini['y'], errors='coerce') 

#mencari mean
mean = data.groupby("label").mean()
mean = mean.round(1)
print(mean)

data['x'] = data['x'].fillna(data.groupby(['label'])['x'].transform('mean'))
data['y'] = data['y'].fillna(data.groupby(['label'])['y'].transform('mean'))

data['x'] = data['x'].round(1) 
data['y'] = data['y'].round(1)
print(data)
np.savetxt("new_ruspini.csv", data, delimiter=",", fmt="%7.3f")
plt.scatter(
    x = "x",
    y = "y",
    data = data
)
plt.show()
