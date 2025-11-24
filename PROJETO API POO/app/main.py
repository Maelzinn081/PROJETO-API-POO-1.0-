# Link da API: http://127.0.0.1:8000/docs#/default/registrar_leitura_sensores__id__registrar_post
# Estou trabalhando para solucionar este erro.
# API REST COM ARQUITETURA 3 CAMADAS.

# ..> Controllers
# ..> Service
# ..> Models
# uvicorn main:app  --reload//para executar a API
# cd app // para acessar a pasta app
# -------------------------------------------------------

# AONDE O CÓDIGO DE FATO ESTÁ INICIANDO O BANCO? (BANCO DE DADOS)

# --------------------------------------------------------

from fastapi import FastAPI
from app.controllers.sensor_controller import router

app = FastAPI()

app.include_router(router)

