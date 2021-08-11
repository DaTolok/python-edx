import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

df = pd.read_csv('Datasets/iris.csv')

data = [go.Box(y=df[df['class'] == flor]['sepal_length'],
               name=flor,
               boxpoints='all')
        for flor in df['class'].unique()]

layout = go.Layout(title='Gráficas de caja: Longitud de sépalo',
                   xaxis=dict(title='Tipo de flor'))
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='box_plot.html')