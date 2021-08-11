import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

df = pd.read_csv('Datasets/iris.csv')

trace1 = go.Box(y=df[df['class'] == 'Iris-setosa']['sepal_length'],
                name='Setosa')

trace2 = go.Box(y=df[df['class'] == 'Iris-versicolor']['sepal_length'],
                name='Versicolor')

trace3 = go.Box(y=df[df['class'] == 'Iris-virginica']['sepal_length'],
                name='Virginica')

data = [trace1, trace2, trace3]
layout = go.Layout(title='Gráficas de caja: Longitud de sépalo',
                   xaxis=dict(title='Tipo de flor'))
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='box_plot.html')