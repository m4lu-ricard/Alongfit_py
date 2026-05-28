import sqlite3

class GerenciadorBanco:
    def __init__(self, caminho_banco_dados="alongfit.db"):
        self.caminho_banco_dados = caminho_banco_dados

    def autenticar_usuario(self, email_digitado, senha_digitada):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                SELECT id_usuario, nome 
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
                INSERT INTO Usuario (nome, email, senha, data_nasc)
                VALUES (?, ?, ?, ?)
            """, (usuario.nome, usuario.email, usuario.senha, usuario.data_nasc))
            conexao_banco.commit()

    def registrar_dor_usuario(self, dor_usuario):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                DELETE FROM Usuario_dor WHERE usuario_id = ?
            """, (dor_usuario.usuario_id,))
            
            cursor_banco.execute("""
                INSERT INTO Usuario_dor (tipo_dor_id, usuario_id)
                VALUES (?, ?)
            """, (dor_usuario.tipo_dor_id, dor_usuario.usuario_id))
            conexao_banco.commit()

    def buscar_dor_registrada_usuario(self, identificador_usuario):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                SELECT tipo_dor_id 
                FROM Usuario_dor 
                WHERE usuario_id = ? 
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
                INSERT INTO Jornada_trabalho (inicio_jornada, intervalo_lembrete_min, usuario_id)
                VALUES (?, ?, ?)
            """, (jornada.inicio_jornada, jornada.intervalo_lembrete_min, jornada.usuario_id))
            conexao_banco.commit()
            return cursor_banco.lastrowid

    def registrar_fim_jornada(self, id_jornada, data_hora_fim):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                UPDATE Jornada_trabalho 
                SET fim_jornada = ? 
                WHERE id_jornada = ?
            """, (data_hora_fim, id_jornada))
            conexao_banco.commit()

    def buscar_alongamentos_por_dor(self, identificador_tipo_dor):
        from model.Alongamento import Alongamento
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                SELECT a.id_alongamento, a.nome, a.descricao, a.duracao
                FROM Alongamento a
                INNER JOIN Alongamento_tipo_dor r ON a.id_alongamento = r.alongamento_id
                WHERE r.tipo_dor_id = ?
            """, (identificador_tipo_dor,))
            
            linhas_retornadas = cursor_banco.fetchall()
            lista_alongamentos = []
            
            for linha in linhas_retornadas:
                lista_alongamentos.append(Alongamento(
                    id_alongamento=linha[0], nome=linha[1], descricao=linha[2], duracao=linha[3]
                ))
            return lista_alongamentos

    def registrar_pausa_concluida(self, pausa):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                INSERT INTO Pausas (inicio, fim, status, usuario_id, alongamento_id)
                VALUES (?, ?, ?, ?, ?)
            """, (pausa.inicio, pausa.fim, pausa.status, pausa.usuario_id, pausa.alongamento_id))
            conexao_banco.commit()

    def registrar_historico_alongamento(self, historico):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                INSERT INTO Historico_alongamento (alongamento_id, usuario_id, inicio, tempo_total, data_fim)
                VALUES (?, ?, ?, ?, ?)
            """, (historico.alongamento_id, historico.usuario_id, historico.inicio, historico.tempo_total, historico.data_fim))
            conexao_banco.commit()

    def obter_estatisticas_pausas(self, identificador_usuario):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                SELECT COUNT(*), SUM(CASE WHEN status = 'realizada' THEN 1 ELSE 0 END)
                FROM Pausas
                WHERE usuario_id = ?
            """, (identificador_usuario,))
            
            resultado = cursor_banco.fetchone()
            total_pausas = resultado[0] if resultado[0] else 0
            pausas_concluidas = resultado[1] if resultado[1] else 0
            return total_pausas, pausas_concluidas

    def obter_estatisticas_alongamentos(self, identificador_usuario):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                SELECT COUNT(*), SUM(tempo_total)
                FROM Historico_alongamento
                WHERE usuario_id = ?
            """, (identificador_usuario,))
            
            resultado = cursor_banco.fetchone()
            total_alongamentos = resultado[0] if resultado[0] else 0
            tempo_total = resultado[1] if resultado[1] else 0
            return total_alongamentos, tempo_total