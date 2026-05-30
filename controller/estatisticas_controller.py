from controller.gerenciador_banco import GerenciadorBanco

class EstatisticasController:
    def __init__(self, identificador_usuario_ativo):
        self.banco_dados = GerenciadorBanco()
        self.identificador_usuario_ativo = identificador_usuario_ativo

    def carregar_resumo_sessao(self):
        total_pausas, pausas_concluidas = self.banco_dados.obter_estatisticas_pausas(self.identificador_usuario_ativo)
        total_alongamentos, tempo_total_segundos = self.banco_dados.obter_estatisticas_alongamentos(self.identificador_usuario_ativo)
        
        taxa_conclusao = 0
        if total_pausas > 0:
            taxa_conclusao = (pausas_concluidas / total_pausas) * 100
            
        tempo_total_minutos = tempo_total_segundos // 60
        
        dados_estatisticos = {
            "total_pausas_programadas": total_pausas,
            "pausas_realizadas": pausas_concluidas,
            "taxa_conclusao_percentagem": round(taxa_conclusao, 1),
            "total_alongamentos_feitos": total_alongamentos,
            "tempo_total_exercicio_minutos": tempo_total_minutos
        }
        
        return dados_estatisticos

    def buscar_dados_mes(self, mes):
        mes_formatado = str(mes).zfill(2)
        
        resultados = self.banco_dados.obter_dados_grafico_mes(self.identificador_usuario_ativo, mes_formatado)
        
        dias = []
        qtd_alongamentos = []
        minutos_total = []
        
        for linha in resultados:
            dia = str(linha[0])
            qtd = linha[1]
            minutos = round((linha[2] or 0) / 60, 1) 
            
            dias.append(dia)
            qtd_alongamentos.append(qtd)
            minutos_total.append(minutos)
            
        return dias, qtd_alongamentos, minutos_total