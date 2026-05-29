import tkinter as tk
from pathlib import Path
from tkinter import font as tkfont

# ==========================================
# CONFIGURAÇÕES E CONSTANTES
# ==========================================
BG_GERAL = "#d9d9d9"
BG_CARTAO = "#FFFFFF"
COR_TEXTO = "#444444"
COR_TITULO = "#1A1A1A"

# Simulando os dias da semana com base na sua imagem
# (nome_do_dia, arquivo_da_imagem)
WEEK_DAYS = [
    ("Dom", "Group 23.png"), 
    ("Seg", "Group 24.png"), 
    ("Ter", "Group 23.png"),
    ("Qua", "Group 23.png"),
    ("Qui", "Group 24.png"),
    ("Sex", "Group 24.png"),
    ("Sab", "Group 23.png"),
]


class TimerPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BG_GERAL)
        self.assets_dir = Path(__file__).resolve().parent.parent / "assets"
        self.icones_dias = {}
        
        self.f_titulo = tkfont.Font(family="Helvetica", size=24, weight="bold")
        self.f_cartao_titulo = tkfont.Font(family="Helvetica", size=32, weight="bold")
        self.f_cartao_texto = tkfont.Font(family="Helvetica", size=32)
        
        # ==========================================
        # 1. CRIANDO AS VARIÁVEIS DINÂMICAS
        # ==========================================
        self.var_nome_tarefa = tk.StringVar(value="Nenhuma tarefa ativa")
        self.var_tempo_principal = tk.StringVar(value="00:00")
        self.var_tempo_pausa = tk.StringVar(value="--:--")
        
        self._build()

    def _build(self):
        # 1. Container Principal
        self.contorno = tk.Frame(self, bg=BG_GERAL, width=1300, height=1400)
        self.contorno.pack(anchor="c", expand=True, fill="both")
        self.contorno.pack_propagate(False)

        # 2. Divisão de Colunas
        self.coluna_esquerda = tk.Frame(self.contorno, bg=BG_GERAL)
        self.coluna_esquerda.pack(side="left", anchor="nw", padx=(0, 20), expand=True, fill="both") 

        self.coluna_direita = tk.Frame(self.contorno, bg=BG_GERAL)
        self.coluna_direita.pack(side="right", anchor="n", expand=True, fill="both") 

        # 3. Cabeçalho
        tk.Label(
            self.coluna_esquerda,
            text="Timer de Trabalho",
            bg=BG_GERAL,
            fg=COR_TITULO,
            font=self.f_titulo,
        ).pack(pady=(30, 10), anchor="w")

        # 4. Construção dos Painéis (Cartões)
        self._build_timer_ativo()
        self._build_pausa_programada()
        self._build_progresso_semanal()


    # ==========================================
    # MÉTODOS DE CONSTRUÇÃO DOS CARTÕES
    # ==========================================

    def _build_timer_ativo(self):
        """Constrói o cartão grande da esquerda (Timer em andamento)"""
        cartao = tk.Frame(self.coluna_esquerda, bg=BG_CARTAO, width=630, height=900)
        cartao.pack(anchor="w", fill="both", expand=True)
        cartao.pack_propagate(False)

        tk.Label(cartao, text="Tarefa em Andamento:", bg=BG_CARTAO, fg=COR_TEXTO, font=self.f_cartao_titulo).pack(pady=(40, 0))
        
        # 1. Variável do Nome da Tarefa
        tk.Label(cartao, textvariable=self.var_nome_tarefa, bg=BG_CARTAO, fg=COR_TEXTO, font=self.f_cartao_texto).pack(pady=(0, 20))

        centro = tk.Frame(cartao, bg=BG_CARTAO)
        centro.pack(expand=True)
        
        # 2. Variável do Relógio
        tk.Label(centro, textvariable=self.var_tempo_principal, bg=BG_CARTAO, fg=COR_TITULO, font=("Helvetica", 64, "bold")).pack()

        # ==========================================
        # 3. OS BOTÕES VOLTARAM! (Área do Rodapé)
        # ==========================================
        rodape = tk.Frame(cartao, bg=BG_CARTAO)
        # Empurra o rodapé pro fundo da tela
        rodape.pack(side="bottom", fill="x", pady=40) 

        # Centralizando os botões criando um frame interno
        caixa_botoes = tk.Frame(rodape, bg=BG_CARTAO)
        caixa_botoes.pack(anchor="c")

        # Botão Pausa
        tk.Button(
            caixa_botoes, 
            text="Pausa", 
            bg="#e5e7eb", 
            font=("Helvetica", 16), 
            relief="flat", 
            padx=30, pady=10
        ).pack(side="left", padx=10)

        # Botão Cancelar
        tk.Button(
            caixa_botoes, 
            text="Cancelar", 
            bg="#e5e7eb", 
            font=("Helvetica", 16), 
            relief="flat", 
            padx=30, pady=10
        ).pack(side="left", padx=10)

    def _build_pausa_programada(self):
        """Constrói o cartão superior da direita (Pausa programada)"""
        cartao = tk.Frame(self.coluna_direita, bg=BG_CARTAO, width=630, height=350)
        # O pady compensa a altura do título da coluna esquerda para alinhar
        cartao.pack(anchor="w", pady=(83, 20), fill="x")
        cartao.pack_propagate(False)

        tk.Label(cartao, text="Pausa programada para:", bg=BG_CARTAO, fg=COR_TEXTO, font=self.f_cartao_titulo).pack(pady=(40, 0))
        
        centro = tk.Frame(cartao, bg=BG_CARTAO)
        centro.pack(expand=True)
        
        # 4. SUBSTITUINDO O TEMPO DA PAUSA
        tk.Label(centro, textvariable=self.var_tempo_pausa, bg=BG_CARTAO, fg=COR_TITULO, font=("Helvetica", 48, "bold")).pack()


    def _build_progresso_semanal(self):
        """Constrói o cartão inferior da direita (Progresso com os dias)"""
        cartao = tk.Frame(self.coluna_direita, bg=BG_CARTAO, width=630, height=350)
        cartao.pack(anchor="w", fill="x")
        cartao.pack_propagate(False)

        tk.Label(cartao, text="Progresso semanal", bg=BG_CARTAO, fg=COR_TITULO, font=self.f_cartao_titulo).pack(pady=(40, 30))

        # Frame para segurar os dias lado a lado centralizados
        caixa_dias = tk.Frame(cartao, bg=BG_CARTAO)
        caixa_dias.pack(anchor="c")

        # Gera os ícones dinamicamente!
        for dia_nome, imagem_nome in WEEK_DAYS:
            self._build_icone_dia(caixa_dias, dia_nome, imagem_nome)


    def _build_icone_dia(self, container_pai, dia_nome, imagem_nome):
        """Método auxiliar que cria cada dia da semana individualmente"""
        dia_container = tk.Frame(container_pai, bg=BG_CARTAO)
        dia_container.pack(side="left", padx=15)

        try:
            # 1. Pega o caminho do arquivo
            caminho_imagem = self.assets_dir / imagem_nome
            
            # 2. O SUBSAMPLE ENTRA AQUI! (Direto na criação do PhotoImage)
            icone = tk.PhotoImage(file=caminho_imagem).subsample(2, 2) 
            
            self.icones_dias[dia_nome] = icone # Salva a referência

            tk.Label(dia_container, image=icone, bg=BG_CARTAO).pack(pady=20)
        except Exception as e:
            tk.Label(dia_container, text="O", font=("Helvetica", 24), bg=BG_CARTAO, fg="#a7f3d0").pack()

        # Adiciona o texto (Dom, Seg, Ter...) embaixo da imagem
        tk.Label(dia_container, text=dia_nome, bg=BG_CARTAO, font=("Helvetica", 14)).pack(pady=(5, 0))