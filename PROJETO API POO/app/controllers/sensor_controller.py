from fastapi import APIRouter
from ..services.sensor_service import ( # <-- Use '..' para indicar o nível superior (a pasta 'app')
    service_criar_sensor,
    service_registrar_leitura,
    service_listar_sensores,
    service_relatorio
)

router = APIRouter()

@router.get("/")
def inicio():
    return {"Mensagem": "API FUNCIONANDO! Use /docs para testar."}


@router.post("/sensores")
def criar_sensor(tipo: str, local: str):
    sensor_id = service_criar_sensor(tipo, local)
    return {"mensagem": "Sensor criado!", "id": sensor_id}


@router.post("/sensores/{id}/registrar")
def registrar(id: int, valor: float):
    alerta, erro = service_registrar_leitura(id, valor)

    if erro:
        return {"erro": erro}

    return {"mensagem": "Leitura registrada!", "valor": valor, "alerta": alerta}


@router.get("/sensores")
def listar():
    return service_listar_sensores()


@router.get("/relatorio")
def relatorio():
    return service_relatorio()
