import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

df = pd.read_csv('Datasets/mpg.csv')
df['year'] = df['model_year'] + np.random.randint(-4,5,df.shape[0])*0.10

app = dash.Dash()
app.layout = html.Div([html.Div([dcc.Graph(id='mpg_scatter',
                                           figure={'data':[go.Scatter(x = df['year']+1900,
                                                                      y = df['mpg'],
                                                                      text = df['name'],
                                                                      hoverinfo = 'text',
                                                                      mode = 'markers')],
                                                   'layout': go.Layout(title = 'mpg.csv dataset',
                                                                       xaxis = {'title': 'model year'},
                                                                       yaxis = {'title': 'miles per gallon'},
                                                                       hovermode='closest')})],
                                style={'width':'50%','display':'inline-block'}),
                       html.Div([dcc.Graph(id='mpg_line',
                                           figure={'data': [go.Scatter(x = [0,1],
                                                                       y = [0,1],
                                                                       mode = 'lines')],
                                                   'layout': go.Layout(title = 'acceleration',
                                                                       margin = {'l':0})}),
                                 dcc.Markdown(id='mpg_stats')],
                                style={'width':'20%',
                                       'height':'50%',
                                       'display':'inline-block'})])

@app.callback(Output('mpg_line', 'figure'),
              [Input('mpg_scatter', 'hoverData')])
def callback_graph(hoverData):
    v_index=hoverData['points'][0]['pointIndex']
    fig={'data':[go.Scatter(x = [0,1],
                            y = [0,60/df.iloc[v_index]['acceleration']],
                            mode='lines',
                            line={'width':2*df.iloc[v_index]['cylinders']})],
         'layout': go.Layout(title = df.iloc[v_index]['name'],
                             xaxis = {'visible':False},
                             yaxis = {'visible':False,
                                      'range':[0,60/df['acceleration'].min()]},
                             margin = {'l':0},
                             height = 300)}
    return fig

@app.callback(Output('mpg_stats', 'children'),
              [Input('mpg_scatter', 'hoverData')])
def callback_stats(hoverData):
    v_index=hoverData['points'][0]['pointIndex']
    stats = """
            {} cylinders\n
            {}cc displacement\n
            0 to 60mph in {} seconds""".format(df.iloc[v_index]['cylinders'],
                                               df.iloc[v_index]['displacement'],
                                               df.iloc[v_index]['acceleration'])
    return stats

if __name__ == '__main__':
    app.run_server()