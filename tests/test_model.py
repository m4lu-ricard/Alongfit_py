"""Regras de validacao das entidades do model/."""
import pytest

from model.Alongamento import Alongamento
from model.HistoricoAlon import HistoricoAlon
from model.JornadaTrabalho import JornadaTrabalho
from model.Pausas import Pausas
from model.Usuario import Usuario


def test_usuario_valido_guarda_os_dados_informados():
    usuario = Usuario(None, "Ana", "ana@email.com", "segredo1", "1990-01-01")

    assert usuario.nome == "Ana"
    assert usuario.email == "ana@email.com"
    assert usuario.senha == "segredo1"


@pytest.mark.parametrize("email", ["anaemail.com", ""])
def test_usuario_rejeita_email_sem_arroba(email):
    with pytest.raises(ValueError, match="E-mail inválido"):
        Usuario(None, "Ana", email, "segredo1", "1990-01-01")


def test_usuario_rejeita_senha_com_menos_de_6_caracteres():
    with pytest.raises(ValueError, match="pelo menos 6 caracteres"):
        Usuario(None, "Ana", "ana@email.com", "12345", "1990-01-01")


def test_pausa_aceita_somente_os_status_previstos():
    pausa = Pausas(None, "2026-11-04 10:00:00", None, "ignorada", 1)
    assert pausa.concluida == "ignorada"

    with pytest.raises(ValueError, match="status de conclusão"):
        Pausas(None, "2026-11-04 10:00:00", None, "feita", 1)


def test_pausa_exige_horario_de_inicio():
    with pytest.raises(ValueError, match="início da pausa é obrigatório"):
        Pausas(None, "", None, "concluida", 1)


def test_historico_rejeita_tempo_total_negativo():
    with pytest.raises(ValueError, match="não pode ser negativo"):
        HistoricoAlon(None, 1, 1, 1, "2026-11-04 10:00:00", -1, None)


@pytest.mark.parametrize("duracao", [0, -30])
def test_alongamento_rejeita_duracao_zero_ou_negativa(duracao):
    with pytest.raises(ValueError, match="maior que zero"):
        Alongamento(1, "Rotação Cervical", "descricao", duracao)


def test_alongamento_rejeita_nome_em_branco():
    with pytest.raises(ValueError, match="não pode ser vazio"):
        Alongamento(1, "   ", "descricao", 30)


def test_jornada_rejeita_lembrete_negativo():
    with pytest.raises(ValueError, match="não pode ser um valor negativo"):
        JornadaTrabalho(None, "Foco", 2, -10, 1, 1)


def test_tipo_dor_exige_regiao_do_corpo():
    from model.TipoDor import TipoDor

    dor = TipoDor(1, "Cervicalgia", None, "Pescoço")
    assert dor.descricao == ""

    with pytest.raises(ValueError, match="região do corpo"):
        TipoDor(1, "Cervicalgia", "dor no pescoço", " ")
