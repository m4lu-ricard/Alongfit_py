"""Cartoes de tarefa (jornada de trabalho) salvos pelo ConfigController."""
from controller.config_controller import ConfigController

USUARIO = 3


def test_salvar_tarefa_grava_no_banco_e_aparece_na_lista(banco):
    config = ConfigController(USUARIO)

    sucesso, _, id_criado = config.salvar_nova_tarefa("Relatório", horas=4, minutos=50, id_dor=2)

    assert sucesso is True
    tarefa = next(t for t in config.buscar_tarefas_do_usuario() if t["id"] == id_criado)
    assert tarefa == {"id": id_criado, "nome": "Relatório", "horas": 4, "minutos": 50, "desconforto": 2}


def test_tarefa_com_intervalo_negativo_nao_e_gravada(banco):
    config = ConfigController(USUARIO)
    quantidade_antes = len(config.buscar_tarefas_do_usuario())

    sucesso, mensagem, id_criado = config.salvar_nova_tarefa("Inválida", horas=4, minutos=-5, id_dor=2)

    assert sucesso is False
    assert "não pode ser um valor negativo" in mensagem
    assert id_criado is None
    assert len(config.buscar_tarefas_do_usuario()) == quantidade_antes


def test_atualizar_e_excluir_tarefa(banco):
    config = ConfigController(USUARIO)
    _, _, id_criado = config.salvar_nova_tarefa("Estudo", horas=2, minutos=30, id_dor=1)

    config.atualizar_tarefa_existente(id_criado, horas=3, minutos=45, id_dor=5)
    tarefa = next(t for t in config.buscar_tarefas_do_usuario() if t["id"] == id_criado)
    assert (tarefa["horas"], tarefa["minutos"], tarefa["desconforto"]) == (3, 45, 5)

    sucesso, _ = config.excluir_tarefa(id_criado)
    assert sucesso is True
    assert all(t["id"] != id_criado for t in config.buscar_tarefas_do_usuario())
