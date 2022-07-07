import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page
from dash import   html





register_page(__name__, path="/" , order=0, name='Inicio' )


#register_page(__name__, path="/")


boxedad = 'assets/ds4a_colombia.svg'
piedef= 'assets/laAscension.png'
layout=  dbc.Container([
    html.Br(),
    html.Div(html.H1("Bienvenido a  T-21 Multiverse !!!")),
    html.Br(),
    html.Div(html.H4("Aqui analizarás posibles escenarios del mercado y su predicción a largo plazo, además del impacto de estos a los estados financieros, para así realizar la toma de decisiones inteligentes antes que sea demasiado tarde. También podrás visualizar de manera sencilla la información poblacional y financiera de tu empresa. ")), 
    html.Br(),
    html.Div(html.H4("Podrás acceder a todas opciones que te brinda nuestra aplicación en la pestaña 'Más opciones' en la esquina superior derecha")), 
    html.Br(), 
    html.Div(html.H3(" ¡Conócenos! ")), 
    
    dbc.Row([
        dbc.Card(
    [
        dbc.CardImg(src="assets/Adriana.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Adriana Godoy González", className="card-title"),
                html.P(
                    "Ingeniera Industrial, Especialista en Inteligencia de Negocios"
                    ,
                    className="card-text",
                ),
                dbc.CardLink("Linkedin link", href="https://www.linkedin.com/in/adriana-godoy-4260211ab/"),
            ]
        ),
    ],
    style={"width": "14rem"},
), 
dbc.Card(
    [
        dbc.CardImg(src="assets/Camilo.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Camilo Pedraza Murcia", className="card-title"),
                html.P(
                    "Ingeniero Mecánico, Ingeniero de Datos",
                    className="card-text",
                ),
                dbc.CardLink("Linkedin link", href="https://www.linkedin.com/in/pedrazac/"),
            ]
        ),
    ],
    style={"width": "14rem"},
), 

dbc.Card(
    [
        dbc.CardImg(src="assets/Eduardo.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Eduardo Donado Sierra", className="card-title"),
                html.P(
                    "Ingeniero Financiero, MSc. en Finanzas ",
                    className="card-text",
                ),
                dbc.CardLink("Linkedin link", href="https://www.linkedin.com/in/david-eduardo-donado-sierra-019282161/"),
            ]
        ),
    ],
    style={"width": "14rem"},
), 
dbc.Card(
    [
        dbc.CardImg(src="assets/Fernando.png", top=True),
        dbc.CardBody(
            [
                html.H4("Fernando Alayón A.", className="card-title"),
                html.P(
                    "Gestor de Riesgos",
                    className="card-text",
                ),
                dbc.CardLink("Linkedin link", href="https://www.linkedin.com/in/fernando-alayon/"),
            ]
        ),
    ],
    style={"width": "14rem"},
), 
 dbc.Card(
    [
        dbc.CardImg(src="assets/JoseLuis.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("Jose Luis Cabrera V.", className="card-title"),
                html.P(
                    " Estadístico, MSc. en Estadística ",
                    className="card-text",
                ),
                dbc.CardLink("Linkedin link", href="https://www.linkedin.com/in/josecabrerav"),
            ]
        ),
    ],
    style={"width": "14rem"},
), 
dbc.Card(
    [
        dbc.CardImg(src="assets/JoseV.jpg", top=True),
        dbc.CardBody(
            [
                html.H4("José Antonio Valencia A.", className="card-title"),
                html.P(
                    "Ingeniero Físico, MSc. en Ciencias-Física",
                    className="card-text",
                ),
                dbc.CardLink("Linkedin link", href="https://www.linkedin.com/in/jose-antonio-valencia-aricapa-080b6850/"),
            ]
        ),
    ],
    style={"width": "14rem"},
), 

dbc.Card(
    [
        dbc.CardImg(src="assets/Sergio.jpeg", top=True),
        dbc.CardBody(
            [
                html.H4("Sergio Aldair Clavijo", className="card-title"),
                html.P(
                    "Ingeniero Industrial y Economista",
                    className="card-text",
                ),
                dbc.CardLink("Linkedin link", href="https://www.linkedin.com/in/sergioaldairclavijo/"),
            ]
        ),
    ],
    style={"width": "14rem"},
), 

    ]),
    dbc.Row([
        dbc.Col(dbc.Card([html.Img(id='boxplot_edad_img', src=boxedad, className='myImg',height=300)],body=True,)),
         dbc.Col(dbc.Card([html.Img(id='barplor_defun_img', src=piedef, className='myImg2',height=300)],body=True,)),
        ])

        ])
