import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page
from dash import  dcc, html, Input, Output, callback

import components.graphs.graficas_pred_dane_ascension as josepred
import base64


register_page(__name__, path="/inicio" , order=0, name='Inicio' )


#register_page(__name__, path="/")


boxedad = 'assets/causas_edad.PNG'
piedef= 'assets/mortalidad_rango_edad.PNG'
layout=  dbc.Container([
    html.Br(),
    html.Div(html.H1("Bienvenido a nuestra aplicación VMIC T-21 !!!")),
    html.Br(),
    html.Div(html.H4("Aqui analizarás posibles escenarios del mercado y su predicción a largo plazo, además del impacto de estos a los estados financieros. También podrás visualizar de manera sencilla la información poblacional y financiera de tu empresa. ")), 
    html.Div(html.H4("Podrás acceder a las diferentes opciones que te brinda nuestra aplicación en la pestaña 'Más opciones' en la esquina superior derecha")), 
    dbc.Row([
        dbc.Col(dbc.Card([html.Img(id='boxplot_edad_img', src=boxedad, className='myImg'),html.Img(id='barplor_defun_img', src=piedef, className='myImg2')],body=True,)),
        ])


])