#libraries
import pandas as pd

from dash_labs.plugins.pages import register_page

from dash import  dcc, html, Input, Output, callback
import plotly.express as px

#importar anexos
import components.Graphs as graphs
import components.tabs as tabs

register_page(__name__, path="/estimacion_costos" , order=3, name='Estimacion Costos' )

#read data
fallecidos_dane = pd.read_csv('data/Fallecimientos_por_depto_DANE_2015_2021_7_deptos.csv')
df_benef = pd.read_csv('data/Conteo_Anual_Mens_Ubic_EdadPop.csv')


layout = html.Div([
    tabs.build_tabs(),
    html.Div(id="app-content",
    ),
])



# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@callback(
    Output("app-content", "children"),
    [Input("app-tabs",  "value")],
)
def render_tab_content(tab_switch):
    if tab_switch == "prediction_data":
        return tabs.build_tab_1()
    
    else :
        return (
            html.Div(
                id="status-container",
                children=[
                    tabs.build_quick_stats_panel(),
                    html.Div(
                        id="graphs-container",
                        
                    ),
                ],
            ),
            
        )



