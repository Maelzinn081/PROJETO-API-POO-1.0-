from models.sensor_model import (
    criar_sensor,
    buscar_sensor,
    registrar_leitura,
    listar_sensores,
    listar_leituras,
    gerar_relatorio
)

from models.sensor_classes import (
    Sensor, SensorTemperatura, SensorUmidade, SensorQualidadeAr
)

# =============================
# SERVICES
# =============================

def service_criar_sensor(tipo, local):
    return criar_sensor(tipo, local)


def service_registrar_leitura(id, valor):
    row = buscar_sensor(id)

    if row is None:
        return None, "Sensor não encontrado!"

    tipo, local = row

    # Instância correta
    if tipo == "temperatura":
        sensor = SensorTemperatura(tipo, local)
    elif tipo == "umidade":
        sensor = SensorUmidade(tipo, local)
    elif tipo == "ar":
        sensor = SensorQualidadeAr(tipo, local)
    else:
        sensor = Sensor(tipo, local)

    alerta = sensor.analisar_dado(valor)

    registrar_leitura(id, valor)

    return alerta, None


def service_listar_sensores():
    sensores = listar_sensores()

    resultado = []
    for s in sensores:
        sensor_id, tipo, local = s
        leituras = listar_leituras(sensor_id)
        media = sum(leituras) / len(leituras) if leituras else 0

        resultado.append({
            "id": sensor_id,
            "tipo": tipo,
            "local": local,
            "leituras": leituras,
            "media": media
        })

    return resultado


def service_relatorio():
    return gerar_relatorio()
