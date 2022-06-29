
import pandas as pd
import numpy as np
import plotly.express as px
import statsmodels.formula.api as smf

######## LECTURA DE LOS ARCHIVOS DE POBLACIÓN Y PIB PER CAPITA POR DEPARTAMENTOS ANUALES ########## 


poblacion_N = pd.read_excel('data/poblacion_por_depto_2015_2024.xlsx') #población nacional con sus proyecciones hasta 2024  
PIB_depto = pd.read_excel('data/PIB_depto_2015_2022.xlsx') #PIB por departamento y por año 
fallecidos_dane = pd.read_csv('data/Fallecimientos_por_depto_DANE_2015_2021_7_deptos.csv')





def consulta_PIB(depto): 
    
    """ Esta función consulta los valores anuales del PIB per capita (PIB por habitante)  
       en el dataset PIB_depto para el departamento escogido 
       Entrada: Departamento -> string 
       Salida: Dataset filtrado por el departamento con  la columna "AÑO" y "PIB_per_capita
       
    """
    
    PIB_depto_1 = PIB_depto[PIB_depto["DEPARTAMENTO"]==depto]
    PIB_depto_1 = PIB_depto_1.transpose()

    PIB_depto_1 = PIB_depto_1.drop(['Unnamed: 0','Unnamed: 0.1',"DEPARTAMENTO"],axis=0).reset_index()
    PIB_depto_1.columns = ["AÑO","PIB_per_capita"]
    PIB_depto_1 = PIB_depto_1.astype('int')
    
    return PIB_depto_1

def consulta_poblacion(Rango_edad,depto):
    
    """ Esta función consulta los valores anules de la población registrada y proyecciones realizada por el DANE, la cual  
       se encuentra en el dataset poblacion_N para el departamento escogido y un rango de edad en particular;
       si el rango de edad es "Total", se toma toda la población en general. 
       
       Entrada: Departamento -> string ; Rango_edad -> string
       Salida: Dataset filtrado por el departamento con  la columna "AÑO" y "PIB_per_capita
       """
    poblacion_depto = poblacion_N[poblacion_N["DEPARTAMENTO"]==depto]
    poblacion_depto_edad = poblacion_depto[["AÑO",Rango_edad]]
    
    return poblacion_depto_edad
    
def consulta(depto,Rango_edad="Total"): 
    
    """ Esta función consulta los fallecidos anules de la población registrada por el DANE ( la cual se encuentra
       en el dataset poblacion_N) para el departamento escogido y un rango de edad en particular; si el rango de edad 
       es "Total", se toma toda la población en general. 
       
       Adicionalmente, toma los dataset de las funciones de población y PIB per capita, con el fin de realizar 
       el dataset necesario para realizar la regresión lineal 
       
       Entrada: Departamento -> string ; Rango_edad -> string
       Salida: Dataset filtrado por el departamento con  la columna "AÑO" , "Rango edad", 
       "total_fallecidos","PIB_per_capita", "Tasa de mortalidad"
       
       Nota: La columna "Rango_edad" tendrá el nombre del rango escogido, y contiene la población del departamento 
       para ese rango de edad 
       
    """  
    if Rango_edad == "Total": 
        fallecidos_depto = fallecidos_dane[fallecidos_dane['DEPARTAMENTO']==depto]
        
    else: 
        fallecidos_depto = fallecidos_dane[(fallecidos_dane['DEPARTAMENTO']==depto)  & 
                                    (fallecidos_dane['Rango Edad']==Rango_edad)]
                                     
                                     
        
    fallecidos_anio = fallecidos_depto.groupby("anio").size().reset_index()
    fallecidos_anio.columns = ["AÑO","total_fallecidos"]
    PIB_depto_1 = consulta_PIB(depto)
    poblacion_depto_edad = consulta_poblacion(Rango_edad,depto)
    
    df_merge_1 = poblacion_depto_edad.merge(fallecidos_anio ,left_on='AÑO', right_on='AÑO',how='inner')
    df_merge = df_merge_1.merge(PIB_depto_1,on="AÑO",how= 'inner')

    #tasa de mortalidad cada 100.000 habitantes 
    df_merge["Tasa_mortalidad"] = (df_merge["total_fallecidos"]/df_merge[Rango_edad])*100000 
    
    
    return df_merge 



