import sqlite3
from model.Alongamento import Alongamento

class GerenciadorBanco:
    def __init__(self, caminho_banco_dados="alongfit.db"):
        self.caminho_banco_dados = caminho_banco_dados

    def buscar_alongamentos_por_dor(self, identificador_tipo_dor):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                SELECT a.id, a.nome, a.descricao, a.duracao
                FROM Alongamento a
                INNER JOIN recomendacao_along r ON a.id = r.Alongamento_idAI
                WHERE r.TipoDor_idTipoDor = ?
            """, (identificador_tipo_dor,))
            
            linhas_retornadas = cursor_banco.fetchall()
            lista_alongamentos = []
            
            for linha in linhas_retornadas:
                alongamento_encontrado = Alongamento(
                    id=linha[0], 
                    nome=linha[1], 
                    descricao=linha[2], 
                    duracao=linha[3]
                )
                lista_alongamentos.append(alongamento_encontrado)
                
            return lista_alongamentos

    def registrar_pausa_concluida(self, identificador_usuario, data_hora_inicio, data_hora_fim, status_conclusao):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                INSERT INTO Pausas (inicio, fim, concluida, Usuario_idUsuario)
                VALUES (?, ?, ?, ?)
            """, (data_hora_inicio, data_hora_fim, status_conclusao, identificador_usuario))
            
            conexao_banco.commit()

    def registrar_historico_alongamento(self, identificador_alongamento, identificador_usuario, data_hora_inicio, data_hora_fim):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                INSERT INTO HistoricoAlon (Alongamento_idAI, Usuario_idUsuario, Inicio, dataFim)
                VALUES (?, ?, ?, ?)
            """, (identificador_alongamento, identificador_usuario, data_hora_inicio, data_hora_fim))
            
            conexao_banco.commit()