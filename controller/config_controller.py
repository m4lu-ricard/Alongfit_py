from datetime import datetime
from model.JornadaTrabalho import JornadaTrabalho
from controller.gerenciador_banco import GerenciadorBanco

class ConfigController:
    def __init__(self, identificador_usuario_ativo):
        self.banco_dados = GerenciadorBanco()
        self.identificador_usuario_ativo = identificador_usuario_ativo

    def buscar_tarefas_do_usuario(self):
        return self.banco_dados.buscar_jornadas_por_usuario(self.identificador_usuario_ativo)
        
    def salvar_nova_tarefa(self, nome_tarefa, horas, minutos, id_dor):
        try:
            nova_jornada = JornadaTrabalho(
                id=None,
                nome=nome_tarefa,
                tempo=horas,
                tempoLembrete=minutos,
                usuario_idUsuario=self.identificador_usuario_ativo,
                desconforto=id_dor
            )
            id_criado = self.banco_dados.registrar_nova_tarefa(nova_jornada)
            return True, "Tarefa salva com sucesso", id_criado
        except Exception as e:
            return False, f"Erro ao salvar: {str(e)}", None

    def atualizar_tarefa_existente(self, id_jornada, horas, minutos, id_dor):
        self.banco_dados.atualizar_tarefa(id_jornada, horas, minutos, id_dor)
    
    def excluir_tarefa(self, id_jornada):
        try:
            self.banco_dados.excluir_tarefa(id_jornada)
            return True, "Tarefa excluída com sucesso"
        except Exception as e:
            return False, f"Erro ao excluir: {str(e)}"