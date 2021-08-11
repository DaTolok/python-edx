import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('Datasets/2018WinterOlympics.csv')

trace1 = go.Bar(x=df['NOC'],
                y=df['Gold'],
                name='Oro',
                marker={'color':'#FFD700'})

trace2 = go.Bar(x=df['NOC'],
                y=df['Silver'],
                name='Plata',
                marker={'color':'#9EA0A1'})

trace3 = go.Bar(x=df['NOC'],
                y=df['Bronze'],
                name='Bronce',
                marker={'color':'#CD7F32'})

data = [trace1, trace2, trace3]
layout = go.Layout(title='Medallas por país')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bar_chart.html')