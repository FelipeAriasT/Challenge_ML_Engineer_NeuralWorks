from datetime import datetime
import pandas as pd
from utils import temporada_alta, calcular_tasa, dif_minutes, get_periodo_dia


def test_temporada_alta():
    """Function that tests the function temporada_alta. 5 test cases are used:
    - date within the high season
    - date outside the high season
    - date on the lower limit of the high season
    - date on the upper limit of the high season
    - date on the upper limit of the high season (last day of February)
    """
    fecha = '2022-12-20 12:00:00'
    resultado = temporada_alta(fecha)
    assert resultado == 1

    fecha = '2022-06-01 09:00:00'
    resultado = temporada_alta(fecha)
    assert resultado == 0

    fecha = '2022-12-15 00:00:00'
    resultado = temporada_alta(fecha)
    assert resultado == 1

    fecha = '2022-09-30 23:59:59'
    resultado = temporada_alta(fecha)
    assert resultado == 0

    fecha = '2022-03-03 12:00:00'
    resultado = temporada_alta(fecha)
    assert resultado == 0

def test_calcular_tasa():
    """Function that tests the function calcular_tasa. The test case uses a dataframe with 6 rows and 2 columns:
    - column 'columna' with 3 different values: A, B and C
    - column 'atraso_15' with 1s and 0s

    The expected result is a dataframe with 3 rows and 1 column:
    - column 'Tasa (%)' with the rate for each value of the column 'columna'
    - compare two dataframes using the function pd.testing.assert_frame_equal
    """
   
    df = pd.DataFrame({
        'columna': ['A', 'A', 'B', 'B', 'B', 'C'],
        'atraso_15': [1, 1, 1, 0, 0, 1]
    })

    resultado = calcular_tasa(df, 'columna')

    assert isinstance(resultado, pd.DataFrame)
    assert resultado.shape == (3, 1)

    resultado = resultado.sort_index()
    expected_result = pd.DataFrame({
        'Tasa (%)': [100.0,33.0, 100.0]
    }, index=['A', 'B', 'C']).sort_index()

    pd.testing.assert_frame_equal(resultado, expected_result)

def test_dif_minutes():
    """Function that tests the function dif_minutes. The test case uses a dictionary with two keys:
    - 'Fecha-O' with a date in the format 'YYYY-MM-DD HH:MM:SS' (string)
    - 'Fecha-I' with a date in the format 'YYYY-MM-DD HH:MM:SS' (string)

    The expected result is the difference in minutes between the two dates.
    """

    data = {
        'Fecha-O': '2022-01-01 12:00:00',
        'Fecha-I': '2022-01-01 10:30:00'
    }

    resultado = dif_minutes(data)

    assert resultado == 90

    data = {
        'Fecha-O': '2022-01-01 12:00:00',
        'Fecha-I': '2022-01-01 12:00:00'
    }

    resultado = dif_minutes(data)

    assert resultado == 0

def test_get_periodo_dia():
    """Function that tests the function get_periodo_dia. 6 test cases are used:
    - date within the morning period
    - date within the afternoon period
    - date within the night period
    - date on the lower limit of the night period
    - date on the upper limit of the night period
    - date on the upper limit of the night period (last day of February)
    """

    fecha = '2022-01-01 08:30:00'
    resultado = get_periodo_dia(fecha)
    assert resultado == 'mañana'

    fecha = '2022-01-01 14:45:00'
    resultado = get_periodo_dia(fecha)
    assert resultado == 'tarde'

    fecha = '2022-01-01 21:00:00'
    resultado = get_periodo_dia(fecha)
    assert resultado == 'noche'

    fecha = '2022-01-01 00:00:00'
    resultado = get_periodo_dia(fecha)
    assert resultado == 'noche'

    fecha = '2022-01-01 04:59:59'
    resultado = get_periodo_dia(fecha)
    assert resultado == 'noche'




