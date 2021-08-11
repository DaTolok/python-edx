import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('Datasets/mpg.csv')
features = df.columns

app = dash.Dash()

app.layout = html.Div([html.Div([dcc.Dropdown(id='features',
                                              options=[{'label':col,
                                                        'value':col}
                                                       for col in features],
                                              value='mpg')]),
                       html.Div(id='stats'),
                       dcc.Graph(id='histogram')],
                      style={'padding':10})

@app.callback(Output(component_id='stats',
                     component_property='children'),
              Output(component_id='histogram',
                     component_property='figure'),
              [Input(component_id='features',
                     component_property='value')])
def update_outputs(feature):
    stats = 'La moda de la variable '+str(feature)+' es '+str(df[feature].mode()[0])
    fig = {'data':[go.Histogram(x=df[feature])],
           'layout':go.Layout(title='Histograma de la variable '+str(feature))}
    return stats, fig

if __name__ == '__main__':
    app.run_server()
