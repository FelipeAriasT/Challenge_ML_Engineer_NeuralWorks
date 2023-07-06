import pickle
from typing import List

import pandas as pd
import yaml
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import uvicorn


# importamos la configuracion general
with open('config/config.yaml') as file:
    config = yaml.safe_load(file)


# cargamos el modelo seleccionado
model = pickle.load(
    open(f"{config['model_directory']}{config['model_name']}", "rb"))
features_name = config['features_name']

# hacer de manera mas general con features_in?


class Vuelo(BaseModel):
    OPERA_Aerolineas_Argentinas: bool
    OPERA_Aeromexico: bool
    OPERA_Air_Canada: bool
    OPERA_Air_France: bool
    OPERA_Alitalia: bool
    OPERA_American_Airlines: bool
    OPERA_Austral: bool
    OPERA_Avianca: bool
    OPERA_British_Airways: bool
    OPERA_Copa_Air: bool
    OPERA_Delta_Air: bool
    OPERA_Gol_Trans: bool
    OPERA_Grupo_LATAM: bool
    OPERA_Iberia: bool
    OPERA_JetSmart_SPA: bool
    OPERA_K_L_M: bool
    OPERA_Lacsa: bool
    OPERA_Latin_American_Wings: bool
    OPERA_Oceanair_Linhas_Aereas: bool
    OPERA_Plus_Ultra_Lineas_Aereas: bool
    OPERA_Qantas_Airways: bool
    OPERA_Sky_Airline: bool
    OPERA_United_Airlines: bool
    TIPOVUELO_I: bool
    TIPOVUELO_N: bool
    MES_1: bool
    MES_2: bool
    MES_3: bool
    MES_4: bool
    MES_5: bool
    MES_6: bool
    MES_7: bool
    MES_8: bool
    MES_9: bool
    MES_10: bool
    MES_11: bool
    MES_12: bool


class ListaVuelos(BaseModel):
    vuelos: List[Vuelo]


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hola NeuralWorks!"}


@app.post("/predict", response_model=List)
async def predict_post(data: ListaVuelos):

    # data=json.loads(data)
    # re-estructurar datos de la lista de vuelos para que funcione el modelo
    # elegido
    df_api = pd.DataFrame(jsonable_encoder(data.vuelos))
    df_api.columns = features_name
    pred = list(model.predict(df_api))
    return [p.item() for p in pred]


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
