#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    home.py
# @Author:      Kuro
# @Time:        18/4/2023 9:37 AM

import warnings

import dash_bootstrap_components as dbc
import pandas as pd
from dash import html, dcc, Output, Input, State, callback

warnings.filterwarnings("ignore")
from utils import encode_data, scale_data, load_model

draw_type_encode = 'model/encode_draw_type.pkl'
feed_type_encode = 'model/encode_feed_type.pkl'

scale_aw = 'model/scale_aw.pkl'
scale_b = 'model/scale_b.pkl'
scale_power = 'model/scale_power.pkl'
scale_s = 'model/scale_s.pkl'

model_aw = 'model/rf_aw.pkl'
model_power = 'model/rf_power.pkl'
model_s = 'model/rf_s.pkl'
model_b = 'model/rf_b.pkl'

draw_type_options = [
    'Synthetic water/ NaCl',
    'Synthetic seawater brine/ NaCl',
    'Synthetic SWRO brine/ NaCl',
    'Synthetic water/ Organic potassium acetate',
    'Synthetic water/ Sodium propionate', 'Synthetic Seawater/ NaCl',
    'Produced water (PW) from petroleum industry',
    'Synthetic RO brine/ NaCl', 'Synthetic seawater/ NaCl',
    'Synthetic water/ Potassium cirate (KCit)',
    'Synthetic water/ Ammonium bicarbonate (NH4HCO3)',
    'Synthetic water/ Sodium chloride (NaCl)',
    'Synthetic Seawater brine/NaCl',
    'Synthetic water/ Calcium accetate (CaAc)',
    'Synthetic water/ Potassium oxalate (KOxa)',
    'Synthetic water/ Ammonium acetate (NH4Ac)',
    'Synthetic water/ Potassium formate (KF)',
    'Seawater brine from the\n TuaSpring desalination plant',
    'Synthetic water/ Calcium propionate (CaP)', 'SWRO brine',
    'Seawater ', 'Synthetic water/ Potassium accetate (KAc)',
    'Synthetic water/ Ammonium carbamate (NH4C)',
    'Synthetic water/ Ammonium formate (NH4F)',
    'Synthetic water/ Sodium glycolate (NaGly)',
    'Synthetic water/ Sodium propionate (NaP)', 'Synthetic water/ KBr',
    'Synthetic water/ KCl', 'Synthetic water/ CaCl2'
]

feed_type_options = [
    'Deionized water', 'Synthetic water/ NaCl',
    'Synthetic riverwater/ NaCl', 'Synthetic wastewater brine/ NaCl',
    'Tap water', 'Ultrapure water', 'Synthetic wastewater/ NaCl',
    'Distilled water', 'NaCl', 'Synthetic RiverWater',
    'Synthetic river water', 'Synthetic Wastewater brine/ NaCl',
    'Wastewater retentate from the NEWater plant \n', 'Fresh water',
    'Treated Wastewater', 'Salt free fresh water',
    'UF treated Wastewater retentate from the NEWater plant \n',
    'MilliQ',
    'NF treated Wastewater retentate from the NEWater plant \n',
    'Municipal wastewater', 'Synthetic river water/ NaCl'
]


