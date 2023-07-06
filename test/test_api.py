from app.main import app
import pytest
from httpx import AsyncClient

#data de testeo
data={
    "vuelos": [
        {
            "OPERA_Aerolineas_Argentinas": True,
            "OPERA_Aeromexico": False,
            "OPERA_Air_Canada": True,
            "OPERA_Air_France": False,
            "OPERA_Alitalia": True,
            "OPERA_American_Airlines": False,
            "OPERA_Austral": True,
            "OPERA_Avianca": False,
            "OPERA_British_Airways": True,
            "OPERA_Copa_Air": False,
            "OPERA_Delta_Air": True,
            "OPERA_Gol_Trans": False,
            "OPERA_Grupo_LATAM": True,
            "OPERA_Iberia": False,
            "OPERA_JetSmart_SPA": True,
            "OPERA_K_L_M": False,
            "OPERA_Lacsa": True,
            "OPERA_Latin_American_Wings": False,
            "OPERA_Oceanair_Linhas_Aereas": True,
            "OPERA_Plus_Ultra_Lineas_Aereas": False,
            "OPERA_Qantas_Airways": True,
            "OPERA_Sky_Airline": False,
            "OPERA_United_Airlines": True,
            "TIPOVUELO_I": False,
            "TIPOVUELO_N": True,
            "MES_1": False,
            "MES_2": True,
            "MES_3": False,
            "MES_4": True,
            "MES_5": False,
            "MES_6": True,
            "MES_7": False,
            "MES_8": True,
            "MES_9": False,
            "MES_10": True,
            "MES_11": False,
            "MES_12": True
        },
        {
            "OPERA_Aerolineas_Argentinas": False,
            "OPERA_Aeromexico": True,
            "OPERA_Air_Canada": False,
            "OPERA_Air_France": True,
            "OPERA_Alitalia": False,
            "OPERA_American_Airlines": True,
            "OPERA_Austral": False,
            "OPERA_Avianca": True,
            "OPERA_British_Airways": False,
            "OPERA_Copa_Air": True,
            "OPERA_Delta_Air": False,
            "OPERA_Gol_Trans": True,
            "OPERA_Grupo_LATAM": False,
            "OPERA_Iberia": True,
            "OPERA_JetSmart_SPA": False,
            "OPERA_K_L_M": True,
            "OPERA_Lacsa": False,
            "OPERA_Latin_American_Wings": True,
            "OPERA_Oceanair_Linhas_Aereas": False,
            "OPERA_Plus_Ultra_Lineas_Aereas": False,
            "OPERA_Qantas_Airways": False,
            "OPERA_Sky_Airline": True,
            "OPERA_United_Airlines": False,
            "TIPOVUELO_I": True,
            "TIPOVUELO_N": False,
            "MES_1": True,
            "MES_2": False,
            "MES_3": True,
            "MES_4": False,
            "MES_5": True,
            "MES_6": False,
            "MES_7": True,
            "MES_8": False,
            "MES_9": True,
            "MES_10": False,
            "MES_11": True,
            "MES_12": False
        }
    ]
}



@pytest.mark.anyio
async def test_predict():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as client:
        response = await client.post("/predict", json=data)
        assert response.status_code == 200
        result = response.json()
        assert isinstance(result, list)
        assert result==[0,0]


