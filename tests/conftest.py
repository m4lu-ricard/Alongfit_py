"""Fixtures compartilhadas pelos testes do AlongFit.

O GerenciadorBanco usa o caminho padrao "alongfit.db", relativo a pasta atual.
Cada teste roda dentro de uma pasta temporaria do pytest (tmp_path), entao o
banco criado ali e descartado no fim e o alongfit.db de quem roda os testes
nunca e tocado.
"""
import pytest

from controller.gerenciador_banco import GerenciadorBanco


class JanelaFalsa:
    """Substitui a janela Tkinter nos testes do cronometro.

    Guarda os agendamentos feitos com after() em vez de executa-los, para que o
    teste controle cada segundo do cronometro.
    """

    def __init__(self):
        self.config_sons = False
        self.config_hidratacao = False
        self.agendados = {}
        self._contador = 0

    def after(self, milissegundos, funcao):
        self._contador += 1
        identificador = f"after#{self._contador}"
        self.agendados[identificador] = (milissegundos, funcao)
        return identificador

    def after_cancel(self, identificador):
        self.agendados.pop(identificador, None)


@pytest.fixture
def pasta_temporaria(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    return tmp_path


@pytest.fixture
def banco(pasta_temporaria):
    return GerenciadorBanco()


@pytest.fixture
def janela():
    return JanelaFalsa()
