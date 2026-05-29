from datetime import datetime
from model.JornadaTrabalho import JornadaTrabalho
from controller.gerenciador_banco import GerenciadorBanco

class ConfigController:
    def __init__(self, identificador_usuario_ativo):
        self.banco_dados = GerenciadorBanco()
        self.identificador_usuario_ativo = identificador_usuario_ativo

    def salvar_preferencias_e_iniciar_jornada(self, horas_trabalho, minutos_pausa):
        try:
            data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            nova_jornada = JornadaTrabalho(
                id=None,
                inicioJornd=data_hora_atual,
                tempoLembrete=minutos_pausa,
                usuario_idUsuario=self.identificador_usuario_ativo,
                fimJornd=None
            )
            
            id_jornada_criada = self.banco_dados.registrar_inicio_jornada(nova_jornada)
            
            return True, "Configurações salvas e jornada iniciada com sucesso.", id_jornada_criada
            
        except ValueError as erro_validacao:
            return False, str(erro_validacao), None
            
        except Exception:
            return False, "Erro inesperado ao salvar no banco de dados.", None