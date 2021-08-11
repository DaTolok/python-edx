import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)
x_values = np.linspace(0, 1, 100)
y_values = np.random.randn(100)

#Calcular el promedio de los valores de y_values
y_avg = #Completar1

#Calcular el valor máximo de y_values
y_max = #Completar2

#Calcular el valor x_y_max tal que (x_y_max, y_max) sea el punto máximo de la gráfica de línea
x_y_max = #Completar3

trace1 = go.Scatter(x=x_values,
                    y=y_values,
                    name='Datos',
                    mode='lines')

#Definir los parámetros x e y de modo que:
#Se genere una línea punteada horizontal a la altura del promedio de y_values
trace2 = go.Scatter(x=#Completar4,
                    y=#Completar5,
                    name='Promedio',
                    mode='lines',
                    line={'dash':'dash'})

data = [trace1, trace2]
layout = go.Layout(title='Gráfica de línea')
fig = go.Figure(data=data, layout=layout)

#Definir los parámetros x e y de modo que esta anotación apunte al valor máximo de la línea
fig.add_annotation(x=#Completar6,
                   y=#Completar7,
                   text="En x = {:.2f} alcanzó su valor máximo de {:.2f}".format(#Completar6, Completar7),
                   showarrow=True,
                   arrowhead=5)

fig.add_annotation(axref='x',
                   ayref='y',
                   x=0.6,
                   y=#Completar8,
                   ax=0.5,
                   ay=-2,
                   text="El promedio de los valores es {:.2f}".format(#Completar8),
                   showarrow=True,
                   arrowhead=5)

pyo.plot(fig, filename='line_chart.html')