import sqlite3
import os
from model.Alongamento import Alongamento

class GerenciadorBanco:
    def __init__(self, caminho_banco_dados="alongfit.db"):
        self.caminho_banco_dados = caminho_banco_dados
        self._inicializar_banco_se_necessario()

    def _inicializar_banco_se_necessario(self):
        # Se o arquivo do banco já existir na pasta, o sistema já foi iniciado antes.
        if os.path.exists(self.caminho_banco_dados):
            return

        print("Primeiro acesso detectado: Construindo o banco de dados local...")
        
        caminho_tabelas = os.path.join('dao', 'Script alongFit.sql')
        caminho_dados = os.path.join('dao', 'Script_InsertDados.sql')
        
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            try:
                # Lê e executa o script que cria as tabelas do sistema
                with open(caminho_tabelas, 'r', encoding='utf-8') as arquivo_tabelas:
                    cursor_banco.executescript(arquivo_tabelas.read())
                    
                # Lê e executa o script que insere os dados iniciais (como a Ana Souza)
                with open(caminho_dados, 'r', encoding='utf-8') as arquivo_dados:
                    cursor_banco.executescript(arquivo_dados.read())
                    
                conexao_banco.commit()
                print("Banco de dados 'alongfit.db' criado com sucesso!")
            except Exception as erro:
                print(f"Erro ao tentar criar o banco de dados inicial: {erro}")

    def autenticar_usuario(self, email_digitado, senha_digitada):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                SELECT idUsuario, nome 
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
            """, (usuario.nome, usuario.email, usuario.senha, usuario.dataNasc))
            conexao_banco.commit()

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

    def buscar_alongamentos_por_dor(self, identificador_tipo_dor, identificador_usuario):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                SELECT a.id, a.nome, a.descricao, a.duracao
                FROM Alongamento a
                INNER JOIN recomendacao_along r ON a.id = r.alongamento_idAl
                WHERE r.TipoDor_idTipoDor = ? AND r.Usuario_idUsuario = ?
            """, (identificador_tipo_dor, identificador_usuario))
            
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
                INSERT INTO HistoricoAlon (alongamento_idAl, Usuario_idUsuario, tipoDor_idTipoDor, Inicio, tempoTotal, dataFim)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (historico.alongamento_idAl, historico.usuario_idUsuario, historico.tipoDor_idTipoDor, historico.inicio, historico.tempoTotal, historico.dataFim))
            conexao_banco.commit()

    def obter_estatisticas_pausas(self, identificador_usuario):
        with sqlite3.connect(self.caminho_banco_dados) as conexao_banco:
            cursor_banco = conexao_banco.cursor()
            cursor_banco.execute("""
                SELECT COUNT(*), SUM(CASE WHEN concluida = 'concluida' THEN 1 ELSE 0 END)
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