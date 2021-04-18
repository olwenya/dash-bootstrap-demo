import dash
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

app.layout = dbc.Container(
    dbc.Alert("Hello Neighbor", color="success")
)

if __name__ == '__main__':
    app.run_server()