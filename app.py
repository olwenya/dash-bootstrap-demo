import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

app.layout = dbc.Container(
    dbc.Jumbotron(children=[
        html.H1("HELLO NEIGHBOR"),
        html.P('dash bootstrap demo')
    ])
)

if __name__ == '__main__':
    app.run_server(debug=True)