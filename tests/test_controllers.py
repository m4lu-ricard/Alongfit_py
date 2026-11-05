"""Banco local, login e estatisticas, usando os dados iniciais de dao/Script_InsertDados.sql."""
from controller.auth_controller import AuthController
from controller.estatisticas_controller import EstatisticasController


def test_banco_novo_e_criado_com_os_dados_iniciais(banco, pasta_temporaria):
    assert (pasta_temporaria / "alongfit.db").exists()

    alongamentos_pescoco = banco.buscar_alongamentos_por_dor(1)
    assert sorted(a.id for a in alongamentos_pescoco) == [1, 2, 7, 9]


def test_login_com_credenciais_corretas_identifica_o_usuario(banco):
    auth = AuthController()

    sucesso, _ = auth.realizar_login("ana.souza@email.com", "ana123")

    assert sucesso is True
    assert auth.identificador_usuario_ativo == 1
    assert auth.nome_usuario_ativo == "Ana Souza"


def test_login_com_senha_errada_e_recusado(banco):
    auth = AuthController()

    sucesso, mensagem = auth.realizar_login("ana.souza@email.com", "senha-errada")

    assert sucesso is False
    assert mensagem == "Email ou senha incorretos."
    assert auth.identificador_usuario_ativo is None


def test_resumo_calcula_taxa_de_conclusao_e_tempo_em_minutos(banco):
    # Usuario 1 nos dados iniciais: 2 pausas concluidas e 7 alongamentos
    # somando 235 segundos (3 minutos inteiros).
    resumo = EstatisticasController(1).carregar_resumo_sessao()

    assert resumo == {
        "total_pausas_programadas": 2,
        "pausas_realizadas": 2,
        "taxa_conclusao_percentagem": 100.0,
        "total_alongamentos_feitos": 7,
        "tempo_total_exercicio_minutos": 3,
    }


def test_resumo_considera_pausas_nao_concluidas(banco):
    # Usuario 4: uma pausa concluida e uma pendente.
    resumo = EstatisticasController(4).carregar_resumo_sessao()

    assert resumo["total_pausas_programadas"] == 2
    assert resumo["taxa_conclusao_percentagem"] == 50.0


def test_resumo_de_usuario_sem_pausas_nao_divide_por_zero(banco):
    resumo = EstatisticasController(99).carregar_resumo_sessao()

    assert resumo["taxa_conclusao_percentagem"] == 0
    assert resumo["total_alongamentos_feitos"] == 0


def test_grafico_do_mes_usa_dados_reais_quando_existem(banco):
    dias, quantidades, minutos, eh_exemplo = EstatisticasController(1).buscar_dados_mes(5)

    assert eh_exemplo is False
    assert dias == ["25", "26", "27", "28", "29", "30", "31"]
    assert quantidades == [1, 1, 1, 1, 1, 1, 1]
    assert minutos[-1] == 1.0


def test_grafico_do_mes_sem_dados_sinaliza_dados_de_exemplo(banco):
    *_, eh_exemplo = EstatisticasController(1).buscar_dados_mes(1)

    assert eh_exemplo is True
