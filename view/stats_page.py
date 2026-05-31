import tkinter as tk
from tkinter import ttk
from datetime import datetime
import sys
import os

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from controller.estatisticas_controller import EstatisticasController

BG_BRANCO = "#FFFFFF"
BG_CINZA_ESCURO = "#EEF4EF"
COR_TITULO = "#000000"
COR_TEXTO = "#000000"


class StatsPage(tk.Frame):
    def __init__(self, parent, app=None):
        super().__init__(parent, bg=BG_CINZA_ESCURO)
        self.app = app
        self.controller = EstatisticasController(self.app.id_usuario_logado)
        
        self._build()

        if hasattr(self.app, 'config_tema_escuro'):
            self.aplicar_tema(self.app.config_tema_escuro)

    def _build(self):
        self.lbl_titulo = tk.Label(
            self, text="Estatísticas", bg=BG_CINZA_ESCURO,
            fg=COR_TITULO, font=("Helvetica", 24, "bold")
        )
        self.lbl_titulo.pack(anchor="w", padx=20, pady=(20, 10))

        self.contorno = tk.Frame(self, bg=BG_BRANCO, highlightthickness=1)
        self.contorno.pack(expand=True, fill="both", padx=20, pady=(0, 20))

        self._build_topo()
        self._build_grafico()

    def _build_topo(self):
        self.topo = tk.Frame(self.contorno, bg=BG_BRANCO)
        self.topo.pack(fill="x", padx=30, pady=20)

        self.lbl_mes = tk.Label(
            self.topo, text="Selecionar mês:", bg=BG_BRANCO,
            fg=COR_TEXTO, font=("Helvetica", 12)
        )
        self.lbl_mes.pack(side="left")

        self.combo_mes = ttk.Combobox(self.topo, state="readonly", width=15)
        self.combo_mes["values"] = [str(i) for i in range(1, 13)]
        self.combo_mes.pack(side="left", padx=10)
        self.combo_mes.set(str(datetime.now().month))
        self.combo_mes.bind("<<ComboboxSelected>>", self.atualizar_grafico)

    def _build_grafico(self):
        self.frame_grafico = tk.Frame(self.contorno, bg="white")
        self.frame_grafico.pack(fill="both", expand=True, padx=20, pady=20)
        self.criar_grafico()

    def criar_grafico(self):
        for widget in self.frame_grafico.winfo_children():
            widget.destroy()

        mes = self.combo_mes.get()

        try:
            dias, qtd_alongamentos, minutos = self.controller.buscar_dados_mes(mes)
        except AttributeError:
            print("Aviso: O método 'buscar_dados_mes' ainda não existe no EstatisticasController.")
            dias, qtd_alongamentos, minutos = [], [], []

        escuro = getattr(self.app, 'config_tema_escuro', False)
        bg_color = "#F8FAF7" if escuro else "white"
        text_color = "black"

        if not dias:
            tk.Label(
                self.frame_grafico, text="Nenhum dado encontrado neste mês",
                font=("Helvetica", 14), bg=bg_color, fg=text_color
            ).pack(expand=True)
            return

        fig = Figure(figsize=(10, 5), dpi=100, facecolor=bg_color)
        ax = fig.add_subplot(111)
        ax.set_facecolor(bg_color)

        x = list(range(len(dias)))
        largura = 0.35

        ax.bar(
            [i - largura/2 for i in x], qtd_alongamentos,
            width=largura, label="Qtd. Alongamentos", color="#a7f3d0"
        )


        ax.bar(
            [i + largura/2 for i in x], minutos,
            width=largura, label="Tempo Total (min)", color="#4A9EFF"
        )

        ax.set_title(f"Alongamentos - Mês {mes}", color=text_color)
        ax.set_xlabel("Dias", color=text_color)
        ax.set_ylabel("Quantidade / Minutos", color=text_color)

        ax.set_xticks(x)
        ax.set_xticklabels(dias, color=text_color)
        ax.tick_params(axis='y', colors=text_color)
        
        for spine in ax.spines.values():
            spine.set_edgecolor(text_color)

        ax.grid(True, alpha=0.2)
        
        legenda = ax.legend(facecolor=bg_color, edgecolor=text_color)
        for text in legenda.get_texts():
            text.set_color(text_color)

        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.frame_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def atualizar_grafico(self, event=None):
        self.criar_grafico()

    def aplicar_tema(self, escuro: bool):
        cor_fundo  = "#AEB9B0" if escuro else BG_CINZA_ESCURO
        cor_cartao = "#F8FAF7" if escuro else BG_BRANCO
        cor_borda  = "#7F8C82" if escuro else "#D9E4DA"
        cor_texto  = "#000000"
        cor_texto_sec = "#000000"

        self.configure(bg=cor_fundo)
        self.lbl_titulo.configure(bg=cor_fundo, fg=cor_texto)
        self.contorno.configure(bg=cor_cartao, highlightbackground=cor_borda,
                                highlightcolor=cor_borda)
        self.topo.configure(bg=cor_cartao)
        self.lbl_mes.configure(bg=cor_cartao, fg=cor_texto_sec)
        self.frame_grafico.configure(bg=cor_cartao)

        self.criar_grafico()
