"""Regras de tempo da jornada (model/tempo_sessao.py), testadas sem nenhuma janela."""
from model.tempo_sessao import TempoSessao


def test_configurar_prepara_o_primeiro_ciclo():
    tempo = TempoSessao()

    tempo.configurar(horas_trabalho=2, minutos_pausa=30)

    assert (tempo.restante_ciclo, tempo.restante_jornada) == (30 * 60, 2 * 3600)


def test_ciclo_e_limitado_ao_que_resta_da_jornada():
    tempo = TempoSessao()
    tempo.configurar(horas_trabalho=1, minutos_pausa=90)

    assert tempo.restante_ciclo == 3600


def test_avancar_desconta_do_ciclo_e_da_jornada():
    tempo = TempoSessao()
    tempo.configurar(horas_trabalho=1, minutos_pausa=20)

    situacao = tempo.avancar_um_segundo()

    assert situacao == TempoSessao.CICLO_EM_ANDAMENTO
    assert (tempo.restante_ciclo, tempo.restante_jornada) == (1199, 3599)


def test_ultimo_segundo_do_ciclo_indica_hora_da_pausa():
    tempo = TempoSessao()
    tempo.configurar(horas_trabalho=1, minutos_pausa=20)
    tempo.restante_ciclo = 1

    assert tempo.avancar_um_segundo() == TempoSessao.FIM_DO_CICLO
    assert tempo.restante_jornada == 3599


def test_ultimo_segundo_da_jornada_indica_fim_da_jornada():
    tempo = TempoSessao()
    tempo.configurar(horas_trabalho=1, minutos_pausa=20)
    tempo.restante_ciclo = 1
    tempo.restante_jornada = 1

    assert tempo.avancar_um_segundo() == TempoSessao.FIM_DA_JORNADA
    assert tempo.jornada_encerrada() is True


def test_jornada_encerrada_nao_desconta_mais_tempo():
    tempo = TempoSessao()
    tempo.restante_jornada = 0

    assert tempo.descontar_da_jornada() is False
    assert tempo.restante_jornada == 0