def predic_dane(depto,Rango_edad="Total"):

    """Esta función realiza la regresión lineal de la tasa de mortalidad para los fallecimientos anuales 
        registrados por el DANE, la formula para la regresión es : 

                    np.log(Tasa_mortalidad) ~  AÑO + I(np.log(PIB_per_capita)) +  I(np.log(PIB_per_capita)**2)

        la función toma con entrada el departamento para el cual se quiere realizar la regresión
        
        Entrada: DEPARTAMENTO -> string; Rango edad -> string 
        Salida: dataset con las columnas AÑO, Total, total_fallecidos, PIB_per_capita, Tasa_mortalidad,	Tasa_mortalidad_pred

        Nota: Total ahce referencia al total de la población del departamento 
              Tasa_mortalidad_pred hace referencia a la tsa de mortalidad predicha por la regresión lineal 
        
        """
    df_merge= consulta (depto,Rango_edad)

    formula1 = "np.log(Tasa_mortalidad) ~  AÑO + I(np.log(PIB_per_capita)) +  I(np.log(PIB_per_capita)**2)" #np.log(PIB_div)**2"#"+ np.log(PIB_per_capita)**2 "
    model_all = smf.ols(formula = formula1, 
                    data = df_merge).fit()
    y = model_all.predict(df_merge[["AÑO","PIB_per_capita"]])
    res = np.array(np.exp(y))
    df_merge["Tasa_mortalidad_pred"] = res
    df_merge
    return df_merge,model_all




def consulta_PIB_anio(depto,anio): 
    
    """ Esta función consulta los valor del PIB per capita (PIB por habitante) para un año específico  
       en el dataset PIB_depto para el departamento escogido 

       Entrada: Departamento -> string : AÑO-> int
       Salida: Dataset filtrado por el departamento con  la columna "AÑO" y "PIB_per_capita"
       
    """
    
    PIB_depto_2 = PIB_depto[PIB_depto["DEPARTAMENTO"]==depto]
    PIB_depto_2 = PIB_depto_2.transpose()

    PIB_depto_2 = PIB_depto_2.drop(['Unnamed: 0','Unnamed: 0.1',"DEPARTAMENTO"],axis=0).reset_index()
    PIB_depto_2.columns = ["AÑO","PIB_per_capita"]
   
    PIB_depto_2 = PIB_depto_2.astype('int')
    PIB_depto_2 = PIB_depto_2[PIB_depto_2["AÑO"]==anio]
    
    return PIB_depto_2


def pred_tasa_dane(depto,anio, Rango_edad="Total"):

    """Esta función predice la tasa de mortalidad para un año en específico para los datos del DANE, 
     siempre y cuando  se tenga el PIB_per_capita de ese año
     
     Entrada: DEPARTAMENTO-> String ; AÑO: int; Rango_edad-> string 
     Salida: dataframe con las columnas AÑO, PIB_per_capita, Tasa_mortalidad_pred """

    X= consulta_PIB_anio(depto,anio)
    df,model = predic_dane(depto,Rango_edad)
    del df
    prediccion_entrada = np.array(np.exp(model.predict(X[["AÑO","PIB_per_capita"]])))
    prediccion_entrada
    X["Tasa_mortalidad_pred"]= prediccion_entrada 
    return X


##### Funciones pata gráficas ########

def grafica_fallecidos_dane(depto): 

    """Esta función realiza la gráfica el hístorico total de fallecimientos regristrados por el DANE
     para un departamento en específico
     
     Entrada: DEPARTAMENTO-> string 
     
     """

    #### VISTAZO RÁPIDO DELOS FALLECIMIENTOS POR AÑO ######
    fallecidos_dep = fallecidos_dane[fallecidos_dane['DEPARTAMENTO']==depto]
    fal_dane_anio = fallecidos_dep.groupby("anio").size().reset_index()
    fal_dane_anio.columns= ["AÑO", "Total_fallecidos"]
    fig = px.bar(fal_dane_anio,x="AÑO",y="Total_fallecidos")
    return fig



def grafica_pred_dane(depto,Rango_edad="Total"):

    """Esta función realiza la gráfica lineal de la tasa de mortalidad calculada con datos del DANE 
    y los valores encontrados por la regresión lineal
    
    Entrada: DEPARTAMENTO-> string, Rango edad -> string"""


    df_d,model = predic_dane(depto,Rango_edad)
    del model 
    fig = px.line(df_d,x="AÑO",y=["Tasa_mortalidad","Tasa_mortalidad_pred"])
    fig.show()