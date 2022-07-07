import datetime
import pandas as pd
import numpy as np
import plotly.express as px
from itertools import product

df_input_proj=pd.read_excel('data/Input.xlsx',sheet_name='Input')
df_input_proj['Date']=pd.to_datetime(df_input_proj['Date'])
df_input_proj['DEPARTAMENTO'].replace('BOGOTA', 'BOGOTA D.C.',inplace=True)
df_input_proj['DEPARTAMENTO'].replace('NARINO', 'NARIÑO',inplace=True)

df_pasado = pd.read_csv('data/data_finanzas_ascension_pasado.csv')

Conteo_Union_Contratos = pd.read_csv('data/Conteo_Contratos_Clientes_Final_Nacional_Dep.csv')

def df_finanzas_mens(df_input_proj,delta_deathrate,delta_fare,delta_cost):
    '''
    Función para hacer todo el calculo de costos ingresos y demás
    '''
    list_sucursales = pd.DataFrame({'Sucursales':df_input_proj['DEPARTAMENTO'].unique()})
    #Historical constants

    #Inflation projection by Bancolombia for 2021,2022,2023,2024,2025 and 2026 respectively
    #inflation=[0.0562,0.0752,0.0407,0.0365,0.0354,0.0325]
    #Sales expenses according with historical data salesexpenses/income 
    sales_expenses_incomeproportion= 0.2829
    #Operative expenses income proportion
    Operative_expenses_incomeproportion=0.1460
    #Other sources of income 
    Other_income=-0.01
    #Average revenue per main subscriber
    subscription_fare=19038.8024
    #Average death costs
    death_cost= 2165147
    #Titular per beneficiaries 
    titularbeneficiaries=1/6

    ''' 
        Projection will generetate the projections output
        inputs:
            death_rate= death rate vector for year
            customers= cuantity of annually new customers
        
        Output: the different lines of the profit and losses statement to reach the operative revenue 
    '''

    #Constants
    ConvertMillion=0.000001


    #variables
    delta_deathrate=delta_deathrate
    delta_fare=delta_fare
    delta_cost=delta_cost

    def projection (death_rate,customers):

        income_pry=[]
        cost_pry=[]
        sales_exp_pry=[]
        operative_exp_pry=[]

        #Income estimation
        temp = subscription_fare*(1+delta_fare)
        for x in customers:
            income_pry.concat((x * titularbeneficiaries * temp) *(1+Other_income)*ConvertMillion)
        
        #Costs estimation 
        w=0
        temp2=death_cost*(1+delta_cost)
        for x in death_rate:
            cost_pry.concat(temp2*(x*(1+delta_deathrate))*customers[w]*ConvertMillion)
            w=w+1

        #sales & operative expenses estimation & Operative expenses estimation 
        z=0
        while z < len(income_pry):
            sales_exp_pry.concat(income_pry[z]*sales_expenses_incomeproportion)
            operative_exp_pry.concat(income_pry[z]*Operative_expenses_incomeproportion)
            z=z+1

        return (income_pry, cost_pry, sales_exp_pry, operative_exp_pry)


    df_graph = pd.DataFrame()
    for i in list_sucursales['Sucursales']:
        DataMerge=pd.DataFrame(product([i], df_input_proj[df_input_proj['DEPARTAMENTO']== i]['Date']),columns=['Sucursal','Fechas'])
        DataMerge['Date_year']= DataMerge['Fechas'].dt.year
        respuesta=projection(np.array(df_input_proj[df_input_proj['DEPARTAMENTO']== i]['DeathRate']),np.array(df_input_proj[df_input_proj['DEPARTAMENTO']== i]['Beneficiarios']))
        df = pd.DataFrame({'Ingresos': respuesta[0], 'Costos': respuesta[1],'Gastos de ventas': respuesta[2], 'Gastos operativos': respuesta[3]})
        DataMerge=pd.concat([DataMerge,df], axis=1)
        df_graph=df_graph.concat(DataMerge)
    df_graph['Utilidad operativa']=df_graph['Ingresos']-df_graph['Costos']-df_graph['Gastos de ventas']-df_graph['Gastos operativos']
    df_graph['Margen operativo']=df_graph['Utilidad operativa']/df_graph['Ingresos']

    return df_graph

