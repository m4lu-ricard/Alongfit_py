import tkinter as tk


class StatsPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#D9D9D9")

        tk.Label(
            self,
            text="Stats",
            bg="#FFFFFF",
            fg="#1A1A1A",
            font=("Helvetica", 24, "bold"),
        ).pack(pady=(60, 10))

        tk.Label(
            self,
            text="Aqui vao aparecer suas estatisticas.",
            bg="#FFFFFF",
            fg="#444444",
            font=("Helvetica", 13),
        ).pack()
