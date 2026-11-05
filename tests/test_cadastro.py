"""Cadastro feito pela tela (AuthController.cadastrar_novo_usuario)."""
import sqlite3

import pytest

from controller.auth_controller import AuthController


def contar_usuarios(pasta):
    with sqlite3.connect(pasta / "alongfit.db") as conexao:
        return conexao.execute("SELECT COUNT(*) FROM Usuario").fetchone()[0]


@pytest.mark.parametrize(
    ("email", "senha", "mensagem"),
    [
        ("joao.email.com", "segredo1", "E-mail inválido."),
        ("joao@email.com", "123", "A senha deve conter pelo menos 6 caracteres."),
    ],
)
def test_cadastro_invalido_e_recusado_e_nada_e_gravado(banco, pasta_temporaria, email, senha, mensagem):
    usuarios_antes = contar_usuarios(pasta_temporaria)

    sucesso, retorno = AuthController().cadastrar_novo_usuario("João", email, senha, "2000-01-01")

    assert sucesso is False
    assert retorno == mensagem
    assert contar_usuarios(pasta_temporaria) == usuarios_antes


def test_cadastro_valido_permite_fazer_login(banco):
    auth = AuthController()

    sucesso, _ = auth.cadastrar_novo_usuario("João", "joao@email.com", "segredo1", "2000-01-01")

    assert sucesso is True
    assert auth.realizar_login("joao@email.com", "segredo1")[0] is True


def test_cadastro_com_email_repetido_e_recusado(banco):
    sucesso, retorno = AuthController().cadastrar_novo_usuario(
        "Outra Ana", "ana.souza@email.com", "segredo1", "1990-01-01"
    )

    assert sucesso is False
    assert retorno.startswith("Erro ao cadastrar")
