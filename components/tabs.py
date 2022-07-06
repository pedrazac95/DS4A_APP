from dash import dcc, html
import dash_daq as daq
import dash_bootstrap_components as dbc

import components.graphs.graficas_consolidado_fallecidos as josegraphs
import components.graphs.FuncionesFinancieras as funfin




def build_tabs():
    return html.Div(
        id="tabs",
        className="tabs",
        children=[
            dcc.Tabs(
                id="app-tabs",
                value="prediction_data",
                className="custom-tabs",
                children=[
                    dcc.Tab(
                        id="prediction_data_tab",
                        label="Pedriction Data",
                        value="prediction_data",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="Prediction_result_tab",
                        label="Prediction Result",
                        value="prediction_result",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                ],
            )
        ],
    )

def build_tab_1():
    return [
        # Manually select metrics
        html.Div(
            id="set-input-data-container",
            # className='twelve columns',
            children=html.P(
                "Set input data for the model"
            ),
        ),
        html.Div(
            id="settings-menu",
            children=[
                html.Div(
                    id="data-select-menu",
                    # className='five columns',
                    children=[
                        html.Label(id="data-select-title", children="Select Data"),
                        html.Br(),
                        dcc.Input(
                            id="Data-select-input-1",
                            type ='number',
                            placeholder="input type number " ,
                                )                     
                            ],
                        ),  
                
                html.Div(
                    id="value-setter-menu",
                    # className='six columns',
                    children=[
                        html.Div(id="value-setter-panel"),
                        html.Br(),
                        html.Div(
                            id="button-div",
                            children=[
                                html.Button("Update", id="value-setter-set-btn"),
                                html.Button(
                                    "View current setup",
                                    id="value-setter-view-btn",
                                    n_clicks=0,
                                ),
                            ],
                        ),
                        html.Div(
                            id="value-setter-view-output", className="output-datatable"
                        ),
                    ],
                ),
            ],
        ),
    ]


def build_quick_stats_panel():
    return html.Div(
        id="quick-stats",
        className="row",
        children=[
            html.Div(
                id="card-1",
                children=[
                    html.P("Operator ID"),
                    daq.LEDDisplay(
                        id="operator-led",
                        value="9999",
                        color="#92e0d3",
                        backgroundColor="#1e2130",
                        size=50,
                    ),
                ],
            ),
            html.Div(
                id="card-2",
                children=[
                    html.P("Time to completion"),
                    daq.Gauge(
                        id="progress-gauge",
                        max=1000,
                        min=0,
                        showCurrentValue=True,  # default size 200 pixel
                    ),
                ],
            ),
            html.Div(
                id="utility-card",
                children=[daq.StopButton(id="stop-button", size=160, n_clicks=0)],
            ),
        ],
    )


def build_tabs_business ():
    return dcc.Tabs(
                id="business-tabs",
                value="business",
                #className="business-tabs",
                children=[
                    dcc.Tab(
                        id="business-info",
                        label="Financial Information",
                        value="financial-info",
                        #className="custom-tab",
                        #selected_className="custom-tab--selected",
                        ),
                    dcc.Tab(
                        id="business-status",
                        label="Status",
                        value="business-status",
                        #className="custom-tab",
                        #selected_className="custom-tab--selected",
                        ),
                    ],
                )

def build_tab_business_info():
    return dcc.Tabs(
                id="business-info-tabs",
                value="business-info",
                className="business-tabs",
                children=[
                    dcc.Tab(
                        id="population-info",
                        label="Population",
                        value="population-info",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                        ),
                    dcc.Tab(
                        id="deaths-info",
                        label="Deaths",
                        value="deaths-info",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                        ),
                    ],
                )
    


def build_tab_business_info_population():
    return [
        html.Br(),
        dbc.Row([
            dbc.Card([dbc.Alert("Consulte aqui información referente a la cantidad de afiliados, la cantidad de retiros y fallecimientos, población activa y la tasa de mortalidad de la entidad.\n A continuación seleccione las ubicacines a consultar:", color="primary"),
                dcc.Dropdown(
                    id="region_status",
                    options=[
                        {"label": "NACIONAL", "value": "NACIONAL"},
                        {"label": "ANTIOQUIA", "value": "ANTIOQUIA"},
                        {"label": "ATLANTICO", "value": "ATLANTICO"},
                        {"label": "BOGOTA D.C.", "value": "BOGOTA D.C."},
                        {"label": "BOLIVAR", "value": "BOLIVAR"},
                        {"label": "BOYACA", "value": "BOYACA"},
                        {"label": "CAQUETA", "value": "CAQUETA"},
                        {"label": "CASANARE", "value": "CASANARE"},
                        {"label": "CALDAS", "value": "CALDAS"},
                        {"label": "CAUCA", "value": "CAUCA"},
                        {"label": "CESAR", "value": "CESAR"},
                        {"label": "CUNDINAMARCA", "value": "CUNDINAMARCA"},
                        {"label": "HUILA", "value": "HUILA"},
                        {"label": "MAGDALENA", "value": "MAGDALENA"},
                        {"label": "META", "value": "META"},
                        {"label": "NARIÑO", "value": "NARIÑO"},
                        {"label": "NORTE DE SANTANDER", "value": "NORTE DE SANTANDER"},
                        {"label": "QUINDIO", "value": "QUINDIO"},
                        {"label": "PUTUMAYO", "value": "PUTUMAYO"},
                        {"label": "RISARALDA", "value": "RISARALDA"},
                        {"label": "SANTANDER", "value": "SANTANDER"},
                        {"label": "SUCRE", "value": "SUCRE"},
                        {"label": "TOLIMA", "value": "TOLIMA"},
                        {"label": "VALLE DEL CAUCA", "value": "VALLE DEL CAUCA"},
                        {"label": "NO DISPONIBLE", "value": "NO DISPONIBLE"},
                    ],
                    value = [],
                    multi = True,
                    #style={'width': "50%"},
                    placeholder="Select a region",
                ),
            ])
        ]),
        dbc.Row([
            dbc.Col([dbc.Alert("Visualice aquí información referente a la cantidad de afiliciones mensuales", color="light"),
                    dbc.Card([ #html.H2("Beneficiarios mensual", className="card-title"),
                    dcc.Graph(id='graph1_status', figure={})
                ]),
            ]),
            dbc.Col([
                    dbc.Card([dbc.Alert("Visualice aquí información referente al crecimiento de la población, 'Población Activa' mensualmente ", color="light"),
                    dcc.Graph(id='graph2_status', figure={}),
                ])
            ])
        ]),
        dbc.Row([
            dbc.Col([
                    dbc.Card([dbc.Alert("Visualice aquí información referente a la cantidad de fallecimientos", color="light"),
                    dcc.Graph(id='graph3_status', figure={}),
                ])
            ]),
            dbc.Col([
                    dbc.Card([dbc.Alert("Visualice aquí información referente a la cantidad de retiros", color="light"),
                    dcc.Graph(id='graph4_status', figure={}),
                ]),
            ]),
        ]),
        dbc.Row([
            dbc.Col([
                    dbc.Card([dbc.Alert("Visualice aquí información referente Tasa de Mortalidad de La Ascensión", color="light"),
                    dcc.Graph(id='graph5_status', figure={}),
                ])
            ],
            width={"size": 8, "offset": 2},
            ) 
        ])
    ]

def build_tab_business_info_deaths():
    return [ html.Br(),
        
        dbc.Row([
        dbc.Alert("Consulte Aquí información referente a los registros del consolidado de fallecimientos, con información por rango de edades, año, parentescos, UEN y sus relaciones con el total de fallecidos registrados desde 2016  hasta la actualidad  ", color="primary",className='alert w-60'),
        dbc.Col([
            html.Br(),
            dbc.Alert("Aquí podras observar el total de fallecimiento para cada  causa de fallecimiento (total de registros)", color="light",className='alert w-60'),
            dbc.Card([ 
                dcc.Graph(id='graph1_predicion_mortalidad', figure=josegraphs.barplot_causas()),
            ],
            body=True,
            color='light',
            
            ),
        ],width={"size": 4.4},),
        dbc.Col([
            html.Br(),
            dbc.Alert("Aquí podras observar el total de  fallecimientos para cada año (total de registros)", color="light"),
            dbc.Card([ 
                dcc.Graph(id='graph2_predicion_mortalidad', figure=josegraphs.barplot_fallecimientos_anio()),
            ],
            body=True,
            color='light'),
        ]),
        dbc.Col([
            html.Br(),
            dbc.Alert("Aquí podras observar el porcentaje de fallecidos por rango de edades siguiendo el rango definido por el DANE", color="light"),
            dbc.Card([
                dcc.Graph(id='graph5_predicion_mortalidad', figure=josegraphs.pie_rango_edad()),
            ],
            body=True,
            color='light'),
        ]),
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Alert("Aquí podras observar la edad de fallecimiento contra las causas de fallecimiento (total de registrados)", color="light"),
            dbc.Card([
                dcc.Graph(id='graph3_predicion_mortalidad', figure=josegraphs.boxplot_Causas_edad()),
            ],
            body=True,
            color='light'),
        ]),
        dbc.Col([
            dbc.Alert("Aquí podras observar la edad de fallecimiento contra el UEN afiliado (total de registrados)", color="light"),
            dbc.Card([
            dcc.Graph(id='graph5_predicion_mortalidad', figure=josegraphs.boxplot_UEN_edad()),
            ],
            body=True,
            color='light'),
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Alert("Aquí podras observar la edad de fallecimiento contra el parentesco del fallecido (total de registrados)", color="light"),
            dbc.Card([
                dcc.Graph(id='graph4_predicion_mortalidad', figure=josegraphs.boxplot_parentesco_edad()),
            ],
            body=True,
            color='light'),
        ])
    ]),
    ]


