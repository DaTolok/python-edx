import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([html.Label('Dropdown'),
                       dcc.Dropdown(options=[{'label': 'New York City', 'value': 'NYC'},
                                             {'label': 'Montréal', 'value': 'MTL'},
                                             {'label': 'San Francisco', 'value': 'SF'}],
                                    value='MTL')])

if __name__ == '__main__':
    app.run_server()