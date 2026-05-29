import tkinter as tk
from pathlib import Path
from tkinter import font as tkfont

BG_GERAL = "#d9d9d9"
BG_CARTAO = "#FFFFFF"
COR_TEXTO = "#444444"
COR_TITULO = "#1A1A1A"

class TimerPage(tk.Frame):
    def __init__(self, parent, app): 
        super().__init__(parent, bg=BG_GERAL)
        self.app = app

        self.assets_dir = Path(__file__).resolve().parent.parent / "assets"
        self.icones_dias = {}

        self.f_titulo = tkfont.Font(family="Helvetica", size=24, weight="bold")
        self.f_cartao_titulo = tkfont.Font(family="Helvetica", size=32, weight="bold")
        self.f_cartao_texto = tkfont.Font(family="Helvetica", size=32)
        
        self.var_nome_tarefa = tk.StringVar(value="Trabalho em Foco")
        self.var_tempo_principal = tk.StringVar(value="00:00")
        self.var_tempo_total = tk.StringVar(value="0:00:00")
        
        self.var_texto_botao_pausa = tk.StringVar(value="Pausa")

        self._build()

        self.app.sessao_controller.vincular_interface_relogio(self.var_tempo_principal.set)
        self.app.sessao_controller.vincular_interface_tempo_total(self.var_tempo_total.set)

    def _build(self):
        self.contorno = tk.Frame(self, bg=BG_GERAL, width=1300, height=1400)
        self.contorno.pack(anchor="c", expand=True, fill="both")
        self.contorno.pack_propagate(False)

        self.coluna_esquerda = tk.Frame(self.contorno, bg=BG_GERAL)
        self.coluna_esquerda.pack(side="left", anchor="nw", padx=(0, 20), expand=True, fill="both") 

        self.coluna_direita = tk.Frame(self.contorno, bg=BG_GERAL)
        self.coluna_direita.pack(side="right", anchor="n", expand=True, fill="both") 

        tk.Label(
            self.coluna_esquerda, text="Timer de Trabalho",
            bg=BG_GERAL, fg=COR_TITULO, font=self.f_titulo
        ).pack(pady=(30, 10), anchor="w")

        self._build_timer_ativo()
        self._build_Tempo_Total_Restante() 
        self._build_progresso_semanal()

    def _build_timer_ativo(self):
        cartao = tk.Frame(self.coluna_esquerda, bg=BG_CARTAO, width=630, height=900)
        cartao.pack(anchor="w", fill="both", expand=True)
        cartao.pack_propagate(False)

        tk.Label(cartao, text="Tarefa em Andamento:", bg=BG_CARTAO, fg=COR_TEXTO, font=self.f_cartao_titulo).pack(pady=(40, 0))
        tk.Label(cartao, textvariable=self.var_nome_tarefa, bg=BG_CARTAO, fg=COR_TEXTO, font=self.f_cartao_texto).pack(pady=(0, 20))

        centro = tk.Frame(cartao, bg=BG_CARTAO)
        centro.pack(expand=True)
        
        tk.Label(centro, textvariable=self.var_tempo_principal, bg=BG_CARTAO, fg=COR_TITULO, font=("Helvetica", 64, "bold")).pack()

        rodape = tk.Frame(cartao, bg=BG_CARTAO)
        rodape.pack(side="bottom", fill="x", pady=40) 
        caixa_botoes = tk.Frame(rodape, bg=BG_CARTAO)
        caixa_botoes.pack(anchor="c")

        tk.Button(
            caixa_botoes, textvariable=self.var_texto_botao_pausa, bg="#e5e7eb", 
            font=("Helvetica", 16), relief="flat", padx=30, pady=10,
            command=self.alternar_pausa
        ).pack(side="left", padx=10)
        
        tk.Button(
            caixa_botoes, text="Cancelar", bg="#e5e7eb", font=("Helvetica", 16), 
            relief="flat", padx=30, pady=10, command=lambda: self.app.show_page("home") 
        ).pack(side="left", padx=10)

    def _build_Tempo_Total_Restante(self):
        cartao = tk.Frame(self.coluna_direita, bg=BG_CARTAO, width=630, height=350)
        cartao.pack(anchor="w", pady=(83, 20), fill="x")
        cartao.pack_propagate(False)

        tk.Label(cartao, text="Tempo Total Restante:", bg=BG_CARTAO, fg=COR_TEXTO, font=self.f_cartao_titulo).pack(pady=(40, 0))
        centro = tk.Frame(cartao, bg=BG_CARTAO)
        centro.pack(expand=True)
        tk.Label(centro, textvariable=self.var_tempo_total, bg=BG_CARTAO, fg=COR_TITULO, font=("Helvetica", 48, "bold")).pack()

    def _build_progresso_semanal(self):
        cartao = tk.Frame(self.coluna_direita, bg=BG_CARTAO, width=630, height=350)
        cartao.pack(anchor="w", fill="x")
        cartao.pack_propagate(False)

        tk.Label(cartao, text="Progresso semanal", bg=BG_CARTAO, fg=COR_TITULO, font=self.f_cartao_titulo).pack(pady=(40, 30))

        caixa_dias = tk.Frame(cartao, bg=BG_CARTAO)
        caixa_dias.pack(anchor="c")

        dias_concluidos = self.app.sessao_controller.obter_progresso_semanal()
        nomes_dias = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"]

        for indice_dia, dia_nome in enumerate(nomes_dias):
            fez_alongamento = (indice_dia in dias_concluidos)
            self._build_icone_dia(caixa_dias, dia_nome, fez_alongamento)

    def _build_icone_dia(self, container_pai, dia_nome, fez_alongamento):
        dia_container = tk.Frame(container_pai, bg=BG_CARTAO)
        dia_container.pack(side="left", padx=15)

        imagem_nome = "verificado.png" if fez_alongamento else "triste.png"
        simbolo_emoji = "✅" if fez_alongamento else "❌"
        cor_emoji = "#4ade80" if fez_alongamento else "#f87171" 

        try:
            caminho_imagem = self.assets_dir / imagem_nome
            icone = tk.PhotoImage(file=caminho_imagem).subsample(2, 2) 
            self.icones_dias[dia_nome] = icone 
            tk.Label(dia_container, image=icone, bg=BG_CARTAO).pack(pady=20)
        except Exception:
            tk.Label(dia_container, text=simbolo_emoji, font=("Helvetica", 24), bg=BG_CARTAO, fg=cor_emoji).pack()

        tk.Label(dia_container, text=dia_nome, bg=BG_CARTAO, font=("Helvetica", 14)).pack(pady=(5, 0))

    def alternar_pausa(self):
        texto_atual = self.var_texto_botao_pausa.get()
        if texto_atual == "Pausa":
            self.app.sessao_controller.pausar_temporizador()
            self.var_texto_botao_pausa.set("Retomar")
        elif texto_atual == "Retomar":
            self.app.sessao_controller.iniciar_temporizador()
            self.var_texto_botao_pausa.set("Pausa")