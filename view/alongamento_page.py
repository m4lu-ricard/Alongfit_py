import tkinter as tk
from tkinter import font as tkfont

class AlongamentoPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="#d9d9d9")
        self.app = app

        # Fontes grandes para visualização de longe
        self.f_titulo = tkfont.Font(family="Helvetica", size=36, weight="bold")
        self.f_descricao = tkfont.Font(family="Helvetica", size=24)
        self.f_relogio = tkfont.Font(family="Helvetica", size=80, weight="bold")

        # Variáveis dinâmicas para o texto e tempo
        self.var_nome = tk.StringVar(value="Preparando...")
        self.var_descricao = tk.StringVar(value="...")
        self.var_tempo = tk.StringVar(value="00:00")

        self.tempo_restante = 0
        self.timer_id = None

        self._build()

    def _build(self):
        # Cartão branco centralizado
        caixa = tk.Frame(self, bg="white", padx=50, pady=50)
        caixa.pack(expand=True)

        tk.Label(caixa, text="✨ Hora de Alongar! ✨", font=("Helvetica", 20, "bold"), fg="#a7f3d0", bg="white").pack(pady=(0, 10))
        tk.Label(caixa, textvariable=self.var_nome, font=self.f_titulo, fg="#1A1A1A", bg="white").pack(pady=10)
        tk.Label(caixa, textvariable=self.var_descricao, font=self.f_descricao, fg="#444444", bg="white").pack(pady=20)
        
        # Relógio
        tk.Label(caixa, textvariable=self.var_tempo, font=self.f_relogio, fg="#1A1A1A", bg="white").pack(pady=40)

        # Botão caso a pessoa queira pular
        tk.Button(
            caixa, 
            text="Pular Alongamento", 
            bg="#e5e7eb", 
            font=("Helvetica", 16), 
            relief="flat", 
            padx=20, pady=10,
            command=self.finalizar_alongamento
        ).pack(pady=10)

    def iniciar_alongamento(self, alongamento):
        """Recebe os dados do banco, exibe na tela e inicia a contagem"""
        self.var_nome.set(alongamento.nome)
        self.var_descricao.set(alongamento.descricao)
        self.tempo_restante = alongamento.duracao
        self.atualizar_interface()
        self.contar_tempo()

    def contar_tempo(self):
        """Loop que reduz 1 segundo e se chama novamente"""
        if self.tempo_restante > 0:
            self.tempo_restante -= 1
            self.atualizar_interface()
            self.timer_id = self.after(1000, self.contar_tempo)
        else:
            self.finalizar_alongamento()

    def atualizar_interface(self):
        # Transforma os segundos do banco de dados (ex: 30) em "00:30"
        minutos, segundos = divmod(self.tempo_restante, 60)
        self.var_tempo.set(f"{minutos:02d}:{segundos:02d}")

    def finalizar_alongamento(self):
        """Para o timer e avisa o controller para voltar à página inicial"""
        if self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        
        self.app.sessao_controller.finalizar_pausa_alongamento()