import pandas as pd
import plotly.express as px

#### Dataset de fallecidos organizado ####### 

df_personas = pd.read_csv('data/df_personas.csv')

def barplot_causas():
    Causas = df_personas.groupby('Causa Fallecimiento').size().reset_index()
    Causas.columns = ["CAUSAS","Total fallecimientos"]
    fig = px.bar(Causas,x="CAUSAS",y="Total fallecimientos")
    fig.update_layout(margin={"r":0,"l":0,"b":0},  xaxis_title="Causas de fallecimiento")
    return fig 

def barplot_fallecimientos_anio(): 
    YEAR = df_personas.groupby("Anio").size().reset_index()
    YEAR.columns = ["YEAR","Total fallecimientos"]
    fig = px.bar(YEAR,x="YEAR",y="Total fallecimientos")
    fig.update_layout(margin={"r":0,"l":0,"b":0},  xaxis_title="")
    return fig

def boxplot_Causas_edad(): 
    fig = px.box(df_personas,x="Causa Fallecimiento", y="Edad")
    fig.update_layout(margin={"r":0,"l":0,"b":0},  xaxis_title="Causas de fallecimiento")
    return fig 

def boxplot_parentesco_edad(): 
    fig = px.box(df_personas, x="Parentesco", y="Edad")
    fig.update_layout(margin={"r":0,"l":0,"b":0},  xaxis_title="Parentesco con el titular")
    return fig 

def boxplot_UEN_edad(): 
    fig = px.box(df_personas, x="UEN", y="Edad")
    fig.update_layout(margin={"r":0,"l":0,"b":0},  xaxis_title="UEN del fallecido")
    return fig 

def pie_rango_edad():
    Rango_Edades = df_personas.groupby('Rango_edad').size().reset_index()
    Rango_Edades.columns = ["Rango de Edades","Total fallecimientos"] 
    fig = px.pie(Rango_Edades,values= "Total fallecimientos", names = "Rango de Edades",hole=0.5)
    fig.update_layout(margin={"r":0,"l":0,"b":0},  xaxis_title="")
    return fig 