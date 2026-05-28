import tkinter as tk
from pathlib import Path

class PopUp(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        
        # 1. Configurações base da janela
        self.geometry("280x320")
        self.configure(bg="#9FE59E") # Fundo verde (que servirá de borda e topo)
        
        # O SEGREDO: Remove a barra padrão do Windows/Mac para criarmos a nossa
        self.overrideredirect(True) 

        # Variáveis para guardar a posição do clique do mouse (para arrastar a janela)
        self._x_mouse = 0
        self._y_mouse = 0

        # Caminho da imagem
        self.assets_dir = Path(__file__).resolve().parent.parent / "assets"

        # 2. Constrói as partes da tela
        self._build_barra_superior()
        self._build_cartao_principal()

        # 3. Centraliza o pop-up na tela do computador
        self._centralizar()

    def _build_barra_superior(self):
        """Cria a nossa própria barra de título verde customizada"""
        topo = tk.Frame(self, bg="#9FE59E")
        topo.pack(fill="x", padx=10, pady=5)

        # MÁGICA: Conecta o clique e o arrastar do mouse ao Frame topo
        topo.bind("<Button-1>", self._iniciar_movimento)
        topo.bind("<B1-Motion>", self._mover_janela)

        # Tenta carregar a logo. Se der erro (caminho errado), não trava o app.
        try:
            caminho_logo = self.assets_dir / "logo.png"
            self.logo_photo = tk.PhotoImage(file=caminho_logo).subsample(3, 3)
            
            # Conecta o clique na logo também
            lbl_logo = tk.Label(topo, image=self.logo_photo, bg="#9FE59E")
            lbl_logo.pack(side="left")
            lbl_logo.bind("<Button-1>", self._iniciar_movimento)
            lbl_logo.bind("<B1-Motion>", self._mover_janela)
        except Exception:
            pass 

        # Conecta o clique no texto "AlongFit" também
        lbl_texto = tk.Label(topo, text="AlongFit", bg="#9FE59E", font=("Helvetica", 10, "bold"))
        lbl_texto.pack(side="left", padx=5)
        lbl_texto.bind("<Button-1>", self._iniciar_movimento)
        lbl_texto.bind("<B1-Motion>", self._mover_janela)

        # Botão X para fechar
        tk.Button(
            topo, 
            text="X", 
            bg="#9FE59E", 
            fg="black", 
            font=("Helvetica", 12, "bold"),
            relief="flat", 
            cursor="hand2",
            activebackground="#9FE59E",
            command=self.destroy # Destrói a janela ao clicar
        ).pack(side="right")

    def _build_cartao_principal(self):
        """Cria a área branca com o cronômetro"""
        cartao = tk.Frame(self, bg="white")
        # O padx=5 e pady=5 deixam um "vazamento" do fundo verde, criando a borda!
        cartao.pack(fill="both", expand=True, padx=5, pady=(0, 5))

        # Tempo grande
        tk.Label(
            cartao, 
            text="14:04", 
            bg="white", 
            fg="black", 
            font=("Helvetica", 64, "bold")
        ).pack(pady=(40, 10))

        # Status
        tk.Label(
            cartao, 
            text="Em andamento...", 
            bg="white", 
            fg="#1A1A1A", 
            font=("Helvetica", 14)
        ).pack(pady=(0, 30))

        # Área dos botões
        frame_botoes = tk.Frame(cartao, bg="white")
        frame_botoes.pack(pady=10)

        tk.Button(
            frame_botoes, 
            text="Pausar", 
            bg="#e8f5e9", # Verde bem clarinho
            font=("Helvetica", 12, "bold"),
            relief="flat", 
            padx=15, pady=5
        ).pack(side="left", padx=10)

        tk.Button(
            frame_botoes, 
            text="Concluir", 
            bg="#9FE59E", # Verde padrão
            font=("Helvetica", 12, "bold"),
            relief="flat", 
            padx=15, pady=5
        ).pack(side="left", padx=10)

    # ==========================================
    # FUNÇÕES DE LÓGICA DA JANELA
    # ==========================================

    def _centralizar(self):
        """Faz um cálculo matemático para o pop-up nascer no meio do monitor"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def _iniciar_movimento(self, event):
        """Salva a posição inicial do clique do mouse"""
        self._x_mouse = event.x
        self._y_mouse = event.y

    def _mover_janela(self, event):
        """Calcula para onde o mouse foi e arrasta a janela junto"""
        x_atual = self.winfo_x()
        y_atual = self.winfo_y()
        
        novo_x = x_atual + (event.x - self._x_mouse)
        novo_y = y_atual + (event.y - self._y_mouse)
        
        self.geometry(f"+{novo_x}+{novo_y}")


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal para testarmos só o pop-up
    
    # Chama o nosso Pop-up
    PopUp(root)
    
    root.mainloop()