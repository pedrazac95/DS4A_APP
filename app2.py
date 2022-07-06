import pandas as pd
#import plotly.express as px  
#import plotly.graph_objects as go

import dash
from dash import Dash, dcc, html, Input, Output
import dash_labs as dl

import dash_bootstrap_components as dbc

from callbacks import register_callbacks


#importar regresiones 

app = Dash(__name__,plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.FLATLY])

# -- Import and clean data (importing csv into pandas)
#df = pd.read_csv("intro_bees.csv")
app.config['suppress_callback_exceptions'] = True
poblacion_N = pd.read_excel('data/poblacion_por_depto_2015_2024.xlsx') #población nacional con sus proyecciones hasta 2024  
PIB_depto = pd.read_excel('data/PIB_depto_2015_2022.xlsx') #PIB por departamento y por año 


navbar1 = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink( "Inicio", href="/inicio")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem(page["name"], href=page["path"])
                for page in dash.page_registry.values()
                if page["module"] != "pages.not_found_404"
                #dbc.DropdownMenuItem("ASENCIÓN DESCRIPTION", href="#"),
                #dbc.DropdownMenuItem("PREDICTION", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="Más opciones",
            direction="start",
        ),
    ],
    brand="Vital Measurments for insurance company",
    brand_href="#",
    color="primary",
    dark=True,
)


# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([
    
    navbar1 ,
    dl.plugins.page_container,

]
)

register_callbacks(app)
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    #app.run_server(debug=True)
    app.run(host='0.0.0.0', port=8050, debug=True)