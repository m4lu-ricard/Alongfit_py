import sys
import os
import tkinter as tk

caminho_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(caminho_raiz)

from controller.config_controller import ConfigController
from controller.sessao_controller import SessaoController

# ... (suas outras importações)
from alongamento_page import AlongamentoPage  # Importe a página nova aqui
from config_page import ConfigPage
from home_page import HomePage
from sidebar import Sidebar
from stats_page import StatsPage
from timer_page import TimerPage

PAGES = {
    "home": HomePage,
    "stats": StatsPage,
    "timer": TimerPage,
    "config": ConfigPage,
    "alongamento": AlongamentoPage,
}

def rodar_app():
    app = AlongFitApp()
    app.mainloop()

class AlongFitApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("AlongFit")
        self.geometry("700x450")
        self.minsize(500, 350)
        self.configure(bg="#FFFFFF")

        self.content = tk.Frame(self, bg="#FFFFFF")
        self.content.pack(side="right", fill="both", expand=True)

        self.sidebar = Sidebar(self, on_select=self.show_page, active_page="timer")
        self.sidebar.pack(side="left", fill="y")

        # 1. SIMULANDO O USUÁRIO LOGADO (Ana Souza, ID 1)
        self.id_usuario_logado = 1 

        # 2. INSTANCIANDO OS CONTROLADORES GLOBAIS
        self.config_controller = ConfigController(self.id_usuario_logado)
        self.sessao_controller = SessaoController(self, self.id_usuario_logado)

        self.content = tk.Frame(self, bg="#FFFFFF")
        self.content.pack(side="right", fill="both", expand=True)

        self.current_page = None
        self.show_page("home")



    def show_page(self, page_name):
        if self.current_page is not None:
            self.current_page.destroy()

        page_class = PAGES[page_name]
        
        # Adicione o "alongamento" nesta lista:
        if page_name in ["home", "timer", "alongamento"]:
            self.current_page = page_class(self.content, app=self)
        else:
            self.current_page = page_class(self.content)
            
        self.current_page.pack(fill="both", expand=True)


if __name__ == "__main__":
    try:
        import hupper

        # 2. O hupper assume o controle, vigia os arquivos .py 
        # e reinicia a função 'rodar_app' se algo mudar
        print("Hot Reload Ativo! Monitorando alterações...")
        reloader = hupper.start_reloader("app.rodar_app")
        
    except ImportError:
        # Caso o hupper não esteja instalado, o app roda normalmente
        rodar_app()