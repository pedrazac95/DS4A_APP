#libraries
#from turtle import update
import pandas as pd

from dash_labs.plugins.pages import register_page

from dash import  dcc, html, Input, Output, callback
import plotly.express as px
import dash_bootstrap_components as dbc


#importar anexos
import components.Graphs as graphs
import components.tabs as tabs

import components.graphs.graphs as josegraphs
import components.graphs.FuncionesFinancieras as funfin



register_page(__name__, path="/business_status" , order=1 , name='Business Status' )

#read data
fallecidos_dane = pd.read_csv('data/Fallecimientos_por_depto_DANE_2015_2021_7_deptos.csv')
#df_benef = pd.read_csv('data/Conteo_Anual_Mens_Ubic_EdadPop.csv')

Conteo_Union = pd.read_csv('data/Conteo_Anual_Mens_Pop_Ubic_TotalNacional.csv')

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            tabs.build_tabs_business()
        ],
        )
    ]),
    html.Br(),
    dbc.Row(id= 'row_info', children=[
    ]),
    dbc.Row(id= 'row_info_2', children=[
    ])
])



# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@callback(
    [Output(component_id='graph1_status', component_property='figure'),
     Output(component_id='graph2_status', component_property='figure'),
     Output(component_id='graph3_status', component_property='figure'),
     Output(component_id='graph4_status', component_property='figure'),
     Output(component_id='graph5_status', component_property='figure')],
    [Input(component_id='region_status', component_property='value')]
)
def update_graphics(option_selected) :
    graph1 = josegraphs.plot_totalafiliados_year_mes_deptoN(Conteo_Union, option_selected)
    graph2 = josegraphs.plot_retiros_year_mes_deptoN(Conteo_Union, option_selected)
    graph3 = josegraphs.plot_siniestros_year_mes_deptoN(Conteo_Union, option_selected)
    graph4 = josegraphs.plot_PobActual_year_mes_deptoN(Conteo_Union, option_selected)
    graph5 = josegraphs.plot_popSiniestros_year_mes_deptoN(Conteo_Union, option_selected)

    return graph1 , graph2, graph3, graph4 , graph5


@callback(
    Output(component_id='row_info', component_property='children'),
    Input(component_id='business-tabs', component_property='value')
)
def render_tab_content(tab_switch):
    if tab_switch == "financial-info":
        return tabs.build_tab_financial_info()

    elif tab_switch == "business-status":
        return tabs.build_tab_business_info()


@callback(
    Output(component_id='row_info_2', component_property='children'),
    [Input(component_id='business-info-tabs', component_property='value'),
    Input(component_id='business-tabs', component_property='value')]
)

def render_tab_content(tab_switch,tab_switch2):
    if tab_switch2 == "business-status":
        if tab_switch == "population-info" :
            return tabs.build_tab_business_info_population()

        elif tab_switch == "deaths-info"  :
            return tabs.build_tab_business_info_deaths()

@callback(
[Output("graph1_financial", "figure"),
Output("graph2_financial", "figure"),
Output("graph3_financial", "figure"),
Output("graph4_financial", "figure")],
[Input("region_financial_info",  "value")],
)
def render_tab_content(option_selected):
    fig1 = funfin.plot_finz_mens(funfin.df_input_proj,0,0,0, option_selected )
    fig2 = funfin.plot_finz_mens_line(funfin.df_input_proj,0,0,0)
    fig3 = funfin.plot_finz_anual(funfin.df_input_proj,0,0,0, option_selected )
    fig4 = funfin.plot_finz_anual_line(funfin.df_input_proj,0,0,0, option_selected)

    return fig1 , fig2 , fig3, fig4
