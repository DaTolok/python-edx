import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json

df = pd.read_csv('Datasets/wheels.csv')

app = dash.Dash()

app.layout = html.Div([html.Div([dcc.Graph(id='color-wheels',
                                           figure={'data':[go.Scatter(x=df['color'],
                                                                      y=df['wheels'],
                                                                      dy=1,
                                                                      mode='markers',
                                                                      marker={'size':12,
                                                                              'color':'rgb(254, 89, 0)',
                                                                              'line':{'width': 2}})],
                                                   'layout':go.Layout(title='Wheels & Colors Scatterplot',
                                                                      xaxis={'title':'Color'},
                                                                      yaxis={'title':'# of Wheels',
                                                                             'nticks':3},
                                                                      hovermode='closest')})],
                                style={'width':'30%',
                                       'float':'left'}),
                       html.Div([html.Pre(id='selected-data',
                                          style={'paddingTop':35})],
                                style={'width':'30%',
                                       'display':'inline-block',
                                       'verticalAlign':'top'}),
                       html.Div([html.Pre(id='rectangle-area',
                                          style={'paddingTop': 35})],
                                style={'width': '30%',
                                       'display': 'inline-block',
                                       'verticalAlign': 'top'})])

@app.callback(Output('selected-data', 'children'),
              Output('rectangle-area', 'children'),
              [Input('color-wheels', 'selectedData')])
def get_hoverinfo(selectecData):
    b=selectecData['range']['x'][1] - selectecData['range']['x'][0]
    h=selectecData['range']['y'][1] - selectecData['range']['y'][0]
    return json.dumps(selectecData, indent=2), 'El área del rectángulo seleccionado es: '+str(b*h)

if __name__ == '__main__':
    app.run_server()
