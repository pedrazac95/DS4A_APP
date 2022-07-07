#libraries
import pandas as pd
from dash_labs.plugins.pages import register_page
from dash import  dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc


#importar anexos
import components.graphs.graficas_pred_dane_ascension as josepred



register_page(__name__, path="/death_prediction" , order=5, name='Predicción tasa de mortalidad' )

#read data
#fallecidos_dane = pd.read_csv('data/Fallecimientos_por_depto_DANE_2015_2021_7_deptos.csv')
#df_benef = pd.read_csv('data/Conteo_Anual_Mens_Ubic_EdadPop.csv')

ascension_mes = pd.read_csv("data/prediccion_tasa_mes_ascension.csv")
dane_ascension_anio = pd.read_csv("data/prediccion_tasa_anio_dane_ascension.csv")



layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([ dbc.Alert("Consulte aqui información referente a las predicciones de la tasa de mortaliadad a nivel Nacional utilizando datos registrados por el DANE, y a nivel organización con los datos registrados en la empresa. Estas predicciones dependen del comportamiento de las defunciones y del PIB per cápita de cada departamento a consultar", color="primary"),
                        dbc.Row([
            dbc.Alert("Seleccione Aquí los departamentos que desee visualizar ", color="light",className='alert w-60'),
            ]),
                dcc.Dropdown(
                    id="region_death_prediction",
                    options=[
                        {"label": "NACIONAL", "value": "NACIONAL"},
                        {"label": "ANTIOQUIA", "value": "ANTIOQUIA"},
                        {"label": "ATLANTICO", "value": "ATLANTICO"},
                        {"label": "BOGOTA D.C.", "value": "BOGOTA D.C."},
                        {"label": "BOLIVAR", "value": "BOLIVAR"},
                        {"label": "BOYACA", "value": "BOYACA"},
                        {"label": "HUILA", "value": "HUILA"},
                        {"label": "NARIÑO", "value": "NARIÑO"},
                        {"label": "SANTANDER", "value": "SANTANDER"},
                        {"label": "TOLIMA", "value": "TOLIMA"},
                        {"label": "VALLE DEL CAUCA", "value": "VALLE DEL CAUCA"},
                    ],
                    value = ["NACIONAL"],
                    multi = True,
                    #style={'width': "50%"},
                    placeholder="Select a region",
                ),
            ])
        ])
    ]),
             dbc.Row([
        html.Hr()
            ]),
    dbc.Row([
        dbc.Col([#dbc.Alert("Visualice aquí información referente a la predicción la tasa de mortalidad ANUAL, a nivel Nacional con datos del DANE  ", color="light"),
            #dbc.Card([
             #   dcc.Graph(id='graph1_pred_dane', figure={}),
            #],
            #body=True,
            #color='light'),
         #   dbc.Row([
        #html.Hr()
            #]),
              dbc.Alert("Visualice aquí información referente a la predicción la tasa de mortalidad ANUAL, a nivel organizacional con datos de la empresa", color="light"),
            dbc.Card([
                dcc.Graph(id='graph2_pred_dane', figure={}),
            ],
            body=True,
            color='light'),
            dbc.Row([
        html.Hr()
            ]),  dbc.Alert("Visualice aquí información referente a la predicción la tasa de mortalidad MENSUAL, a nivel organizacional con datos de la empresa  ", color="light"),
            dbc.Card([
                dcc.Graph(id='graph3_pred_ascencion', figure={}),
            ],
            body=True,
            color='light'
            )
        ]),
    ]),
])




# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@callback(
    [#Output("graph1_pred_dane", "figure"),
    Output("graph2_pred_dane", "figure"),
    Output("graph3_pred_ascencion", "figure")],
    [Input("region_death_prediction",  "value")],
)
def render_tab_content(option_selected):
    #fig1 = josepred.lineplot_dane_anio(dane_ascension_anio, option_selected)
    fig2 = josepred.lineplot_ascension_anio(dane_ascension_anio, option_selected)
    fig3 = josepred.lineplot_ascension_mes(ascension_mes, option_selected)

    return  fig2 , fig3


