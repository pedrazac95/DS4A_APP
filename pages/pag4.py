#libraries
from multiprocessing.sharedctypes import Value
import pandas as pd

from dash_labs.plugins.pages import register_page

from dash import  dcc, html, Input, Output, callback
import plotly.express as px
import dash_bootstrap_components as dbc

import json

import joblib


#importar anexos
import components.Graphs as graphs

import components.graphs.regresion_beneficiarios as predben

import components.Graphs as graphs


register_page(__name__, path="/users_prediction" , order=4 , name='User prediction')


#read data
df_prediccion_benef = pd.read_csv('data/df_prediccion_benef.csv', sep=',')

departamentos = json.load(open('data/Colombia.geojson' , 'r',encoding="utf8"))
for fish in departamentos['features']:
    fish['id'] = fish['properties']['NOMBRE_DPT']

df_benef_depto = pd.read_csv('data/df_benf_depto.csv', sep=',')

#model_benef = joblib.load('data/model_pred_benf.data')




layout = dbc.Container([
    dbc.Row([
          
        dbc.Col([
            dbc.Label("Input data for prediction"),
            html.Br(),
            html.Br(),
            dbc.Input(
                id="valor_mensual",
                placeholder="Select a monthly value",
                value = None,
                #style={'width': "50%"},
                ),
            html.Br(),
            dbc.Input(
                id="valor_age", 
                placeholder="Enter age", 
                type="number",
                min=0, max=120, step=1),
            html.Br(),
            dbc.Select(
                id="valor_sexo",
                options=[
                    {"label": "Masculino", "value": "M"},
                    {"label": "Femenino", "value": "F"},
                    ],
                value = None,
                #style={'width': "50%"},
                placeholder="Select a genre",
                ),
            html.Br(),
            dbc.Select(
                id="nombre_UEN",
                options=[
                    {"label": "POLICIA", "value": "POLICIA NACIONAL"},
                    {"label": "ELECTRIFICADORAS", "value": "ELECTRIFICADORAS"},
                    {"label": "EMPRESARIAL", "value": "EMPRESARIAL"},
                    {"label": "FUERZAS MILITARES", "value": "FUERZAS MILITARES"},
                    ],
                value = None,
                #style={'width': "50%"},
                placeholder="Select a category",
                ),
            html.Br(),
            dbc.Select(
                id="valor_sucursal",
                options=[
                    {"label": "Outsourcing", "value": "Outsourcing"},
                    {"label": "Mocoa", "value": "Mocoa"},
                    {"label": "Cali", "value": "Cali"},
                    {"label": "Melgar", "value": "Melgar"},
                    {"label": "Florencia", "value": "Florencia"},
                    {"label": "Call Center", "value": "Call Center"},
                    {"label": "Ibague", "value": "Ibague"},
                    {"label": "Villavicencio", "value": "Villavicencio"},
                    {"label": "Sincelejo", "value": "Sincelejo"},
                    {"label": "Pasto", "value": "Pasto"},
                    {"label": "Valledupar", "value": "Valledupar"},
                    {"label": "Barranquilla", "value": "Barranquilla"},
                    {"label": "Bogota", "value": "Bogota"},
                    {"label": "Manizales", "value": "Manizales"},
                    {"label": "Medellin", "value": "Medellin"},
                    {"label": "Tunja", "value": "Tunja"},
                    {"label": "Popayan", "value": "Popayan"},
                    {"label": "Pereira", "value": "Pereira"},
                    {"label": "Santa Marta", "value": "Santa Marta"},
                    {"label": "Cartagena", "value": "Cartagena"},
                    {"label": "Bucaramanga", "value": "Bucaramanga"},
                    {"label": "Cucuta", "value": "Cucuta"},
                    {"label": "Of. Principal", "value": "Of. Principal"},
                    {"label": "Duitama", "value": "Duitama"},
                    {"label": "Neiva", "value": "Neiva"},
                    {"label": "San Gil", "value": "San Gil"},
                    {"label": "Villeta", "value": "Villeta"},
                    {"label": "Yopal", "value": "Yopal"},
                    {"label": "Armenia", "value": "Armenia"},
                    {"label": "Buenaventura", "value": "Buenaventura"},
                    {"label": "Cajamarca", "value": "Cajamarca"},
                    ],
                value = None,
                #style={'width': "50%"},
                placeholder="Select a zone",
                ),
            ]
            ,width=3
            ),
        
        dbc.Col([
            #html.Br(),
            dcc.Graph(id='graph1', figure=predben.grafica_colombia(df_benef_depto , departamentos)),
            ]
            ,width=9
            ),
        ]),
    dbc.Row([
        dbc.Col([
            html.Div([
                dbc.Button("Calculate Prediction", id='calculate_prediction' ,color="success", className="me-1", outline=True, n_clicks=0),
                ],
                className="d-grid gap-2 d-md-flex justify-content-md-center"
                ),
            html.Br(),
            #dbc.Alert(color="success", id= 'alert_prediction'),
            html.Span(id="example-output", style={"verticalAlign": "middle"}),
        ]
        ,width=3
        )          
    ])
])
    



# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@callback(
    Output(component_id='example-output', component_property='children'),
    [
    Input(component_id='valor_mensual', component_property='value'),
    Input(component_id='valor_age', component_property='value'),
    Input(component_id='valor_sexo', component_property='value'),
    Input(component_id='nombre_UEN', component_property='value'),
    Input(component_id='valor_sucursal', component_property='value'),
    Input(component_id='calculate_prediction', component_property='n_clicks'),
    ]
)
def update_prediction(valor_mensual, valor_age, valor_sexo,nombre_UEN,valor_sucursal, n):
    if n is None:
        return 'Calculate User Predcition'
    else:
        df = predben.modelo_beneficiarios( df_prediccion_benef,valor_mensual ,valor_age, valor_sexo,nombre_UEN,valor_sucursal)
        return df#model_benef.predict(df)
