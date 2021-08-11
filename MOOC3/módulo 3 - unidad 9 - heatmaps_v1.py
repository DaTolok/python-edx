import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

df1 = pd.read_csv('Datasets/2010YumaAZ.csv')
df2 = pd.read_csv('Datasets/2010SitkaAK.csv')
df3 = pd.read_csv('Datasets/2010SantaBarbaraCA.csv')

data = [go.Heatmap(x=df1['DAY'],
                   y=df1['LST_TIME'],
                   z=df1['T_HR_AVG'].values.tolist())]

layout = go.Layout(title='Yuma:Temperatura promedio por días y horas')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='heatmaps.html')