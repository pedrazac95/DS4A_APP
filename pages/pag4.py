#libraries

#from turtle import reset
import pandas as pd
import numpy as np 
from dash_labs.plugins.pages import register_page

from dash import  dcc, html, Input, Output, callback

import dash_bootstrap_components as dbc

import json

import joblib


import components.graphs.regresion_beneficiarios as predben




register_page(__name__, path="/users_prediction" , order=4 , name='Predicción de usuarios')


#read data
df_prediccion_benef = pd.read_csv('data/df_prediccion_benef.csv', sep=',')

departamentos = json.load(open('data/Colombia.geojson' , 'r',encoding="utf8"))
for fish in departamentos['features']:
    fish['id'] = fish['properties']['NOMBRE_DPT']

df_benef_depto = pd.read_csv('data/df_benf_depto.csv', sep=',')

model_benef = joblib.load('data/model_pred_benf.pkl')




layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([ dbc.Alert("Consulte aqui información referente a las predicciones de la cantidad de beneficiarios potenciales en un contrato, dadas las caracaterísticas del titular del contrato, tales como mes de inscripción, edad, genero, categoría de trabajo y unidad territorial ", color="primary")])
        ])]),

    dbc.Row([
          
        dbc.Col([
            html.Br(),
            dbc.Alert("Ingrese los datos para la predicción de ususarios: ",color="light"),
            html.Br(),
            dbc.Label("Ingrese el valor mensual a pagar (en COP) del contrato:   "),
            dbc.Input(
                id="valor_mensual",
                placeholder="Ingrese valor mensual ",
                value = None,
                #style={'width': "50%"},
                ),
            html.Br(),
            dbc.Label("Ingrese la edad del titular en años: "),
            dbc.Input(
                id="valor_age", 
                placeholder="Ingrese la edad", 
                type="number",
                min=0, max=120, step=1),
            html.Br(),
            dbc.Label("Seleccione género del titular: "),
            dbc.Select(
                id="valor_sexo",
                options=[
                    {"label": "Masculino", "value": "M"},
                    {"label": "Femenino", "value": "F"},
                    ],
                value = "M",
                #style={'width': "50%"},
                placeholder="Seleccione género del titular",
                ),
            html.Br(),
            dbc.Label("Selecciona una categoría: "),
            dbc.Select(
                id="nombre_UEN",
                options=[
                    {"label": "POLICIA", "value": "POLICIA NACIONAL"},
                    {"label": "ELECTRIFICADORAS", "value": "ELECTRIFICADORAS"},
                    {"label": "EMPRESARIAL", "value": "EMPRESARIAL"},
                    {"label": "FUERZAS MILITARES", "value": "FUERZAS MILITARES"},
                    ],
                value = "EMPRESARIAL",
                #style={'width': "50%"},
                placeholder="Selecciona una categoría",
                ),
            html.Br(),
            dbc.Label("Seleccione unidad territorial: "),
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
                value = "Cali",
                #style={'width': "50%"},
                placeholder="Seleccione unidad territorial",
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
        html.Br(),
    dbc.Row([
        dbc.Col([
            html.Div([
                dbc.Button("Calcular predicción", id='calculate_prediction' ,color="success", className="me-1", outline=False, n_clicks=0),
                ],
                className="d-grid gap-2 d-md-flex justify-content-md-center"
                ),
            html.Br(),
            #dbc.Alert(color="success", id= 'alert_prediction'),
        ]
        ,width=3
        ), dbc.Col(html.H3(id="example-output", style={"verticalAlign": "middle"}))          
    ])
])
    



# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@callback(
    [Output(component_id='example-output', component_property='children'),
    Output(component_id='calculate_prediction', component_property='n_clicks')],
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
    if n == 0:
        return ['Aquí obtendrá el valor de la predicción',0]
    else:
        df_1 = predben.modelo_beneficiarios( df_prediccion_benef,int(valor_mensual) ,valor_age, valor_sexo,nombre_UEN,valor_sucursal)
        value= model_benef.predict(df_1)
        
        res = ["La cantidad de usuarios predicha en este contrato es de : {}".format(round(value[0])),0]
      
       
        return res
