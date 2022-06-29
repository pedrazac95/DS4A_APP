import pandas as pd
import plotly.express as px  
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc


#importar regresiones 
import regresion_ascension as ra
import regresion_dane as rd

#importar anexos
import components.Graphs as graphs





app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

# -- Import and clean data (importing csv into pandas)
#df = pd.read_csv("intro_bees.csv")
df = pd.read_csv("data/conteo_union.csv")

poblacion_N = pd.read_excel('data/poblacion_por_depto_2015_2024.xlsx') #población nacional con sus proyecciones hasta 2024  
PIB_depto = pd.read_excel('data/PIB_depto_2015_2022.xlsx') #PIB por departamento y por año 
fallecidos_dane = pd.read_csv('data/Fallecimientos_por_depto_DANE_2015_2021_7_deptos.csv')

df_benef = pd.read_csv('data/Conteo_Anual_Mens_Ubic_EdadPop.csv')



navbar1 = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink( "Inicio", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("DANE DESCRIPTION", href = "#"),
                dbc.DropdownMenuItem("ASENCIÓN DESCRIPTION", href="#"),
                dbc.DropdownMenuItem("PREDICTION", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
            direction="start",
        ),
    ],
    brand="DS4A Project - La Aensción - Team 21",
    brand_href="#",
    color="primary",
    dark=True,
)


# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([
    
    navbar1 ,

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
    dcc.Graph(id='my_bee_map', figure={}),


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
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The departments chosen by user are: {}".format(', '.join(option_slctd))

    fig = graphs.graph1(df, option_slctd)

    '''dff = df.copy()
    dff = dff[dff["Sucursal"].isin(option_slctd)]
    # Plotly Express

    fig = px.line(dff[(dff['Year_Month']!='NA')], x='Year_Month', y="Count_CCont", color='Sucursal' )
'''
    return container , fig


@app.callback(
    Output(component_id='grafica_falleccidos', component_property='figure'),
    [Input(component_id='slct_dpto', component_property='value')]
)
def update_graph_2(option_slctd):

    '''fallecidos_copy = fallecidos_dane.copy()
    fallecidos_dep =fallecidos_copy[fallecidos_copy['DEPARTAMENTO'].isin(option_slctd)]
    fal_dane_anio = fallecidos_dep.groupby(["anio", 'DEPARTAMENTO']).size().reset_index()
    fal_dane_anio.columns= ["AÑO", 'DEPARTAMENTO', "Total_fallecidos"]
    fig = px.bar(fal_dane_anio,x="AÑO",y="Total_fallecidos" , color='DEPARTAMENTO')'''

    return  graphs.graph2(fallecidos_dane, option_slctd)


@app.callback(
    Output(component_id='grafica_siniestros', component_property='figure'),
    [Input(component_id='slct_dpto3', component_property='value')]
)
def update_graph_2(option_slctd):

    return  graphs.graph3(df_benef, option_slctd)


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    #app.run_server(debug=True)
    app.run(host='0.0.0.0', port=8050, debug=True)