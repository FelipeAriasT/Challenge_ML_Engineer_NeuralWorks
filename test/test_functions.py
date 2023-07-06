from functions import *
from datetime import datetime
import pandas as pd


def test_temporada_alta():
    # Caso de prueba: fecha dentro de la temporada alta
    fecha = '2022-12-20 12:00:00'
    resultado = temporada_alta(fecha)
    assert resultado == 1

    # Caso de prueba: fecha fuera de la temporada alta
    fecha = '2022-06-01 09:00:00'
    resultado = temporada_alta(fecha)
    assert resultado == 0

    # Caso de prueba: fecha en el límite inferior de la temporada alta
    fecha = '2022-12-15 00:00:00'
    resultado = temporada_alta(fecha)
    assert resultado == 1

    # Caso de prueba: fecha en el límite superior de la temporada alta
    fecha = '2022-09-30 23:59:59'
    resultado = temporada_alta(fecha)
    assert resultado == 0

    # Caso de prueba: fecha en el límite superior de la temporada alta (último día de febrero)
    fecha = '2022-03-03 12:00:00'
    resultado = temporada_alta(fecha)
    assert resultado == 0


def test_calcular_tasa():
    # Datos de prueba
    df = pd.DataFrame({
        'columna': ['A', 'A', 'B', 'B', 'B', 'C'],
        'atraso_15': [1, 1, 1, 0, 0, 1]
    })

    # Calcular la tasa para la columna 'columna'
    resultado = calcular_tasa(df, 'columna')

    # Verificar el tipo y tamaño del resultado
    assert isinstance(resultado, pd.DataFrame)
    assert resultado.shape == (3, 1)

    # Verificar los valores de la tasa calculada
    resultado = resultado.sort_index()
    expected_result = pd.DataFrame({
        'Tasa (%)': [100.0,33.0, 100.0]
    }, index=['A', 'B', 'C']).sort_index()

    pd.testing.assert_frame_equal(resultado, expected_result)

def test_dif_min():
    # Datos de prueba
    data = {
        'Fecha-O': '2022-01-01 12:00:00',
        'Fecha-I': '2022-01-01 10:30:00'
    }

    # Calcular la diferencia en minutos
    resultado = dif_min(data)

    # Verificar el resultado esperado
    assert resultado == 90

    # Caso de prueba con fechas iguales
    data = {
        'Fecha-O': '2022-01-01 12:00:00',
        'Fecha-I': '2022-01-01 12:00:00'
    }

    resultado = dif_min(data)

    # Verificar que la diferencia sea cero
    assert resultado == 0


def test_get_periodo_dia():
    # Caso de prueba: fecha en el período de la mañana
    fecha = '2022-01-01 08:30:00'
    resultado = get_periodo_dia(fecha)
    assert resultado == 'mañana'

    # Caso de prueba: fecha en el período de la tarde
    fecha = '2022-01-01 14:45:00'
    resultado = get_periodo_dia(fecha)
    assert resultado == 'tarde'

    # Caso de prueba: fecha en el período de la noche
    fecha = '2022-01-01 21:00:00'
    resultado = get_periodo_dia(fecha)
    assert resultado == 'noche'

    # Caso de prueba: fecha en el límite inferior del período de la noche
    fecha = '2022-01-01 00:00:00'
    resultado = get_periodo_dia(fecha)
    assert resultado == 'noche'

    # Caso de prueba: fecha en el límite superior del período de la noche
    fecha = '2022-01-01 04:59:59'
    resultado = get_periodo_dia(fecha)
    assert resultado == 'noche'




