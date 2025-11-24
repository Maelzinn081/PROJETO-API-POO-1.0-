from abc import ABC, abstractmethod

class DispositivoMonitoramento(ABC):

    @abstractmethod
    def analisar_dado(self, valor):
        pass


class Sensor(DispositivoMonitoramento):

    def __init__(self, tipo, local):
        self.tipo = tipo
        self.local = local

    def analisar_dado(self, valor):
        return "Sem análise específica."


class SensorTemperatura(Sensor):

    def analisar_dado(self, valor):
        if valor > 40:
            return "ALERTA! Temperatura alta!"
        if valor < 0:
            return "ALERTA! Temperatura baixa!"
        return "Temperatura normal."


class SensorUmidade(Sensor):

    def analisar_dado(self, valor):
        if valor > 80:
            return "ALERTA! Umidade alta!"
        if valor < 20:
            return "ALERTA! Umidade baixa!"
        return "Umidade normal."


class SensorQualidadeAr(Sensor):

    def analisar_dado(self, valor):
        if valor > 150:
            return "ALERTA! Qualidade do ar ruim!"
        return "Qualidade do ar aceitável."
