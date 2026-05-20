import tkinter as tk


class HomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#FFFFFF")

        tk.Label(
            self,
            text="Home",
            bg="#FFFFFF",
            fg="#1A1A1A",
            font=("Helvetica", 24, "bold"),
        ).pack(pady=(60, 10))

        tk.Label(
            self,
            text="Bem-vinda ao AlongFit.",
            bg="#FFFFFF",
            fg="#444444",
            font=("Helvetica", 13),
        ).pack()
