import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
from plotly import subplots

df1 = pd.read_csv('Datasets/2010YumaAZ.csv')
df2 = pd.read_csv('Datasets/2010SitkaAK.csv')
df3 = pd.read_csv('Datasets/2010SantaBarbaraCA.csv')

trace1 = go.Heatmap(x=df1['DAY'],
                    y=df1['LST_TIME'],
                    z=df1['T_HR_AVG'].values.tolist(),
                    colorscale='Jet',
                    zmin=0,
                    zmax=45)

trace2 = go.Heatmap(x=df2['DAY'],
                    y=df2['LST_TIME'],
                    z=df2['T_HR_AVG'].values.tolist(),
                    colorscale='Jet',
                    zmin=0,
                    zmax=45)

trace3 = go.Heatmap(x=df3['DAY'],
                    y=df3['LST_TIME'],
                    z=df3['T_HR_AVG'].values.tolist(),
                    colorscale='Jet',
                    zmin=0,
                    zmax=45)

fig = subplots.make_subplots(rows=1,
                             cols=3,
                             subplot_titles=['Yuma', 'Sitka', 'Santa Barbara'],
                             shared_yaxes=True)

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)
fig.append_trace(trace3, 1, 3)

fig.update_layout(title='Mapa de calor de tres ciudades',
                  title_x=0.5)

pyo.plot(fig,filename='heatmaps.html')