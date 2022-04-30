
from  InterpretationCSV import df
import numpy as np
import pandas as pd
from scipy import stats


def calculate_statistics(df):
    arr = set(np.array(df['ccaa_iso']))
    df_agrupado=df.groupby('ccaa_iso', as_index=False).sum()
    maximo =df_agrupado['num_casos'].max()
    minimo =df_agrupado['num_casos'].min()

    df_max=df_agrupado.loc[df_agrupado['num_casos'] == maximo]

    num_casos_prueba_ag= df_max['num_casos_prueba_ag']
    num_casos_prueba_elisa= df_max['num_casos_prueba_elisa']
    num_casos_prueba_desconocida=df_max['num_casos_prueba_desconocida']
    num_casos_prueba_pcr=df_max['num_casos_prueba_pcr']


    df_min=df_agrupado.loc[df_agrupado['num_casos'] == minimo]

    arr_aux=np.array(df['num_casos'])

    # Media Aritmetica
    media_aritmetica = np.mean((arr_aux)) 

    # Desviación típica
    des_tipica= np.std(arr_aux)

    # varianza
    varianza = np.var(arr_aux) 

    #moda
    moda =stats.mode(df['ccaa_iso'])
    #print(df_agrupado)

    respuesta = pd.DataFrame({
        'Máxima provincia contagiada': [df_max['ccaa_iso'].values[0]],
        'Cantidad contagiados': [maximo],
        'Mínima provincia contagiada': [df_min['ccaa_iso'].values[0]],
        'Cantidad mínima': [minimo],
        'Media aritmética': [media_aritmetica],
        'Desviación típica': [des_tipica],
        'Varianza': [varianza],
        'Moda provincia': [moda.mode[0]],
        'Moda cantidad': [moda.count[0]],
        
        })
        
    #respuesta.to_excel('covid_project/results/covid_statistics.xlsx')
    respuesta= (np.array(respuesta))
    #print(respuesta)
    return(respuesta)



