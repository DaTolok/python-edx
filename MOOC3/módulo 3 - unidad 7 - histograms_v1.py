import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

df = pd.read_csv('Datasets/mpg.csv')

data = [go.Histogram(x=df['mpg'])]

layout = go.Layout(title='Histograma')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='histogram.html')