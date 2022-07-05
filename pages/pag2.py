#libraries
import pandas as pd

from dash_labs.plugins.pages import register_page

from dash import  dcc, html, Input, Output, callback
import plotly.express as px

#importar anexos
import components.Graphs as graphs

register_page(__name__, path="/estimacion_ingresos" , order=2, name='Estimacion Ingresos' )

#read data
fallecidos_dane = pd.read_csv('data/Fallecimientos_por_depto_DANE_2015_2021_7_deptos.csv')
df_benef = pd.read_csv('data/Conteo_Anual_Mens_Ubic_EdadPop.csv')


layout = html.Div([
    
    html.Br(),
    
    dcc.Dropdown(
        id="slct_year",
        options=[
            {"label": "ANTIOQUIA", "value": "ANTIOQUIA"},
            {"label": "ATLANTICO", "value": "ATLANTICO"},
            {"label": "BOGOTA D.C.", "value": "BOGOTA D.C."},
            {"label": "BOLIVAR", "value": "BOLIVAR"},
            {"label": "BOYACA", "value": "BOYACA"},
            {"label": "CALDAS", "value": "CALDAS"},
            {"label": "CAQUETA", "value": "CAQUETA"},
            {"label": "CASANARE", "value": "CASANARE"},
            {"label": "CAUCA", "value": "CAUCA"},
            {"label": "CESAR", "value": "CESAR"},
            {"label": "CUNDINAMARCA", "value": "CUNDINAMARCA"},
            {"label": "HUILA", "value": "HUILA"},
            {"label": "MAGDALENA", "value": "MAGDALENA"},
            {"label": "META", "value": "META"},
            {"label": "NARIÑO", "value": "NARIÑO"},
            {"label": "NORTE DE SANTANDER", "value": "NORTE DE SANTANDER"},
            {"label": "PUTUMAYO", "value": "PUTUMAYO"},
            {"label": "QUINDIO", "value": "QUINDIO"},
            {"label": "RISARALDA", "value": "RISARALDA"},
            {"label": "SANTANDER", "value": "SANTANDER"},
            {"label": "SUCRE", "value": "SUCRE"},
            {"label": "TOLIMA", "value": "TOLIMA"},
            {"label": "VALLE DEL CAUCA", "value": "VALLE DEL CAUCA"},
            ],
        multi=True,
        value = [],
        style={'width': "50%"},
        placeholder="Select a region",
        ),

    html.Div(id='output_container', children=[]),
    html.Br(),
    dcc.Graph(id='graph1', figure={}),


    dcc.Dropdown(
        id="slct_dpto",
        options=[
            {"label": "ATLANTICO", "value": "ATLANTICO"},
            {"label": "BOGOTA D.C.", "value": "BOGOTA D.C."},
            {"label": "HUILA", "value": "HUILA"},
            {"label": "NARIÑO", "value": "NARIÑO"},
            {"label": "SANTANDER", "value": "SANTANDER"},
            {"label": "TOLIMA", "value": "TOLIMA"},
            {"label": "VALLE DEL CAUCA", "value": "VALLE DEL CAUCA"},           
            ],
        multi=True,
        value=[],
        style={'width': "50%"},
        placeholder="Select a region"
        ),

    dcc.Graph(id='grafica_falleccidos', figure={}),

    dcc.Dropdown(
        id="slct_dpto3",
        options=[
            {"label": "ANTIOQUIA", "value": "ANTIOQUIA"},
            {"label": "ATLANTICO", "value": "ATLANTICO"},
            {"label": "BOGOTA D.C.", "value": "BOGOTA D.C."},
            {"label": "BOLIVAR", "value": "BOLIVAR"},
            {"label": "BOYACA", "value": "BOYACA"},
            {"label": "CALDAS", "value": "CALDAS"},
            {"label": "CAQUETA", "value": "CAQUETA"},
            {"label": "CASANARE", "value": "CASANARE"},
            {"label": "CAUCA", "value": "CAUCA"},
            {"label": "CESAR", "value": "CESAR"},
            {"label": "CUNDINAMARCA", "value": "CUNDINAMARCA"},
            {"label": "HUILA", "value": "HUILA"},
            {"label": "MAGDALENA", "value": "MAGDALENA"},
            {"label": "META", "value": "META"},
            {"label": "NARIÑO", "value": "NARIÑO"},
            {"label": "NORTE DE SANTANDER", "value": "NORTE DE SANTANDER"},
            {"label": "PUTUMAYO", "value": "PUTUMAYO"},
            {"label": "QUINDIO", "value": "QUINDIO"},
            {"label": "RISARALDA", "value": "RISARALDA"},
            {"label": "SANTANDER", "value": "SANTANDER"},
            {"label": "SUCRE", "value": "SUCRE"},
            {"label": "TOLIMA", "value": "TOLIMA"},
            {"label": "VALLE DEL CAUCA", "value": "VALLE DEL CAUCA"},           
            ],
        multi=True,
        value=[],
        style={'width': "50%"},
        placeholder="Select a region"
        ),

        dcc.Graph(id='grafica_siniestros', figure={}),


    

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