def plot_finz_mens(df_input_proj,delta_deathrate,delta_fare,delta_cost,ubica):
    df_graph_r = df_finanzas_mens(df_input_proj,delta_deathrate,delta_fare,delta_cost)
    pop_predicted_Nac_dep_month = pd.melt(df_graph_r.drop(columns=['Date_year','Ingresos','Margen operativo']), id_vars=['Sucursal','Fechas'],var_name='Finanzas', value_name = "COP millones")
    fig = px.bar(pop_predicted_Nac_dep_month[pop_predicted_Nac_dep_month['Sucursal']==ubica], x='Fechas', y='COP millones', color="Finanzas",category_orders={"Finanzas": ["Costos", "Gastos de ventas", "Gastos operativos", "Utilidad operativa"]},hover_name='Finanzas')
    fig.update_layout(
    #title="Contract Behavior",
    xaxis_title=None,
    yaxis_title='COP millones',
    legend_title=None,
    legend=dict(
    orientation="h",
    yanchor="top",
    y=-0.1,
    xanchor="right",
    x=1
    ))
   
    
    return fig

def plot_finz_mens_line(df_input_proj,delta_deathrate,delta_fare,delta_cost,ubica):
    df_graph_r = df_finanzas_mens(df_input_proj,delta_deathrate,delta_fare,delta_cost)
    fig = px.line(df_graph_r[df_graph_r['Sucursal'].isin(ubica)], x='Fechas', y='Margen operativo', color="Sucursal",hover_name='Sucursal')
    fig.update_layout(
    #title="Contract Behavior",
    xaxis_title=None,
    yaxis_title="Margen operativo (%)",
    legend_title=None,
    legend=dict(
    orientation="h",
    yanchor="top",
    y=-0.1,
    xanchor="right",
    x=1
    ))
    return fig

def plot_finz_anual(df_input_proj,delta_deathrate,delta_fare,delta_cost,ubica):
    df_graph_r = df_finanzas_mens(df_input_proj,delta_deathrate,delta_fare,delta_cost)
    df_graph_annual=df_graph_r[['Sucursal','Date_year','Ingresos','Costos','Gastos de ventas','Gastos operativos']].groupby(by=['Sucursal','Date_year']).sum().reset_index()
    df_graph_annual['Utilidad operativa']=df_graph_annual['Ingresos']-df_graph_annual['Costos']-df_graph_annual['Gastos de ventas']-df_graph_annual['Gastos operativos']

    #df_pasado['Utilidad operativa']=df_pasado['Ingresos']-df_pasado['Costos']-df_pasado['Gastos de ventas']-df_pasado['Gastos operativos']
    #df_graph_annual=pd.concat([df_pasado,df_graph_annual],ignore_index=True)
    df_graph_annual['Margen operativo']=df_graph_annual['Utilidad operativa']/df_graph_annual['Ingresos']

    pop_predicted_Nac = pd.melt(df_graph_annual.drop(columns=['Ingresos','Margen operativo']), id_vars=['Sucursal','Date_year'],var_name='Finanzas', value_name = "COP millones")
    fig = px.bar(pop_predicted_Nac[pop_predicted_Nac['Sucursal']==ubica], x='Date_year', y='COP millones', color="Finanzas",category_orders={"Finanzas": ["Costos", "Gastos ventas", "Gastos operativos", "Margen operativo"]},hover_name='Finanzas')    
    fig.update_layout(
    #title="Contract Behavior",
    xaxis_title=None,
    yaxis_title='COP millones',
    legend_title=None,
    legend=dict(
    orientation="h",
    yanchor="top",
    y=-0.1,
    xanchor="right",
    x=1
    ))
    return fig

