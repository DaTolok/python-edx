import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

df = pd.read_csv('Datasets/iris.csv')

variables = #Completar1
marginals = #Completar2

app = dash.Dash()

app.layout = html.Div([html.Div([html.H1('Análisis del dataset iris.csv')],
                                style={'textAlign': 'center'}),
                       html.Div([html.H3('Configuración de parámetros de la gráfica')],
                                style={'marginLeft': '5%'}),
                       html.Div([html.Label('Selecciona la variable del eje X'),
                                 dcc.Dropdown(id='eje-x', options=#Completar3)],
                                style={'width': '20%',
                                       'marginRight': '3%',
                                       'marginLeft': '5%',
                                       'verticalAlign': 'top',
                                       'display': 'inline-block'}),
                       html.Div([html.Label('Selecciona el marginal del eje X'),
                                 dcc.RadioItems(id='marginal-x', options=#Completar4, labelStyle={'display': 'block'})],
                                style={'width': '20%',
                                       'marginRight': '4%',
                                       'display': 'inline-block'}),
                       html.Div([html.Label('Seleccionar la variable del eje Y'),
                                 dcc.Dropdown(id='eje-y', options=#Completar3)],
                                style={'width': '20%',
                                       'marginRight': '3%',
                                       'verticalAlign': 'top',
                                       'display': 'inline-block'}),
                       html.Div([html.Label('Selecciona el marginal del eje Y'),
                                 dcc.RadioItems(id='marginal-y', options=#Completar4, labelStyle={'display': 'block'})],
                                style={'width': '20%',
                                       'display': 'inline-block'}),
                       html.Div([dcc.Graph(id='scatter')])])

@app.callback(Output('scatter', 'figure'),
              [Input('eje-x', 'value'),
               Input('marginal-x', 'value'),
               Input('eje-y', 'value'),
               Input('marginal-y', 'value')])
def update_outputs(vx, mx, vy, my):
    fig = px.scatter(df,
                     x=#Completar5,
                     y=#Completar6,
                     color='class',
                     marginal_x=#Completar7,
                     marginal_y=#Completar8,
                     title='Diagrama de dispersión: '+str(#Completar5)+' v.s. '+str(#Completar6))
    return fig

if __name__ == '__main__':
    app.run_server()
