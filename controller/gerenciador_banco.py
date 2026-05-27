import sqlite3
from model.Alongamento import Alongamento

class GerenciadorBanco:
    def __init__(self, caminho_banco_dados="alongfit.db"):
        self.caminho_banco_dados = caminho_banco_dados

    def autenticar_usuario(self, email_digitado, senha_digitada):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                SELECT idUsuario, Nome 
                FROM Usuario 
                WHERE email = ? AND senha = ?
            """, (email_digitado, senha_digitada))
            
            usuario_encontrado = cursor_banco.fetchone()
            
            if usuario_encontrado:
                return {"id": usuario_encontrado[0], "nome": usuario_encontrado[1]}
            return None

    def registrar_usuario(self, usuario):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                INSERT INTO Usuario (Nome, email, senha, dataNasc)
                VALUES (?, ?, ?, ?)
            """, (usuario.Nome, usuario.email, usuario.senha, usuario.dataNasc))
            conexao_banco.commit()

    def registrar_dor_usuario(self, dor_usuario):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                DELETE FROM UserDor WHERE Usuario_idUsuario = ?
            """, (dor_usuario.usuario_idUsuario,))
            
            cursor_banco.execute("""
                INSERT INTO UserDor (TipoDor_idTipoDor, Usuario_idUsuario)
                VALUES (?, ?)
            """, (dor_usuario.tipoDor_idTipoDor, dor_usuario.usuario_idUsuario))
            conexao_banco.commit()

    def buscar_dor_registrada_usuario(self, identificador_usuario):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                SELECT TipoDor_idTipoDor 
                FROM UserDor 
                WHERE Usuario_idUsuario = ? 
                LIMIT 1
            """, (identificador_usuario,))
            
            linha_retornada = cursor_banco.fetchone()
            if linha_retornada:
                return linha_retornada[0]
            return 1

    def registrar_inicio_jornada(self, jornada):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                INSERT INTO JornadaTrabalho (inicioJornd, tempoLembrete, Usuario_idUsuario)
                VALUES (?, ?, ?)
            """, (jornada.inicioJornd, jornada.tempoLembrete, jornada.usuario_idUsuario))
            conexao_banco.commit()
            return cursor_banco.lastrowid

    def registrar_fim_jornada(self, id_jornada, data_hora_fim):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                UPDATE JornadaTrabalho 
                SET fimJornd = ? 
                WHERE id = ?
            """, (data_hora_fim, id_jornada))
            conexao_banco.commit()

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
                lista_alongamentos.append(Alongamento(
                    id=linha[0], nome=linha[1], descricao=linha[2], duracao=linha[3]
                ))
            return lista_alongamentos

    def registrar_pausa_concluida(self, pausa):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                INSERT INTO Pausas (inicio, fim, concluida, Usuario_idUsuario)
                VALUES (?, ?, ?, ?)
            """, (pausa.inicio, pausa.fim, pausa.concluida, pausa.usuario_idUsuario))
            conexao_banco.commit()

    def registrar_historico_alongamento(self, historico):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                INSERT INTO HistoricoAlon (Alongamento_idAI, Usuario_idUsuario, Inicio, dataFim)
                VALUES (?, ?, ?, ?)
            """, (historico.Alongamento_idAI, historico.usuario_idUsuario, historico.inicio, historico.dataFim))
            conexao_banco.commit()

    def obter_estatisticas_pausas(self, identificador_usuario):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                SELECT COUNT(*), SUM(CASE WHEN concluida = 'SIM' THEN 1 ELSE 0 END)
                FROM Pausas
                WHERE Usuario_idUsuario = ?
            """, (identificador_usuario,))
            
            resultado = cursor_banco.fetchone()
            total_pausas = resultado[0] if resultado[0] else 0
            pausas_concluidas = resultado[1] if resultado[1] else 0
            return total_pausas, pausas_concluidas

    def obter_estatisticas_alongamentos(self, identificador_usuario):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                SELECT COUNT(*), SUM(tempoTotal)
                FROM HistoricoAlon
                WHERE Usuario_idUsuario = ?
            """, (identificador_usuario,))
            
            resultado = cursor_banco.fetchone()
            total_alongamentos = resultado[0] if resultado[0] else 0
            tempo_total = resultado[1] if resultado[1] else 0
            return total_alongamentos, tempo_total