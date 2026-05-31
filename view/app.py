import sys
import os
import tkinter as tk

caminho_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(caminho_raiz)

from controller.config_controller import ConfigController
from controller.sessao_controller import SessaoController

from alongamento_page import AlongamentoPage
from config_page import ConfigPage
from home_page import HomePage
from sidebar import Sidebar
from stats_page import StatsPage
from timer_page import TimerPage
from LoginPage import LoginPage
from CadastroPage import CadastroPage

PAGES = {
    "login": LoginPage,
    "cadastro": CadastroPage,
    "home": HomePage,
    "stats": StatsPage,
    "timer": TimerPage,
    "config": ConfigPage,
    "alongamento": AlongamentoPage,
}

PAGES_COM_APP = {"login", "cadastro", "home", "timer", "alongamento", "config", "stats"}


def rodar_app():
    app = AlongFitApp()
    app.mainloop()


class AlongFitApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("AlongFit")
        self.configure(bg="#FFFFFF")
        
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        
        largura_app = int(largura_tela * 0.85)
        altura_app = int(altura_tela * 0.85)
        
        pos_x = (largura_tela // 2) - (largura_app // 2)
        pos_y = (altura_tela // 2) - (altura_app // 2)
        
        self.geometry(f"{largura_app}x{altura_app}+{pos_x}+{pos_y}")
        self.minsize(800, 600) 

        self.config_tema_escuro     = False
        self.config_sons            = True
        self.config_hidratacao      = False
        self.config_frequencia_agua = "A cada 1 hora"

        self.id_usuario_logado = None  

        self.config_controller = None
        self.sessao_controller = None

        self.sidebar = Sidebar(self, on_select=self.show_page, active_page="home")

        self.content = tk.Frame(self, bg="#FFFFFF")
        self.content.pack(side="right", fill="both", expand=True)

        self.current_page = None
        
        self.show_page("login")

    def inicializar_sistema_pos_login(self, id_usuario):
        self.id_usuario_logado = id_usuario
        
        self.config_controller = ConfigController(self.id_usuario_logado)
        self.sessao_controller = SessaoController(self, self.id_usuario_logado)
        
        self.content.pack_forget()
        self.sidebar.pack(side="left", fill="y")
        self.content.pack(side="right", fill="both", expand=True)
        
        self.show_page("home")

    def deslogar_usuario(self):
        if self.sessao_controller:
            self.sessao_controller.pausar_temporizador()
            
        self.id_usuario_logado = None
        self.config_controller = None
        self.sessao_controller = None
        
        self.sidebar.pack_forget()
        self.show_page("login")

    def show_page(self, page_name):
        if self.current_page is not None:
            self.current_page.destroy()

        page_class = PAGES[page_name]
        self.current_page = page_class(self.content, app=self)
        self.current_page.pack(fill="both", expand=True)

        self.aplicar_tema_global()

    def aplicar_tema_global(self):
        escuro = self.config_tema_escuro
        cor_raiz    = "#AEB9B0" if escuro else "#EEF4EF"
        cor_content = "#AEB9B0" if escuro else "#EEF4EF"

        self.configure(bg=cor_raiz)
        self.content.configure(bg=cor_content)

        if hasattr(self.sidebar, 'aplicar_tema'):
            self.sidebar.aplicar_tema(escuro)

        if self.current_page and hasattr(self.current_page, 'aplicar_tema'):
            self.current_page.aplicar_tema(escuro)


if __name__ == "__main__":

    rodar_app()
