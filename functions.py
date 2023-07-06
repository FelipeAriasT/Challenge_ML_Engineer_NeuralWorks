import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import pickle
from pathlib import Path

def temporada_alta(fecha):
    """Función que determina si una fecha corresponde a la temporada alta o no.
    Parámetros:
    - fecha: fecha en formato 'YYYY-MM-DD HH:MM:SS'
    Retorna:
    - 1 si la fecha corresponde a la temporada alta, 0 en caso contrario
    """
    fecha_año = int(fecha.split('-')[0])
    fecha = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
    range1_min = datetime.strptime('15-Dec', '%d-%b').replace(year=fecha_año)
    range1_max = datetime.strptime('31-Dec', '%d-%b').replace(year=fecha_año)
    range2_min = datetime.strptime('1-Jan', '%d-%b').replace(year=fecha_año)
    range2_max = datetime.strptime('3-Mar', '%d-%b').replace(year=fecha_año)
    range3_min = datetime.strptime('15-Jul', '%d-%b').replace(year=fecha_año)
    range3_max = datetime.strptime('31-Jul', '%d-%b').replace(year=fecha_año)
    range4_min = datetime.strptime('11-Sep', '%d-%b').replace(year=fecha_año)
    range4_max = datetime.strptime('30-Sep', '%d-%b').replace(year=fecha_año)

    if ((fecha >= range1_min and fecha <= range1_max) or
        (fecha >= range2_min and fecha <= range2_max) or
        (fecha >= range3_min and fecha <= range3_max) or
            (fecha >= range4_min and fecha <= range4_max)):
        return 1
    else:
        return 0


def calcular_tasa(df, columna):
    """
    Calcula la tasa de atrasos para una columna de un dataframe.

    Parámetros:
    - df: dataframe con los datos
    - columna: nombre de la columna para la que se calcula la tasa

    Retorna:
    - un dataframe con la tasa de atrasos para cada valor de la columna.
    """
    dic_atrasos = {}
    for _, row in df.iterrows():
        if row['atraso_15'] == 1:
            if row[columna] not in dic_atrasos:
                dic_atrasos[row[columna]] = 1
            else:
                dic_atrasos[row[columna]] += 1
    
    total_values = df[columna].value_counts()
    
    dic_tasas = {}
    for name, total in total_values.items():
        if name in dic_atrasos:
            dic_tasas[name] = round(dic_atrasos[name]/total , 2)*100
        else:
            dic_tasas[name] = 0
            
    return pd.DataFrame.from_dict(data = dic_tasas, orient = 'index', columns = ['Tasa (%)'])


def dif_min(data):
    """Función que calcula la diferencia en minutos entre dos fechas.
    Parámetros:
    - data: diccionario con las fechas en formato 'YYYY-MM-DD HH:MM:SS'
    Retorna:
    - diferencia en minutos entre las fechas
    """
    fecha_o = datetime.strptime(data['Fecha-O'], '%Y-%m-%d %H:%M:%S')
    fecha_i = datetime.strptime(data['Fecha-I'], '%Y-%m-%d %H:%M:%S')
    dif_min = ((fecha_o - fecha_i).total_seconds()) / 60
    return dif_min


def get_periodo_dia(fecha):
    """Función que determina el periodo del día de una fecha.
    Parámetros:
    - fecha: fecha en formato 'YYYY-MM-DD HH:MM:SS'
    Retorna:
    - periodo del día de la fecha
    """
    fecha_time = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S').time()
    mañana_min = datetime.strptime("05:00", '%H:%M').time()
    mañana_max = (datetime.strptime("11:59", '%H:%M') + timedelta(seconds=59)).time()
    tarde_min = datetime.strptime("12:00", '%H:%M').time()
    tarde_max = (datetime.strptime("18:59", '%H:%M') + timedelta(seconds=59)).time()
    noche_min1 = datetime.strptime("19:00", '%H:%M').time()
    noche_max1 = (datetime.strptime("23:59", '%H:%M') + timedelta(seconds=59)).time()
    noche_min2 = datetime.strptime("00:00", '%H:%M').time()
    noche_max2 = (datetime.strptime("4:59", '%H:%M') + timedelta(seconds=59)).time()

    if (fecha_time > mañana_min and fecha_time < mañana_max):
        return 'mañana'
    elif (fecha_time > tarde_min and fecha_time < tarde_max):
        return 'tarde'
    elif ((fecha_time >= noche_min1 and fecha_time <= noche_max1) or
          (fecha_time >= noche_min2 and fecha_time <= noche_max2)):
        return 'noche'
