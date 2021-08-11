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

data = [trace0]
layout = go.Layout(title='Gráfica de línea')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatter.html')