def home():
    return html.Div(children=[
        dbc.Row([
            dbc.Col([
                html.Label("Draw Type:", style={'margin-left': '1em'}),
                dcc.Dropdown(
                    id='draw_type',
                    options=draw_type_options,
                    value=draw_type_options[0],
                    style={'margin-left': '0.5em'}
                )
            ]),
            dbc.Col([
                html.Label("Feed Type:", style={'margin-left': '1em'}),
                dcc.Dropdown(
                    id='feed_type',
                    options=feed_type_options,
                    value=feed_type_options[0],
                    style={'margin-left': '0.5em'}
                )
            ], style={'margin-bottom': '1em'}),
        ], style={'margin-right': '0.5em'}),
        dbc.Row([
            dbc.Col([
                html.Label("Draw Flow Rate L/min:", style={'margin-left': '1em'}),
                dcc.Input(
                    id='draw_flow_rate',
                    type='number',
                    value=0.5,
                    style={'margin-left': '0.5em', 'width': '5em'}
                )
            ]),
            dbc.Col([
                html.Label("Feed Flow Rate L/min:", style={'margin-left': '1em'}),
                dcc.Input(
                    id='feed_flow_rate',
                    type='number',
                    value=0.5,
                    style={'margin-left': '0.5em', 'width': '5em'}
                )
            ]),
            dbc.Col([
                html.Label("Draw Concentration M:", style={'margin-left': '1em'}),
                dcc.Input(
                    id='draw_concentrate_m',
                    type='number',
                    value=0.599,
                    style={'margin-left': '0.5em', 'width': '5em'}
                )
            ]),
            dbc.Col([
                html.Label("Feed Concentration M:", style={'margin-left': '1em'}),
                dcc.Input(
                    id='feed_concentrate_m',
                    type='number',
                    value=0,
                    style={'margin-left': '0.5em', 'width': '5em'}
                )
            ]),
        ], style={'margin-bottom': '0.5em'}),
        dbc.Row([
            dbc.Col([
                html.Label("Draw Temprature K:", style={'margin-left': '1em'}),
                dcc.Input(
                    id='draw_temp_k',
                    type='number',
                    value=298.0,
                    style={'margin-left': '1.7em', 'width': '5em'}
                )
            ]),
            dbc.Col([
                html.Label("Feed Temprature K:", style={'margin-left': '1em'}),
                dcc.Input(
                    id='feed_temp_k',
                    type='number',
                    value=298.0,
                    style={'margin-left': '1.7em', 'width': '5em'}
                )
            ]),
            dbc.Col([
                html.Label("∆π bar:", style={'margin-left': '1em'}),
                dcc.Input(
                    id='pi_bar',
                    type='number',
                    value=27.63,
                    style={'margin-left': '7.5em', 'width': '5em'}
                )
            ]),
            dbc.Col([
                html.Label("ΔP bar:", style={'margin-left': '1em'}),
                dcc.Input(
                    id='p_bar',
                    type='number',
                    value=0,
                    style={'margin-left': '7.5em', 'width': '5em'}
                )
            ]),
        ], style={'margin-bottom': '0.5em'}),
        dbc.Row([
            dbc.Col([
                html.Label("Jw L/(m2.h):", style={'margin-left': '1em'}),
                dcc.Input(
                    id='jw',
                    type='number',
                    value=15.286200,
                    style={'margin-left': '5.15em', 'width': '5em'}
                )
            ]),
            dbc.Col([]), dbc.Col([]), dbc.Col([])
        ], style={'margin-bottom': '4em'}),
        ######################-Button-######################
        html.Div(
            dbc.Button(id='pred_btn', children="Predict",
                       style={'verticalAlign': 'middle', "margin-top": "30px", "margin-bottom": "60px",
                              'width': '200px'},
                       n_clicks=0),
            style={"textAlign": "center"}
        ),
        ###################################################
        dbc.Row([
            dbc.Col(html.Label(children="Power Density W/m2:", style={'font-weight': 'bold'})),
            dbc.Col(
                dcc.Loading(
                    id="loading1",
                    type="default",
                    children=html.Label(id='power_output', children="0")
                )
            ),
            dbc.Col([]), dbc.Col([]), dbc.Col([]), dbc.Col([]), dbc.Col([])
        ], style={'margin-bottom': '0.5em'}),
        dbc.Row([
            dbc.Col(html.Label(children="Aw L/(m2.h.bar):", style={'font-weight': 'bold'})),
            dbc.Col(
                dcc.Loading(
                    id="loading2",
                    type="default",
                    children=html.Label(id='aw_output', children="0")
                )
            ),
            dbc.Col([]), dbc.Col([]), dbc.Col([]), dbc.Col([]), dbc.Col([])
        ], style={'margin-bottom': '0.5em'}),
        dbc.Row([
            dbc.Col(html.Label(children="B L/(m2.h):", style={'font-weight': 'bold'})),
            dbc.Col(
                dcc.Loading(
                    id="loading3",
                    type="default",
                    children=html.Label(id='bl_output', children="0")
                )
            ),
            dbc.Col([]), dbc.Col([]), dbc.Col([]), dbc.Col([]), dbc.Col([])
        ], style={'margin-bottom': '0.5em'}),
        dbc.Row([
            dbc.Col(html.Label(children="S m:", style={'font-weight': 'bold'})),
            dbc.Col(dcc.Loading(
                id="loading4",
                type="default",
                children=html.Label(id='s_output', children="0")
            )),
            dbc.Col([]), dbc.Col([]), dbc.Col([]), dbc.Col([]), dbc.Col([])
        ], style={'margin-bottom': '0.5em'}),

    ], style={'margin-top': '2em'})


@callback(
    Output("power_output"*10000, "children"),
    Output("aw_output"*10000, "children"),
    Output("bl_output"*10000, "children"),
    Output("s_output"*10000, "children"),

    Input("pred_btn", "n_clicks"),

    State("draw_type", "value"),
    State("feed_type", "value"),
    State("draw_flow_rate", "value"),
    State("feed_flow_rate", "value"),
    State("draw_concentrate_m", "value"),
    State("feed_concentrate_m", "value"),
    State("draw_temp_k", "value"),
    State("feed_temp_k", "value"),
    State("pi_bar", "value"),
    State("p_bar", "value"),
    State("jw", "value"),
    prevent_initial_call=True,
)
def page_return(n_clicks, draw_type, feed_type, draw_flow_rate, feed_flow_rate, draw_concentrate_m,
                feed_concentrate_m, draw_temp_k, feed_temp_k, pi_bar, p_bar, jw):
    if n_clicks != 0:
        df_test = pd.DataFrame([[draw_type, feed_type, draw_flow_rate, feed_flow_rate, draw_concentrate_m,
                                 feed_concentrate_m, draw_temp_k, feed_temp_k, pi_bar, p_bar, jw]])

        df_test = encode_data(df_test, 0, draw_type_encode)
        df_test = encode_data(df_test, 1, feed_type_encode)

        df_power = df_test.copy()
        df_aw = df_test.copy()
        df_b = df_test.copy()
        df_s = df_test.copy()

        X_test_power = scale_data(df_power, scale_power)
        X_test_aw = scale_data(df_aw, scale_aw)
        X_test_b = scale_data(df_b, scale_b)
        X_test_s = scale_data(df_s, scale_s)

        rf_power, rf_aw, rf_b, rf_s = load_model(model_power, model_aw, model_b, model_s)

        power_pred = rf_power.predict(X_test_power)
        aw_pred = rf_aw.predict(X_test_aw)
        b_pred = rf_b.predict(X_test_b)
        s_pred = rf_s.predict(X_test_s)
        return power_pred, aw_pred, b_pred, s_pred
    else:
        return None, None, None, None
