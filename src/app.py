'''
 # Dash port of Shiny iris k-means example:
 # https://shiny.rstudio.com/gallery/kmeans-example.html
 # Source: https://dash-bootstrap-components.opensource.faculty.ai/examples/iris/
 # @ Create Time: 2025-10-22 16:40:55.586733
 # Run this app with `python app.py` and
 # visit http://127.0.0.1:8050/ in your web browser.
'''

import dash
from dash import html, dcc
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

app=dash.Dash(external_stylesheets=[dbc.themes.FLATLY])
server=app.server
app.layout=html.Div(html.H1("DASHBOARD TEST"))


if __name__=="__main__":
    app.run_server(debug=True,port=8050)
