import tkinter as tk
from pathlib import Path

from tkinter import font as tkfont

#SIDEBAR

# CORES 
SIDEBAR_BG  = "#FFFFFF"
CARD_BG     = "#FFFFFF"
TEXT_DARK   = "#1A1A1A"
BTN_HOVER   = "#C8C8C8"

# BOTÕES
# (nome_da_pagina, arquivo_da_imagem)
MENU_ITEMS = [
    ("home", "homeLogo.png"),
    ("stats", "status.png"),
    ("timer", "timer.png"),
    ("config", "config.png"),
]
ACTIVE_PAGE = "timer"


class Sidebar(tk.Frame):
    def __init__(self, parent, on_select=None, active_page=ACTIVE_PAGE, **kwargs):
        super().__init__(parent, bg=SIDEBAR_BG, width=120, **kwargs)
        self.pack_propagate(False)

        self.on_select = on_select
        self.active_page = active_page
        self.buttons = {}
        self.menu_icons = {}
        # Caminho absoluto da pasta assets.
        # Usar Path evita problemas de caminho entre sistemas operacionais
        self.assets_dir = Path(__file__).resolve().parent.parent / "assets"

        self.f_logo  = tkfont.Font(family="Helvetica", size=14, weight="bold")
        self.f_item  = tkfont.Font(family="Helvetica", size=11)

        # Monta todos os componentes visuais da sidebar
        self._build()

    def _build(self):
        # Container da área da logo
        logo_frame = tk.Frame(self, bg=SIDEBAR_BG)
        logo_frame.pack(pady=(20, 16), padx=10, anchor="w")

        # Carrega a imagem da logo da pasta assets
        logo_path = self.assets_dir / "logo.png"
        # subsample reduz o tamanho da imagem
        # (2,2) significa reduzir pela metade horizontal e verticalmente
        self.logo_photo = tk.PhotoImage(file=logo_path).subsample(2, 2)

        tk.Label(
            logo_frame,
            image=self.logo_photo,
            bg=SIDEBAR_BG
            ).pack(side="left")
        tk.Label(logo_frame, text="AlongFit", bg=SIDEBAR_BG,
                 font=self.f_logo, fg=TEXT_DARK).pack(side="left", padx=4)

        # Cria os botões do menu
        for page_name, image_name in MENU_ITEMS:
            self._menu_button(page_name, image_name)

    def _menu_button(self, page_name, image_name):
        # Verifica se o botão atual é a página ativa
        active = page_name == self.active_page
        bg_normal = CARD_BG if active else SIDEBAR_BG

        container = tk.Frame(self, bg=bg_normal, cursor="hand2",
                             padx=10, pady=10)
        container.pack(padx=10, pady=4)

        # Carrega o ícone do botão
        icon = tk.PhotoImage(file=self.assets_dir / image_name)
        # Guarda referência da imagem 
        self.menu_icons[page_name] = icon

        icon_label = tk.Label(container, image=icon, bg=bg_normal)
        icon_label.pack()
        self.buttons[page_name] = (container, icon_label)

        # Eventos de hover e clique.
        def on_enter(e):
            if page_name != self.active_page:
                container.configure(bg=BTN_HOVER)
                icon_label.configure(bg=BTN_HOVER)

        def on_leave(e):
            if page_name != self.active_page:
                container.configure(bg=SIDEBAR_BG)
                icon_label.configure(bg=SIDEBAR_BG)

        def on_click(e):
            self.select_page(page_name)

        # Aplica os eventos tanto no container quanto na imagem
        for widget in (container, icon_label):
            widget.bind("<Enter>", on_enter)
            widget.bind("<Leave>", on_leave)
            widget.bind("<Button-1>", on_click)

    def select_page(self, page_name):
        # Atualiza visualmente qual página está selecionada
        self.active_page = page_name
        self._refresh_buttons()

        if self.on_select:
            self.on_select(page_name)

    def _refresh_buttons(self):
        # Atualiza as cores dos botões baseado na página ativa
        for page_name, (container, icon_label) in self.buttons.items():
            bg = CARD_BG if page_name == self.active_page else SIDEBAR_BG
            container.configure(bg=bg)
            icon_label.configure(bg=bg)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sidebar – AlongFit")
    root.geometry("140x400")
    root.resizable(False, False)
    root.configure(bg=SIDEBAR_BG)

    sidebar = Sidebar(root)
    sidebar.pack(side="left", fill="y")

    root.mainloop()
