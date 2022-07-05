import pandas as pd 
import plotly.express as px 

#ascension_mes = pd.read_csv("jose/prediccion_tasa_mes_ascension.csv")
#dane_ascension_anio = pd.read_csv("jose/prediccion_tasa_anio_dane_ascension.csv")

def lineplot_dane_anio(df, filtro):
    df2 = df.copy()
    df2= df2[df2['DATA']=='DANE']
    df3=df2[df2['DEPARTMENT'].isin(filtro)]
    fig = px.line(df3, x='YEAR', y="Death Rate",color='DEPARTMENT')
    fig.update_layout(
    margin={"r":0,"l":0,"b":0},
    title="Death Rate vs Dates (YEAR)",
    xaxis_title="Dates (YEAR)",
    yaxis_title="Death Rate ",
    legend_title="DEPARTMENT",
    legend=dict(
            x=0,
            y=1,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
    )
    )

    return fig 

def lineplot_ascension_anio(df, filtro):
    df2 = df.copy()
    df2 = df2[df2['DATA']=='LA ASCENSION']
    df3=df2[df2['DEPARTMENT'].isin(filtro)]
    fig = px.line(df3, x='YEAR', y="Death Rate",color='DEPARTMENT')
    fig.update_layout(
    margin={"r":0,"l":0,"b":0},
    title="Death Rate vs Dates (YEAR)",
    xaxis_title="Dates (YEAR)",
    yaxis_title="Death Rate ",
    legend_title="DEPARTMENT",
    legend=dict(
            x=0,
            y=1,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
    )
    )
    return fig 

def lineplot_ascension_mes(df , filtro):

    df2=df[df['DEPARTMENT'].isin(filtro)]
    fig = px.line(df2, x="Year_Month",y="Death Rate",color="DEPARTMENT")
    fig.update_layout(
    margin={"r":0,"l":0,"b":0},
    title="Death Rate vs Dates (YEAR-MONTH)",
    xaxis_title="Dates (YEAR-MONTH)",
    yaxis_title="Death Rate ",
    legend_title="DEPARTMENT",
    legend=dict(
            x=0,
            y=1,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
    )
    )
    return fig 