def plot_finz_anual_line(df_input_proj,delta_deathrate,delta_fare,delta_cost,ubica):
    df_graph_r = df_finanzas_mens(df_input_proj,delta_deathrate,delta_fare,delta_cost)
    df_graph_annual=df_graph_r[['Sucursal','Date_year','Ingresos','Costos','Gastos de ventas','Gastos operativos']].groupby(by=['Sucursal','Date_year']).sum().reset_index()
    df_graph_annual['Utilidad operativa']=df_graph_annual['Ingresos']-df_graph_annual['Costos']-df_graph_annual['Gastos de ventas']-df_graph_annual['Gastos operativos']

    #df_pasado['Utilidad operativa']=df_pasado['Ingresos']-df_pasado['Costos']-df_pasado['Gastos de ventas']-df_pasado['Gastos operativos']
    #df_graph_annual=pd.concat([df_pasado,df_graph_annual],ignore_index=True)
    df_graph_annual['Margen operativo']=df_graph_annual['Utilidad operativa']/df_graph_annual['Ingresos']
       
    fig = px.line(df_graph_annual[df_graph_annual['Sucursal'].isin(ubica)], x='Date_year', y='Margen operativo', color="Sucursal",hover_name='Sucursal')
    fig.update_layout(
    #title="Contract Behavior",
    xaxis_title=None,
    yaxis_title="Margen operativo (%)",
    legend_title=None,
    legend=dict(
    orientation="h",
    yanchor="top",
    y=-0.1,
    xanchor="right",
    x=1
    )
    )
    return fig

#plot_finz_mens(df_input_proj,delta_deathrate=0,delta_fare=0,delta_cost=0,ubica='NACIONAL')
#plot_finz_mens_line(df_input_proj,delta_deathrate=0,delta_fare=0,delta_cost=0)
#plot_finz_anual(df_input_proj,delta_deathrate=0,delta_fare=0,delta_cost=0,ubica='NACIONAL')
#plot_finz_anual_line(df_input_proj,delta_deathrate=0,delta_fare=0,delta_cost=0,ubica='NACIONAL')

def plot_contratos_hechos_year_mes_deptoN(Conteo_Union_Contratos,ubica):
    """Esta función realiza la gráfica lineal temporal de los contratos realizados mensualmente por departamento y Nivel Nacional
        Registrados por la empresa La Ascensión S.A.  """
    fig = px.line(Conteo_Union_Contratos[Conteo_Union_Contratos['Sucursal'].isin(ubica)], x='Year_Month', y="Count_Contratos",color='Sucursal', hover_name='Sucursal')
    fig.update_layout(
    #title="Contract Behavior",
    xaxis_title=None,
    yaxis_title="Número de contratos",
    legend_title=None,
    legend=dict(
    orientation="h",
    yanchor="top",
    y=-0.1,
    xanchor="right",
    x=1
    )
    )
    return fig
def plot_pop_Clien_Contra_year_mes_deptoN(Conteo_Union_Contratos,ubica):
    """Esta función realiza la gráfica lineal temporal del porncetaje de clientes afiliados por los contratos realizados por departamento y Nivel Nacional
        Registrados por la empresa La Ascensión S.A.  """
    fig = px.line(Conteo_Union_Contratos[Conteo_Union_Contratos['Sucursal'].isin(ubica)], x='Year_Month', y='Proporción Población x Contrato',color='Sucursal', hover_name='Sucursal')
    fig.update_layout(
    #title="Contract Customers",
    xaxis_title=None,
    yaxis_title="Número promedio de afiliados por contrato",
    legend_title=None,
    legend=dict(
    orientation="h",
    yanchor="top",
    y=-0.1,
    xanchor="right",
    x=1
    )
    )
    return fig

def VariacionDelta_pago(delta_fare):
    data = round(19038.8024*(1+delta_fare))
    data = 'Tarifa de suscripción definida:  $' + str(data)
    return data

def VariacionDelta_servicio(delta_fare):
    data = round(2165147*(1+delta_fare))
    data = 'Costo del servicio exequial definido:  $' + str(data)
    return data