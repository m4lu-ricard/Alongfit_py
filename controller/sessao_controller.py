from datetime import timedelta, datetime
from controller.gerenciador_banco import GerenciadorBanco
from model.Pausas import Pausas
from model.HistoricoAlon import HistoricoAlon
from model.Alongamento import Alongamento
from view.pop_up import PopUp

class SessaoController:
    def __init__(self, janela_principal, identificador_usuario_logado):
        self.janela_principal = janela_principal
        self.identificador_usuario_logado = identificador_usuario_logado
        self.banco_dados = GerenciadorBanco()
        
        self.tempo_trabalho_total_restante = 0 
        self.tempo_pausa_segundos = 0          
        self.tempo_restante_segundos = 0       
        
        self.identificador_dor_selecionada = None
        self.temporizador_rodando = False
        self.identificador_processo_temporizador = None
        
        self.funcao_atualizar_texto_relogio = None
        self.funcao_atualizar_tempo_total = None 

    def configurar_sessao(self, horas_trabalho, minutes_pausa, identificador_dor):
        self.tempo_trabalho_total_restante = horas_trabalho * 3600
        self.tempo_pausa_segundos = minutes_pausa * 60
        self.identificador_dor_selecionada = identificador_dor
        self._definir_proximo_ciclo()

    def _definir_proximo_ciclo(self):
        if self.tempo_trabalho_total_restante > self.tempo_pausa_segundos:
            self.tempo_restante_segundos = self.tempo_pausa_segundos
        else:
            self.tempo_restante_segundos = self.tempo_trabalho_total_restante
        self.atualizar_interface_relogio()

    def vincular_interface_relogio(self, funcao_atualizacao):
        self.funcao_atualizar_texto_relogio = funcao_atualizacao
        self.atualizar_interface_relogio()

    def vincular_interface_tempo_total(self, funcao_atualizacao):
        self.funcao_atualizar_tempo_total = funcao_atualizacao
        self.atualizar_interface_relogio()

    # =========================================================================
    # FUNÇÃO DO PROGRESSO SEMANAL QUE FALTAVA
    # =========================================================================
    def obter_progresso_semanal(self):
        """Pede ao banco de dados a lista de dias em que houve alongamento"""
        return self.banco_dados.obter_dias_semana_com_alongamento(self.identificador_usuario_logado)

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
            self.tempo_trabalho_total_restante -= 1 
            self.atualizar_interface_relogio()
            
            self.identificador_processo_temporizador = self.janela_principal.after(
                1000, self.executar_ciclo_temporizador
            )
        elif self.tempo_restante_segundos <= 0:
            self.pausar_temporizador()
            if self.tempo_trabalho_total_restante <= 0:
                self.finalizar_jornada_completa()
            else:
                self.disparar_alerta_alongamento()

    def ticar_tempo_total_durante_alongamento(self):
        if self.tempo_trabalho_total_restante > 0:
            self.tempo_trabalho_total_restante -= 1
            self.atualizar_interface_relogio()
            if self.tempo_trabalho_total_restante <= 0:
                self.finalizar_jornada_completa()

    def atualizar_interface_relogio(self):
        if self.funcao_atualizar_texto_relogio:
            tempo_formatado = str(timedelta(seconds=self.tempo_restante_segundos))
            if tempo_formatado.startswith("0:"):
                tempo_formatado = tempo_formatado[2:]
            self.funcao_atualizar_texto_relogio(tempo_formatado)
            
        if self.funcao_atualizar_tempo_total:
            tempo_total_formatado = str(timedelta(seconds=max(0, self.tempo_trabalho_total_restante)))
            self.funcao_atualizar_tempo_total(tempo_total_formatado)

    def disparar_alerta_alongamento(self):
        alongamentos_recomendados = self.banco_dados.buscar_alongamentos_por_dor(
            self.identificador_dor_selecionada, 
            self.identificador_usuario_logado
        )
        
        if not alongamentos_recomendados:
            nomes_dor = {0: "Geral", 1: "Ombros/Pescoço", 4: "Mãos/Punhos", 5: "Costas"}
            regiao = nomes_dor.get(self.identificador_dor_selecionada, "Corpo")
            alongamento_selecionado = Alongamento(id=999, nome=f"Alongamento para {regiao}", descricao="Afaste-se da cadeira, estique os braços para cima e relaxe o pescoço.", duracao=30)
        else:
            alongamento_selecionado = alongamentos_recomendados[0]
            
        try:
            data_hora_inicio_pausa = datetime.now()
            data_hora_fim_pausa = data_hora_inicio_pausa + timedelta(seconds=alongamento_selecionado.duracao)
            data_hora_inicio_formatada = data_hora_inicio_pausa.strftime("%Y-%m-%d %H:%M:%S")
            data_hora_fim_formatada = data_hora_fim_pausa.strftime("%Y-%m-%d %H:%M:%S")

            nova_pausa = Pausas(idPausas=None, inicio=data_hora_inicio_formatada, fim=data_hora_fim_formatada, concluida='concluida', usuario_idUsuario=self.identificador_usuario_logado)
            self.banco_dados.registrar_pausa_concluida(nova_pausa)
            
            if alongamento_selecionado.id != 999:
                novo_historico = HistoricoAlon(idHisto=None, alongamento_idAl=alongamento_selecionado.id, usuario_idUsuario=self.identificador_usuario_logado, tipoDor_idTipoDor=self.identificador_dor_selecionada, inicio=data_hora_inicio_formatada, tempoTotal=alongamento_selecionado.duracao, dataFim=data_hora_fim_formatada)
                self.banco_dados.registrar_historico_alongamento(novo_historico)
        except Exception as e:
            print(f"Log: Pausa registrada localmente ({e})")
        
        PopUp(self.janela_principal, controller=self, alongamento=alongamento_selecionado)

    def retomar_apos_alongamento(self):
        if self.tempo_trabalho_total_restante <= 0:
            self.finalizar_jornada_completa()
            return
            
        self._definir_proximo_ciclo()
        self.iniciar_temporizador()

    def finalizar_jornada_completa(self):
        self.temporizador_rodando = False
        if self.funcao_atualizar_texto_relogio:
            self.funcao_atualizar_texto_relogio("00:00")
        if self.funcao_atualizar_tempo_total:
            self.funcao_atualizar_tempo_total("0:00:00")