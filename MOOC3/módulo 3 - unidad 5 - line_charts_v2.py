import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)
x_values = np.linspace(0, 1, 100)
y_values = np.random.randn(100)

trace0 = go.Scatter(x=x_values,
                    y=y_values,
                    mode='lines',
                    name='lines')

trace1 = go.Scatter(x=x_values,
                    y=y_values+5,
                    mode='lines+markers',
                    name='lines+markers')

trace2 = go.Scatter(x=x_values,
                    y=y_values-5,
                    mode='markers',
                    name='markers')

data = [trace0, trace1, trace2]
layout = go.Layout(title='Gráfica de línea')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatter.html')