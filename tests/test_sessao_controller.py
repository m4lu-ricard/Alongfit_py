"""Comportamento do cronometro do SessaoController.

A janela Tkinter e substituida pela JanelaFalsa (conftest.py) e o pop-up de
alongamento por um registro simples, para que o teste controle cada segundo.
Estes testes servem de rede de seguranca para a refatoracao da Issue #13.
"""
import pytest

import controller.sessao_controller as modulo_sessao
from controller.sessao_controller import SessaoController

USUARIO = 2  # nos dados iniciais, o usuario 2 tem 1 pausa e nenhum alongamento


class PopUpFalso:
    abertos = []

    def __init__(self, janela, controller, alongamento):
        PopUpFalso.abertos.append(alongamento)


@pytest.fixture
def sessao(banco, janela, monkeypatch):
    PopUpFalso.abertos = []
    monkeypatch.setattr(modulo_sessao, "PopUp", PopUpFalso)

    controlador = SessaoController(janela, USUARIO)
    tela = {}
    controlador.vincular_interface_relogio(lambda texto: tela.__setitem__("relogio", texto))
    controlador.vincular_interface_tempo_total(lambda texto: tela.__setitem__("total", texto))
    controlador.tela = tela
    return controlador


def test_configurar_sessao_define_o_primeiro_ciclo(sessao):
    sessao.configurar_sessao(horas_trabalho=1, minutes_pausa=20, identificador_dor=1)

    assert sessao.tempo_restante_segundos == 20 * 60
    assert sessao.tempo_trabalho_total_restante == 3600
    assert sessao.tela == {"relogio": "20:00", "total": "1:00:00"}


def test_ciclo_nao_passa_do_tempo_que_resta_da_jornada(sessao):
    sessao.configurar_sessao(horas_trabalho=1, minutes_pausa=90, identificador_dor=1)

    assert sessao.tempo_restante_segundos == 3600


def test_cada_segundo_desconta_do_ciclo_e_da_jornada_e_agenda_o_proximo(sessao, janela):
    sessao.configurar_sessao(horas_trabalho=1, minutes_pausa=20, identificador_dor=1)

    sessao.iniciar_temporizador()

    assert sessao.tempo_restante_segundos == 1199
    assert sessao.tempo_trabalho_total_restante == 3599
    assert sessao.tela["relogio"] == "19:59"
    assert [ms for ms, _ in janela.agendados.values()] == [1000]


def test_pausar_cancela_o_proximo_segundo(sessao, janela):
    sessao.configurar_sessao(horas_trabalho=1, minutes_pausa=20, identificador_dor=1)
    sessao.iniciar_temporizador()

    sessao.pausar_temporizador()
    sessao.executar_ciclo_temporizador()

    assert janela.agendados == {}
    assert sessao.temporizador_rodando is False
    assert sessao.tempo_restante_segundos == 1199


def test_fim_do_ciclo_abre_alongamento_e_registra_a_pausa(sessao, banco, janela):
    sessao.configurar_sessao(horas_trabalho=1, minutes_pausa=20, identificador_dor=1)
    sessao.tempo_restante_segundos = 1
    pausas_antes, concluidas_antes = banco.obter_estatisticas_pausas(USUARIO)

    sessao.iniciar_temporizador()

    assert sessao.temporizador_rodando is False
    assert janela.agendados == {}
    assert len(PopUpFalso.abertos) == 1
    assert PopUpFalso.abertos[0].id in {1, 2, 7, 9}  # alongamentos indicados para a dor 1
    assert banco.obter_estatisticas_pausas(USUARIO) == (pausas_antes + 1, concluidas_antes + 1)
    assert banco.obter_estatisticas_alongamentos(USUARIO)[0] == 1


def test_retomar_apos_alongamento_inicia_novo_ciclo(sessao, janela):
    sessao.configurar_sessao(horas_trabalho=1, minutes_pausa=20, identificador_dor=1)
    sessao.tempo_restante_segundos = 1
    sessao.iniciar_temporizador()

    sessao.retomar_apos_alongamento()

    assert sessao.temporizador_rodando is True
    assert sessao.tempo_restante_segundos == 20 * 60 - 1
    assert len(janela.agendados) == 1


def test_tempo_total_continua_correndo_durante_o_alongamento(sessao):
    sessao.configurar_sessao(horas_trabalho=1, minutes_pausa=20, identificador_dor=1)

    sessao.ticar_tempo_total_durante_alongamento()

    assert sessao.tempo_trabalho_total_restante == 3599
    assert sessao.tempo_restante_segundos == 20 * 60


def test_fim_da_jornada_zera_o_relogio_sem_abrir_alongamento(sessao, janela):
    sessao.configurar_sessao(horas_trabalho=1, minutes_pausa=20, identificador_dor=1)
    sessao.tempo_restante_segundos = 1
    sessao.tempo_trabalho_total_restante = 1

    sessao.iniciar_temporizador()

    assert sessao.temporizador_rodando is False
    assert sessao.tela == {"relogio": "00:00", "total": "0:00:00"}
    assert PopUpFalso.abertos == []
    assert janela.agendados == {}
