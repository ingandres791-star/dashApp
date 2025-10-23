import dash
from dash import html, dcc
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import pandas as pd

app=dash.Dash(external_stylesheets=[dbc.themes.FLATLY])
server=app.server

data=pd.read_excel("datos/AREAS Y DESORILLES LEAR_(2025).xlsx",sheet_name=None)
AREAS=data["AREA"]
app.layout=html.Div(children=[html.H1("DASHBOARD TEST"),
                              html.Div("Hola mundo :)")
                             ])


if __name__=="__main__":
    app.run_server(debug=True,port=8050)
