import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(['Esta es la división más externa!',
                       html.Div(['Esta es una división interna!'],
                                style={'color':'blue',
                                       'border':'2px blue dotted'}),
                       html.Div(['Otra división interna!'],
                                style={'color':'green',
                                       'border':'2px green dashed'})],
                      style={'color':'red',
                             'border':'3px red solid'})

if __name__ == '__main__':
    app.run_server()
