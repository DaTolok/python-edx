import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

df = pd.read_csv('Datasets/iris.csv')

data = [go.Box(y=df['sepal_length'])]

pyo.plot(data, filename='box_plot.html')