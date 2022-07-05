import numpy                 as np
import pandas                as pd
import plotly.express as px
from datetime import datetime
import statsmodels.formula.api as smf
import joblib

 
#load data
#model_benef = joblib.load('model_pred_benf.data')


def plot_beneficiarios_deptos (df:pd.DataFrame):

    """Esta función realiza la gráfica lineal temporal de la tasa de mortalidad por departamento 
        Registrados por la empresa La Ascensión S.A.  """

    fig = px.line(df, x='Year_Month', y="Proporcion_Siniestros",color='Sucursal', hover_name='Rango_Edad', line_group="Rango_Edad")

    return fig

def modelo_beneficiarios (df:pd.DataFrame ,Valor_Mensual, edad_aprox, Sexo, Nombre_UEN, Sucursal):
    
    """ Modelo para estimar la cantidad de beneficiarios que se añadirian en un contrato para un cliente dependiendo del valor mensual que pagara, la
    edad aproximada de la persona, el sexo, nomre
        """

    df_prediccion_benef = df.copy()
    df_prediccion_benef.loc[df_prediccion_benef['Valor_Mensual']==0,'Valor_Mensual']=Valor_Mensual
    df_prediccion_benef.loc[df_prediccion_benef['edad_aprox']==0,'edad_aprox']=edad_aprox
    df_prediccion_benef.loc[df_prediccion_benef['Sexo_{}'.format(Sexo)]==0,'Sexo_{}'.format(Sexo)]=1
    df_prediccion_benef.loc[df_prediccion_benef['Nombre_UEN_{}'.format(Nombre_UEN)]==0,'Nombre_UEN_{}'.format(Nombre_UEN)]=1
    df_prediccion_benef.loc[df_prediccion_benef['Sucursal_{}'.format(Sucursal)]==0,'Sucursal_{}'.format(Sucursal)]=1

    #resultado = model_benef.predict(df_prediccion_benef)

    return df_prediccion_benef

def grafica_colombia (df:pd.DataFrame, geojson):
    fig = px.choropleth_mapbox(df, geojson=geojson, locations='DEPARTAMENTO', color='cant_benef',                       
                           mapbox_style="carto-positron",
                           zoom=4, center = {"lat": 4, "lon": -72},
                           labels={'COUNT':'Deaths Counts'},
                           width = 1000,
                           height = 500,
                           color_continuous_scale="jet"
                          )
    #fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig