import plotly.express as px
from dateutil.relativedelta import *




#Conteo_Union = pd.read_csv('conteo_anual.csv')

def plot_totalafiliados_year_mes_deptoN(Conteo_Union, filtro):
    """Esta función realiza la gráfica lineal temporal de la creacion de contratos (Total de población afiliada) por departamento y Nivel Nacional
        Registrados por la empresa La Ascensión S.A.  """
    Conteo_Union = Conteo_Union[Conteo_Union['Sucursal'].isin(filtro)]
    fig = px.line(Conteo_Union[(Conteo_Union['Year_Month']!='NA')], x='Year_Month', y="Count_CCont",color="Sucursal")
    fig.update_layout(
        margin={"r":0,"l":0,"b":0},
        #title="Plot Title",
        xaxis_title=None,
        yaxis_title="Cantidad de Afiliados",
        #legend_title="Ubicación Sucursal",
        legend_title=None,
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.1,
            xanchor="right",
            x=1
        ),
    )
    
    return fig



def plot_retiros_year_mes_deptoN(Conteo_Union, filtro):
    """Esta función realiza la gráfica lineal temporal de los retiros por departamento y Nivel Nacional
        Registrados por la empresa La Ascensión S.A.  """
    Conteo_Union = Conteo_Union[Conteo_Union['Sucursal'].isin(filtro)]
    fig = px.line(Conteo_Union[(Conteo_Union['Year_Month']!='NA')], x='Year_Month', y="Pop_Actual",color="Sucursal")
    fig.update_layout(
        margin={"r":0,"l":0,"b":0},
        #title="Plot Title",
        xaxis_title=None,
        yaxis_title="Población",
        legend_title=None,
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.1,
            xanchor="right",
            x=1
        ),
    )
    return fig

def plot_siniestros_year_mes_deptoN(Conteo_Union, filtro):
    """Esta función realiza la gráfica lineal temporal de los siniestros(Muertes) por departamento y Nivel Nacional
        Registrados por la empresa La Ascensión S.A.  """
    Conteo_Union = Conteo_Union[Conteo_Union['Sucursal'].isin(filtro)]
    fig = px.line(Conteo_Union[(Conteo_Union['Year_Month']!='NA')], x='Year_Month', y="Count_Sin",color="Sucursal")
    fig.update_layout(
        margin={"r":0,"l":0,"b":0},
        #title="Plot Title",
        xaxis_title=None,
        yaxis_title="Cantidad de Fallecimientos",
        legend_title=None,
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.1,
            xanchor="right",
            x=1
        ),
    )
    return fig

def plot_PobActual_year_mes_deptoN(Conteo_Union, filtro):
    """Esta función realiza la gráfica lineal temporal de la población actual quitando personas retiradas y muertas por departamento y Nivel Nacional
        Registrados por la empresa La Ascensión S.A.  """
    Conteo_Union = Conteo_Union[Conteo_Union['Sucursal'].isin(filtro)]
    fig = px.line(Conteo_Union[(Conteo_Union['Year_Month']!='NA')], x='Year_Month', y="Count_Ret",color="Sucursal")
    fig.update_layout(
        margin={"r":0,"l":0,"b":0},
        #title="Plot Title",
        xaxis_title=None,
        yaxis_title="Cantidad de Retiros",
        legend_title=None,
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.1,
            xanchor="right",
            x=1
        ),
    )
    return fig

def plot_popSiniestros_year_mes_deptoN(Conteo_Union, filtro):
    """Esta función realiza la gráfica lineal temporal de la población actual quitando personas retiradas y muertas por departamento y Nivel Nacional
        Registrados por la empresa La Ascensión S.A.  """
    Conteo_Union = Conteo_Union[Conteo_Union['Sucursal'].isin(filtro)]
    fig = px.line(Conteo_Union[(Conteo_Union['Year_Month']!='NA')], x='Year_Month', y="Proporcion_Siniestros",color="Sucursal")
    fig.update_layout(
        margin={"r":0,"l":0,"b":0},
        #title="Tasa de Mortalidad La Ascensión",
        xaxis_title=None,
        yaxis_title="% de fallecimientos",
        legend_title=None,
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.1,
            xanchor="right",
            x=1
        ),
    )
    return fig