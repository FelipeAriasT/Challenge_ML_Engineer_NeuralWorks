from datetime import datetime, timedelta
import pandas as pd


def temporada_alta(fecha):
    """Function that determines if a date corresponds to the high season or not.
    Parameters:
    - date: date in format 'YYYY-MM-DD HH:MM:SS' (string)
    Returns:
    - 1 if the date corresponds to the high season, 0 otherwise (int)"""
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
    """Function that calculates the delay rate for a column of a dataframe.
    Parameters:
    - df: dataframe with the data (pandas dataframe)
    - columna: name of the column for which the rate is calculated (string)
    Returns:
    - a dataframe with the delay rate for each value of the column (pandas dataframe)"""

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

def dif_minutes(data):
    """Function that calculates the difference in minutes between two dates.
    Parameters:
    - data: dictionary with the dates in format 'YYYY-MM-DD HH:MM:SS' (string)
    Returns:
    - difference in minutes between the dates (int)
    """
    fecha_o = datetime.strptime(data['Fecha-O'], '%Y-%m-%d %H:%M:%S')
    fecha_i = datetime.strptime(data['Fecha-I'], '%Y-%m-%d %H:%M:%S')
    dif_min = ((fecha_o - fecha_i).total_seconds()) / 60
    return dif_min

def get_periodo_dia(fecha):
    """Function that determines the day period of a date.
    Parameters:
    - fecha: date in format 'YYYY-MM-DD HH:MM:SS' (string)
    Returns:
    - day period of the date (string)
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
