import tkinter as tk
from pathlib import Path
from tkinter import font as tkfont

BG_GERAL  = "#EEF4EF"
BG_CARTAO = "#FFFFFF"
COR_TEXTO = "#000000"
COR_TITULO = "#000000"


class TimerPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg=BG_GERAL)
        self.app = app
        self.assets_dir = Path(__file__).resolve().parent.parent / "assets"
        self.icones_dias = {}

        self.f_titulo        = tkfont.Font(family="Helvetica", size=24, weight="bold")
        self.f_cartao_titulo = tkfont.Font(family="Helvetica", size=32, weight="bold")
        self.f_cartao_texto  = tkfont.Font(family="Helvetica", size=32)

        self.var_nome_tarefa       = tk.StringVar(value="Trabalho em Foco")
        self.var_tempo_principal   = tk.StringVar(value="00:00")
        self.var_tempo_total       = tk.StringVar(value="0:00:00")
        self.var_texto_botao_pausa = tk.StringVar(value="Pausa")

        self._build()

        self.app.sessao_controller.vincular_interface_relogio(self.var_tempo_principal.set)
        self.app.sessao_controller.vincular_interface_tempo_total(self.var_tempo_total.set)

        if hasattr(self.app, 'config_tema_escuro'):
            self.aplicar_tema(self.app.config_tema_escuro)

    def _build(self):
        self.contorno = tk.Frame(self, bg=BG_GERAL)
        self.contorno.pack(expand=True, fill="both")

        # 1. CABEÇALHO (Ocupa a largura toda e serve para o título principal)
        self.cabecalho = tk.Frame(self.contorno, bg=BG_GERAL)
        self.cabecalho.pack(fill="x", padx=30)
        
        self.lbl_titulo_timer = tk.Label(
            self.cabecalho, text="Timer de Trabalho",
            bg=BG_GERAL, fg=COR_TITULO, font=self.f_titulo
        )
        self.lbl_titulo_timer.pack(pady=(30, 15), anchor="w")

        # 2. CORPO (Onde as colunas são divididas e começam exatamente na mesma altura)
        self.corpo = tk.Frame(self.contorno, bg=BG_GERAL)
        self.corpo.pack(expand=True, fill="both", padx=30, pady=(0, 30))

        self.coluna_esquerda = tk.Frame(self.corpo, bg=BG_GERAL)
        self.coluna_esquerda.pack(side="left", expand=True, fill="both", padx=(0, 15))
        
        self.coluna_direita = tk.Frame(self.corpo, bg=BG_GERAL)
        self.coluna_direita.pack(side="right", expand=True, fill="both", padx=(15, 0))

        self._build_timer_ativo()
        self._build_tempo_total_restante()
        self._build_progresso_semanal()

    def _build_timer_ativo(self):
        self.cartao_timer = tk.Frame(self.coluna_esquerda, bg=BG_CARTAO, highlightthickness=1)
        self.cartao_timer.pack(fill="both", expand=True)

        self.lbl_tarefa_titulo = tk.Label(
            self.cartao_timer, text="Tarefa em Andamento:",
            bg=BG_CARTAO, fg=COR_TEXTO, font=self.f_cartao_titulo
        )
        self.lbl_tarefa_titulo.pack(pady=(40, 0))

        self.lbl_nome_tarefa = tk.Label(
            self.cartao_timer, textvariable=self.var_nome_tarefa,
            bg=BG_CARTAO, fg=COR_TEXTO, font=self.f_cartao_texto
        )
        self.lbl_nome_tarefa.pack(pady=(0, 20))

        centro = tk.Frame(self.cartao_timer, bg=BG_CARTAO)
        centro.pack(expand=True)
        self.lbl_relogio = tk.Label(
            centro, textvariable=self.var_tempo_principal,
            bg=BG_CARTAO, fg=COR_TITULO, font=("Helvetica", 64, "bold")
        )
        self.lbl_relogio.pack()

        rodape = tk.Frame(self.cartao_timer, bg=BG_CARTAO)
        rodape.pack(side="bottom", fill="x", pady=40)
        self.rodape_timer = rodape

        caixa_botoes = tk.Frame(rodape, bg=BG_CARTAO)
        caixa_botoes.pack(anchor="c")
        self.caixa_botoes_timer = caixa_botoes

        tk.Button(
            caixa_botoes, textvariable=self.var_texto_botao_pausa,
            bg="#e5e7eb", fg="#000000", font=("Helvetica", 16), relief="flat",
            padx=30, pady=10, command=self.alternar_pausa
        ).pack(side="left", padx=10)

        tk.Button(
            caixa_botoes, text="Cancelar",
            bg="#e5e7eb", fg="#000000", font=("Helvetica", 16), relief="flat",
            padx=30, pady=10, command=self._cancelar_e_zerar_cronometro
        ).pack(side="left", padx=10)

    def _build_tempo_total_restante(self):
        self.cartao_total = tk.Frame(self.coluna_direita, bg=BG_CARTAO, highlightthickness=1)
        # O cartão agora expande perfeitamente com margem inferior
        self.cartao_total.pack(pady=(0, 15), fill="both", expand=True)

        self.lbl_total_titulo = tk.Label(
            self.cartao_total, text="Tempo Total Restante:",
            bg=BG_CARTAO, fg=COR_TEXTO, font=self.f_cartao_titulo
        )
        self.lbl_total_titulo.pack(pady=(40, 0))

        centro = tk.Frame(self.cartao_total, bg=BG_CARTAO)
        centro.pack(expand=True)
        self.centro_total = centro
        self.lbl_total_valor = tk.Label(
            centro, textvariable=self.var_tempo_total,
            bg=BG_CARTAO, fg=COR_TITULO, font=("Helvetica", 48, "bold")
        )
        self.lbl_total_valor.pack()

    def _build_progresso_semanal(self):
        self.cartao_semanal = tk.Frame(self.coluna_direita, bg=BG_CARTAO, highlightthickness=1)
        # O cartão agora expande perfeitamente com margem superior
        self.cartao_semanal.pack(pady=(15, 0), fill="both", expand=True)

        self.lbl_semanal_titulo = tk.Label(
            self.cartao_semanal, text="Progresso semanal",
            bg=BG_CARTAO, fg=COR_TITULO, font=self.f_cartao_titulo
        )
        self.lbl_semanal_titulo.pack(pady=(40, 30))

        caixa_dias = tk.Frame(self.cartao_semanal, bg=BG_CARTAO)
        caixa_dias.pack(anchor="c")
        self.caixa_dias = caixa_dias

        dias_concluidos = self.app.sessao_controller.obter_progresso_semanal()
        for indice, nome in enumerate(["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"]):
            self._build_icone_dia(caixa_dias, nome, indice in dias_concluidos)

    def _build_icone_dia(self, parent, dia_nome, fez_alongamento):
        dia_container = tk.Frame(parent, bg=BG_CARTAO)
        dia_container.pack(side="left", padx=10) # Reduzido ligeiramente para caber melhor em ecrãs menores
        imagem_nome = "verificado.png" if fez_alongamento else "triste.png"
        simbolo = "✅" if fez_alongamento else "❌"
        cor_emoji = "#4ade80" if fez_alongamento else "#f87171"
        try:
            caminho = self.assets_dir / imagem_nome
            icone = tk.PhotoImage(file=caminho).subsample(2, 2)
            self.icones_dias[dia_nome] = icone
            tk.Label(dia_container, image=icone, bg=BG_CARTAO).pack(pady=20)
        except Exception:
            tk.Label(dia_container, text=simbolo, font=("Helvetica", 24),
                     bg=BG_CARTAO, fg=cor_emoji).pack()
        tk.Label(dia_container, text=dia_nome, bg=BG_CARTAO,
                 fg="#000000", font=("Helvetica", 14)).pack(pady=(5, 0))

    def alternar_pausa(self):
        if self.var_texto_botao_pausa.get() == "Pausa":
            self.app.sessao_controller.pausar_temporizador()
            self.var_texto_botao_pausa.set("Retomar")
        else:
            self.app.sessao_controller.iniciar_temporizador()
            self.var_texto_botao_pausa.set("Pausa")

    def aplicar_tema(self, escuro: bool):
        cor_geral  = "#AEB9B0" if escuro else BG_GERAL
        cor_cartao = "#F8FAF7" if escuro else BG_CARTAO
        cor_texto  = "#000000"
        cor_titulo = "#000000"
        cor_botoes = "#DDE8DF" if escuro else "#E9EFEA"
        cor_borda  = "#7F8C82" if escuro else "#D9E4DA"

        self.configure(bg=cor_geral)
        self.contorno.configure(bg=cor_geral)
        self.cabecalho.configure(bg=cor_geral)
        self.corpo.configure(bg=cor_geral)
        self.coluna_esquerda.configure(bg=cor_geral)
        self.coluna_direita.configure(bg=cor_geral)
        self.lbl_titulo_timer.configure(bg=cor_geral, fg=cor_titulo)

        for w in [self.cartao_timer, self.rodape_timer, self.caixa_botoes_timer]:
            w.configure(bg=cor_cartao)
        for cartao in [self.cartao_timer, self.cartao_total, self.cartao_semanal]:
            cartao.configure(highlightbackground=cor_borda, highlightcolor=cor_borda)
        for lbl in [self.lbl_tarefa_titulo, self.lbl_nome_tarefa]:
            lbl.configure(bg=cor_cartao, fg=cor_texto)
        self.lbl_relogio.configure(bg=cor_cartao, fg=cor_titulo)
        for filho in self.caixa_botoes_timer.winfo_children():
            filho.configure(bg=cor_botoes, fg=cor_titulo,
                            activebackground=cor_botoes, activeforeground=cor_titulo)

        self.cartao_total.configure(bg=cor_cartao)
        self.centro_total.configure(bg=cor_cartao)
        self.lbl_total_titulo.configure(bg=cor_cartao, fg=cor_texto)
        self.lbl_total_valor.configure(bg=cor_cartao, fg=cor_titulo)

        self.cartao_semanal.configure(bg=cor_cartao)
        self.caixa_dias.configure(bg=cor_cartao)
        self.lbl_semanal_titulo.configure(bg=cor_cartao, fg=cor_titulo)
        for dia_container in self.caixa_dias.winfo_children():
            dia_container.configure(bg=cor_cartao)
            for filho in dia_container.winfo_children():
                filho.configure(bg=cor_cartao, fg=cor_titulo)
    
    def _cancelar_e_zerar_cronometro(self):
        if self.app and self.app.sessao_controller:
            self.app.sessao_controller.pausar_temporizador()
            self.app.sessao_controller.tempo_restante_segundos = 0
            self.app.sessao_controller.tempo_trabalho_total_restante = 0
            self.app.sessao_controller.atualizar_interface_relogio()
