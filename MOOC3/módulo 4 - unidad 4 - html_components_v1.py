import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(['Esta es la división más externa!'],
                      style={'color':'red',
                             'border':'3px red solid'})

if __name__ == '__main__':
    app.run_server()