import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([dcc.Input(id='txt',
                                 value='Texto inicial',
                                 type='text'),
                       html.Div(id='div')])


@app.callback(Output(component_id='div',
                     component_property='children'),
              [Input(component_id='txt',
                     component_property='value')])
def update_div(input_value):
    return "El texto que ingresado es: {}".format(input_value)


if __name__ == '__main__':
    app.run_server()
