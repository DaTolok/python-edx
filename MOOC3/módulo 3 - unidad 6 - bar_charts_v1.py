import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('Datasets/2018WinterOlympics.csv')
#print(df.head())
data = [go.Bar(x=df['NOC'],
                y=df['Total'])]
layout = go.Layout(title='Medallas por país')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bar_chart.html')