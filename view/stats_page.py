import tkinter as tk


class StatsPage(tk.Frame):
    def __init__(self, parent, app=None):
        super().__init__(parent, bg="#D9D9D9")
        self.app = app

        self.lbl_titulo = tk.Label(
            self, text="Stats",
            bg="#D9D9D9", fg="#1A1A1A",
            font=("Helvetica", 24, "bold"),
        )
        self.lbl_titulo.pack(pady=(60, 10))

        self.lbl_sub = tk.Label(
            self, text="Aqui vão aparecer suas estatísticas.",
            bg="#D9D9D9", fg="#444444",
            font=("Helvetica", 13),
        )
        self.lbl_sub.pack()

        if self.app and hasattr(self.app, 'config_tema_escuro'):
            self.aplicar_tema(self.app.config_tema_escuro)

    def aplicar_tema(self, escuro: bool):
        cor_fundo = "#1E1E1E" if escuro else "#D9D9D9"
        cor_texto = "#FFFFFF" if escuro else "#1A1A1A"
        cor_sub   = "#AAAAAA" if escuro else "#444444"

        self.configure(bg=cor_fundo)
        self.lbl_titulo.configure(bg=cor_fundo, fg=cor_texto)
        self.lbl_sub.configure(bg=cor_fundo, fg=cor_sub)
