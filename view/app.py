import tkinter as tk

from config_page import ConfigPage
from home_page import HomePage
from sidebar import Sidebar
from stats_page import StatsPage
from timer_page import TimerPage

#app.py pra rodar o tkinter

PAGES = {
    "home": HomePage,
    "stats": StatsPage,
    "timer": TimerPage,
    "config": ConfigPage,
}


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

        self.current_page = None
        self.show_page("timer")

    def show_page(self, page_name):
        if self.current_page is not None:
            self.current_page.destroy()

        page_class = PAGES[page_name]
        self.current_page = page_class(self.content)
        self.current_page.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = AlongFitApp()
    app.mainloop()
