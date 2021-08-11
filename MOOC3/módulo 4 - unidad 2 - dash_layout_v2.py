import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[html.H1('Hola Dash!'),
                                html.Div('Dash: Tableros web con Python'),
                                dcc.Graph(id='example',
                                          figure={'data':[{'x':[1, 2, 3],
                                                           'y':[4, 1, 2],
                                                           'type':'bar',
                                                           'name':'SF'},
                                                          {'x': [1, 2, 3],
                                                           'y': [2, 4, 5],
                                                           'type': 'bar',
                                                           'name': 'NYC'}],
                                                  'layout':{'title':'Gráficas de barras'}
                                                  }
                                          )
                                ]
                      )

if __name__ == '__main__':
    app.run_server()

"""
colors = {'background':'#111111',
          'text':'#7FDBFF'}
#CSS
html.H1('Hola Dash!',
        style={'textAlign':'center',
               'color':colors['text']})

'layout':{'title':'Gráficas de barras',
          'plot_bgcolor':colors['background'],
          'paper_bgcolor':colors['background'],
          'font':{'color':colors['text']}}

style={'backgroundColor':colors['background']}
"""