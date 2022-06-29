import numpy                 as np
import pandas                as pd
import plotly.express as px
from datetime import datetime
import statsmodels.formula.api as smf
import regresion_dane as rd 

######### Lectura del dataset ########## 

df_benef = pd.read_csv('data/Conteo_Anual_Mens_Ubic_EdadPop.csv')

def plot_siniestros_anio_mes_depto():

    """Esta función realiza la gráfica lineal temporal de la tasa de mortalidad por departamento 
        Registrados por la empresa La Ascensión S.A.  """

    fig = px.line(df_benef, x='Year_Month', y="Proporcion_Siniestros",color='Sucursal', hover_name='Rango_Edad', line_group="Rango_Edad")
    fig.show()

def proceso_datos(depto): 

    """Esta función realiza el proceso de selección, filtrado, depurado y unión de los datos necesarios 
        para crear el dataframe con el cual se realizará la regresión lineal 
        
        Entrada: DEPARTAMENTO -> string

        Salida: dataframe -> Year, Proporcion_Siniestros,AÑO,Total,total_fallecidos,PIB_per_capita,Tasa_mortalidad,
        Tasa_mortalidad_pred, Month_1, Month_2, Month_3, Month_4, Month_5, Month_6, Month_7, Month_8, Month_9,
         Month_10, Month_11, Month_12; 

                lista con las fechas -> dates
        
        """
    benf_depto = df_benef[(df_benef["Sucursal"]==depto) & (df_benef["Year"] != 2022)] 
    fallecidos_total = benf_depto.groupby(["Year","Month"])["Proporcion_Siniestros"].sum().reset_index()
    Rango_edad="Total"
    data_dane,model= rd.predic_dane(depto,Rango_edad)
    del model 
    df_merge = fallecidos_total.merge(data_dane,left_on="Year", right_on = "AÑO",how= 'inner')

    #Se eliminan los siniestros con valor de cero para evitar divisiones por cero.
    df_merge.drop(df_merge.loc[df_merge['Proporcion_Siniestros']==0].index,inplace=True) 

    #Se crea el arreglo que contiene las fechas para la graficar la serie de tiempo 
    dates = df_merge.apply(lambda r: datetime(int(r['Year']), int(r['Month']), 28) , axis=1) 
    df_merge= pd.get_dummies(df_merge,columns=["Month"])

    return df_merge,dates



def model_pred_ascension(depto):

    """
    Esta función realiza la regresión lineal de los datos filtrados de la empresa La Ascensión S.A. 
    por medio de la siguiente fórmula: 

    np.log(Proporcion_Siniestros)~ AÑO+	Tasa_mortalidad_pred+	Month_1 + Month_2 + Month_3 + Month_4 
                                   + Month_5 + Month_6 + Month_7 + Month_8	+ Month_9 + Month_10 + Month_11 
                                   +Month_12 +I(np.log(PIB_per_capita)**2) + np.log(PIB_per_capita) 
                                   + AÑO:Month_1 + AÑO:Month_2 + AÑO:Month_3 + AÑO:Month_4 + AÑO:Month_5 
                                   + AÑO:Month_6 + AÑO:Month_7 + AÑO:Month_8	+ AÑO:Month_9 + AÑO:Month_10 
                                   + AÑO:Month_11  + AÑO:Month_12

    Entrada: DEPARTAMENTO -> string
    Salida: dataframe con las columnas dates, Tasa_mortalidad, Tasa_mortalidad_prediccion
            modeloa de la regresion -> model_all 


    """
    df_mod,dates = proceso_datos(depto)
    formula1 = "np.log(Proporcion_Siniestros)~ AÑO+	Tasa_mortalidad_pred+	Month_1 + Month_2 + Month_3 + Month_4 + Month_5 + Month_6 + Month_7 + Month_8	+ Month_9 + Month_10 + Month_11  +Month_12	+I(np.log(PIB_per_capita)**2) + np.log(PIB_per_capita) + AÑO:Month_1 + AÑO:Month_2 + AÑO:Month_3 + AÑO:Month_4 + AÑO:Month_5 + AÑO:Month_6 + AÑO:Month_7 + AÑO:Month_8	+ AÑO:Month_9 + AÑO:Month_10 + AÑO:Month_11  + AÑO:Month_12 "
    #formula1 = "np.log(Proporcion_Siniestros) ~   Year_Month  + np.log(PIB_per_capita) +   I(np.log(PIB_per_capita)**2)" 
    model_all = smf.ols(formula = formula1, 
                 data = df_mod).fit()
    Y = pd.DataFrame()
    Y["dates"] = dates 
    Y["Tasa_mortalidad"] = df_mod["Proporcion_Siniestros"]
    Y["Tasa_mortalidad_prediccion"] =np.array(np.exp(model_all.fittedvalues)) 

    return Y,model_all 

def pred_ascension_mes(depto,anio_pred,mes_pred,Rango_edad="Total"): 

    """
    Esta función realiza la predicción de la tasa de mortalidad para un año y mes específico de los datos 
    registrados por la empresa La Ascensi+on S.A.

    Entrada:  DEPARTAMENTO -> string;  AÑO A PREDECIR -> int; MES A PREDECIR-> int; Rango edad-> string 
    Salida: valor de la tasa de mortalidad para el año y mes deseado 

    """
    df_pred = rd.pred_tasa_dane(depto,anio_pred, Rango_edad)
    for i in range(1,13):
        df_pred["Month_{}".format(i)] = 0 
    df_pred["Month_{}".format(mes_pred)] = 1
    Y, model_all = model_pred_ascension(depto)
    del Y 
    pred_tasa  = np.exp(model_all.predict(df_pred))/100000
    return pred_tasa

def plot_tasa_pred(depto): 

    """
    Esta función realiza la gráfica lineal temporal de la tasa de mortalidad calaculada con los datos 
    de la empresa La Ascensión S.A. y de la tasa de mortalidad calculada por la regresión lineal

    Entrada: DEPARATAMENTO -> string 

    """
    Y,model = model_pred_ascension(depto)
    del model
    fig = px.line(Y,x="dates",y=["Tasa_mortalidad","Tasa_mortalidad_prediccion"])
    fig.show()