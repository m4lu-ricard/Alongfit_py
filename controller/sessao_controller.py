from datetime import timedelta, datetime
from controller.gerenciador_banco import GerenciadorBanco
from model.Pausas import Pausas
from model.HistoricoAlon import HistoricoAlon

class SessaoController:
    def __init__(self, janela_principal, identificador_usuario_logado):
        self.janela_principal = janela_principal
        self.identificador_usuario_logado = identificador_usuario_logado
        self.banco_dados = GerenciadorBanco()
        
        self.tempo_trabalho_segundos = 0
        self.tempo_pausa_segundos = 0
        self.tempo_restante_segundos = 0
        
        self.temporizador_rodando = False
        self.identificador_processo_temporizador = None
        
        self.funcao_atualizar_texto_relogio = None

    def configurar_sessao(self, horas_trabalho, minutos_pausa):
        self.tempo_trabalho_segundos = horas_trabalho * 3600
        self.tempo_pausa_segundos = minutos_pausa * 60
        self.tempo_restante_segundos = self.tempo_pausa_segundos

    def vincular_interface_relogio(self, funcao_atualizacao):
        self.funcao_atualizar_texto_relogio = funcao_atualizacao
        self.atualizar_interface_relogio()

    def iniciar_temporizador(self):
        if not self.temporizador_rodando:
            self.temporizador_rodando = True
            self.executar_ciclo_temporizador()

    def pausar_temporizador(self):
        self.temporizador_rodando = False
        if self.identificador_processo_temporizador is not None:
            self.janela_principal.after_cancel(self.identificador_processo_temporizador)
            self.identificador_processo_temporizador = None

    def executar_ciclo_temporizador(self):
        if self.temporizador_rodando and self.tempo_restante_segundos > 0:
            self.tempo_restante_segundos -= 1
            self.atualizar_interface_relogio()
            
            self.identificador_processo_temporizador = self.janela_principal.after(
                1000, self.executar_ciclo_temporizador
            )
        elif self.tempo_restante_segundos <= 0:
            self.pausar_temporizador()
            self.disparar_alerta_alongamento()

    def atualizar_interface_relogio(self):
        if self.funcao_atualizar_texto_relogio:
            tempo_formatado = str(timedelta(seconds=self.tempo_restante_segundos))
            if tempo_formatado.startswith("0:"):
                tempo_formatado = tempo_formatado[2:]
            self.funcao_atualizar_texto_relogio(tempo_formatado)

    def disparar_alerta_alongamento(self):
        identificador_dor_usuario = self.banco_dados.buscar_dor_registrada_usuario(self.identificador_usuario_logado)
        
        alongamentos_recomendados = self.banco_dados.buscar_alongamentos_por_dor(identificador_dor_usuario)
        
        if alongamentos_recomendados:
            alongamento_selecionado = alongamentos_recomendados[0]
            
            data_hora_inicio_pausa = datetime.now()
            data_hora_fim_pausa = data_hora_inicio_pausa + timedelta(seconds=alongamento_selecionado.duracao)
            
            data_hora_inicio_formatada = data_hora_inicio_pausa.strftime("%Y-%m-%d %H:%M:%S")
            data_hora_fim_formatada = data_hora_fim_pausa.strftime("%Y-%m-%d %H:%M:%S")

            nova_pausa = Pausas(
                idPausas=None,
                inicio=data_hora_inicio_formatada,
                fim=data_hora_fim_formatada,
                concluida='SIM',
                usuario_idUsuario=self.identificador_usuario_logado
            )
            
            novo_historico = HistoricoAlon(
                idHisto=None,
                Alongamento_idAI=alongamento_selecionado.id,
                usuario_idUsuario=self.identificador_usuario_logado,
                inicio=data_hora_inicio_formatada,
                tempoTotal=alongamento_selecionado.duracao,
                dataFim=data_hora_fim_formatada
            )

            self.banco_dados.registrar_pausa_concluida(nova_pausa)
            self.banco_dados.registrar_historico_alongamento(novo_historico)
        
        self.tempo_restante_segundos = self.tempo_pausa_segundos
        self.atualizar_interface_relogio()