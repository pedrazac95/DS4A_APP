from pandas import DataFrame
import plotly.express as px  

def graph1 (df: DataFrame, filtro:list):
    df = df[df["Sucursal"].isin(filtro)]
    # Plotly Express

    fig = px.line(df[(df['Year_Month']!='NA')], x='Year_Month', y="Count_CCont", color='Sucursal' )

    return fig


def graph2 (df: DataFrame, filtro:list):
    fallecidos_dep =df[df['DEPARTAMENTO'].isin(filtro)]
    fal_dane_anio = fallecidos_dep.groupby(["anio", 'DEPARTAMENTO']).size().reset_index()
    fal_dane_anio.columns= ["AÑO", 'DEPARTAMENTO', "Total_fallecidos"]
    fig = px.bar(fal_dane_anio,x="AÑO",y="Total_fallecidos" , color='DEPARTAMENTO')
    return fig

def graph3 (df: DataFrame, filtro:list):
    df2 = df[df['Sucursal'].isin(filtro)]

    return px.line(df2, x='Year_Month', y="Proporcion_Siniestros",color='Sucursal', hover_name='Rango_Edad')