def build_tab_financial_info():
    return [
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dcc.Dropdown(
                        id="region_financial_info",
                        options=[
                            {"label": "NACIONAL", "value": "NACIONAL"},
                            {"label": "ANTIOQUIA", "value": "ANTIOQUIA"},
                            {"label": "ATLANTICO", "value": "ATLANTICO"},
                            {"label": "BOGOTA D.C.", "value": "BOGOTA D.C."},
                            {"label": "HUILA", "value": "HUILA"},
                            {"label": "NARIÑO", "value": "NARIÑO"},
                            {"label": "SANTANDER", "value": "SANTANDER"},
                            {"label": "TOLIMA", "value": "TOLIMA"},
                            {"label": "VALLE DEL CAUCA", "value": "VALLE DEL CAUCA"},
                        ],
                        value = 'NACIONAL',
                        multi = False,
                        #style={'width': "50%"},
                        placeholder="Select a region",
                    ),
                ],
                body=True,
                color='light'),
            ]),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dcc.Graph(id='graph1_financial', figure={}),
                ],
                body=True,
                color='light'),
            ]),
            dbc.Col([
                dbc.Card([
                    dcc.Graph(id='graph2_financial', figure={}),
                ],
                body=True,
                color='light'
                ),
            ]),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dcc.Graph(id='graph3_financial', figure={}),
                ],
                body=True,
                color='light'
                ),
            ]),
            dbc.Col([
                dbc.Card([
                    dcc.Graph(id='graph4_financial', figure={}),
                ],
                body=True,
                color='light'
                ),
            ]),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dcc.Graph(id='graph5_financial', figure=funfin.plot_contratos_hechos_year_mes_deptoN(funfin.Conteo_Union_Contratos)),
                ],
                body=True,
                color='light'
                ),
            ]),
            dbc.Col([
                dbc.Card([
                    dcc.Graph(id='graph6_financial', figure=funfin.plot_pop_Clien_Contra_year_mes_deptoN(funfin.Conteo_Union_Contratos)),
                ],
                body=True,
                color='light'
                ),
            ]),
        ])
    ]
                