import plotly.express as px 

#ascension_mes = pd.read_csv("jose/prediccion_tasa_mes_ascension.csv")
#dane_ascension_anio = pd.read_csv("jose/prediccion_tasa_anio_dane_ascension.csv")

def lineplot_dane_anio(df, filtro):
    df2 = df.copy()
    df2= df2[df2['DATA']=='DANE']
    df3=df2[df2['DEPARTMENT'].isin(filtro)]
    fig = px.line(df3, x='YEAR', y="Death Rate",color='DEPARTMENT')
    #fig.update_layout(
    #margin={"r":0,"l":0,"b":0},
    #xaxis_title="",
    #yaxis_title="Tasa de mortalidad ",
    #legend_title="DEPARTAMENTO",
    #legend=dict(
    #        x=0,
    #        y=1,
    #        bgcolor='rgba(255, 255, 255, 0)',
    #        bordercolor='rgba(255, 255, 255, 0)'
    #)
    #)
    fig.update_layout(
    legend_title=None,
    xaxis_title="",
    yaxis_title="Tasa de mortalidad ",
    legend=dict(
    orientation="h",
    yanchor="top",
    y=-0.1,
    xanchor="right",
    x=1
    )
    )

    return fig 

def lineplot_ascension_anio(df, filtro):
    df2 = df.copy()
    df2 = df2[df2['DATA']=='LA ASCENSION']
    df3=df2[df2['DEPARTMENT'].isin(filtro)]
    fig = px.line(df3, x='YEAR', y="Death Rate",color='DEPARTMENT')
    #fig.update_layout(
    #margin={"r":0,"l":0,"b":0},
    #xaxis_title="",
    #yaxis_title="Tasa de mortalidad",
    #legend_title="DEPARTAMENTO",
    #legend=dict(
     #       x=0,
     #       y=1,
      #      bgcolor='rgba(255, 255, 255, 0)',
       #     bordercolor='rgba(255, 255, 255, 0)'
    #)
    #)
    fig.update_layout(
    legend_title=None,
    xaxis_title="",
    yaxis_title="Tasa de mortalidad",
    legend=dict(
    orientation="h",
    yanchor="top",
    y=-0.1,
    xanchor="right",
    x=1
    )
    )
    return fig 

def lineplot_ascension_mes(df , filtro):

    df2=df[df['DEPARTMENT'].isin(filtro)]
    fig = px.line(df2, x="Year_Month",y="Death Rate",color="DEPARTMENT")
    #fig.update_layout(
    #margin={"r":0,"l":0,"b":0},
    #xaxis_title="",
    #yaxis_title="Tasa de mortalidad",
    #legend_title="DEPARTAMENTO",
    #legend=dict(
     #       x=0,
      #      y=1,
       #     bgcolor='rgba(255, 255, 255, 0)',
        #    bordercolor='rgba(255, 255, 255, 0)'
    #)
    #)
    fig.update_layout(
    legend_title=None,
    xaxis_title="",
    yaxis_title="Tasa de mortalidad",
    legend=dict(
    orientation="h",
    yanchor="top",
    y=-0.1,
    xanchor="right",
    x=1
    )
    )
    return fig 

