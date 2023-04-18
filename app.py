#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    app.py
# @Author:      Kuro
# @Time:        18/4/2022 3:24 AM


import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

from pages.home import home

app = dash.Dash(__name__,
                assets_folder="assets",
                assets_url_path="assets",
                external_stylesheets=[
                    dbc.themes.BOOTSTRAP,
                    "https://cdn.jsdelivr.net/gh/lipis/flag-icons@6.6.6/css/flag-icons.min.css"
                ])

app.config['suppress_callback_exceptions'] = True

app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    html.Div(children=home())
])

if __name__ == "__main__":
    app.run_server(debug=True)
