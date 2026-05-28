import tkinter as tk
from tkinter import font as tkfont

# ==========================================
# CONSTANTES DE CORES
# ==========================================
BG_BRANCO = "white"
BG_CINZA_CLARO = "#f0f0f0"
BG_CINZA_ESCURO = "#D9D9D9"
BG_BOTAO_VERDE = "#a7f3d0"
BG_BOTAO_CINZA = "#c8d6ce"
COR_TEXTO = "#444444"
COR_TITULO = "#1A1A1A"


class CartaoTarefa(tk.Frame):
    """Componente reutilizável que representa uma única tarefa com seus detalhes."""
    
    def __init__(self, parent, nome_tarefa, tempo_info):
        super().__init__(parent, bg=BG_CINZA_CLARO)
        self.pack(fill="x", padx=40, pady=10)
        
        self.nome_tarefa = nome_tarefa
        self.tempo_info = tempo_info

        self._build_cabecalho()
        self._build_detalhes()

    def _build_cabecalho(self):
        """Monta a barra superior do cartão (Título e Botões principais)"""
        cabecalho = tk.Frame(self, bg=BG_CINZA_CLARO, padx=15, pady=10)
        cabecalho.pack(fill="x")

        # Botão do título que funciona como sanfona (abre/fecha detalhes)
        tk.Button(
            cabecalho, 
            text=self.nome_tarefa, 
            font=("Helvetica", 14, "bold"), 
            bg=BG_CINZA_CLARO, 
            relief="flat", 
            cursor="hand2", 
            command=self.alternar_detalhes
        ).pack(side="left")

        tk.Label(cabecalho, text=self.tempo_info, bg=BG_CINZA_CLARO, fg="#555555").pack(side="left", padx=20)

        tk.Button(cabecalho, text="excluir", bg="#bcbcbc", relief="flat").pack(side="right", padx=(10, 0))
        tk.Button(cabecalho, text="Iniciar", bg=BG_BOTAO_CINZA, relief="flat").pack(side="right")

    def _build_detalhes(self):
        """Monta a área inferior do cartão (escondida por padrão)"""
        self.detalhes = tk.Frame(self, bg=BG_CINZA_ESCURO, padx=15, pady=15)
        # Note que NÃO damos .pack() aqui, para que ele nasça fechado.

        coluna_esquerda = tk.Frame(self.detalhes, bg=BG_CINZA_ESCURO)
        coluna_esquerda.pack(side="left", anchor="nw") 

        coluna_direita = tk.Frame(self.detalhes, bg=BG_CINZA_ESCURO)
        coluna_direita.pack(side="right", anchor="ne") 

        self._montar_jornada_e_desconforto(coluna_esquerda)
        self._montar_lembretes_e_resumo(coluna_direita)

    def _montar_jornada_e_desconforto(self, parent):
        # 1. Jornada
        tk.Label(parent, text="🕒 Jornada de trabalho", bg=BG_CINZA_ESCURO).pack(anchor="w", pady=(0, 5))
        botoes_jornada = tk.Frame(parent, bg=BG_CINZA_ESCURO)
        botoes_jornada.pack(anchor="w")

        for horas in ["4h", "6h", "8h"]:
            tk.Button(botoes_jornada, text=horas, bg=BG_BOTAO_CINZA, relief="flat").pack(side="left", padx=(0 if horas=="4h" else 5, 5))
        tk.Entry(botoes_jornada, bg=BG_BOTAO_CINZA, width=4).pack(side="left", padx=5)

        # 2. Desconforto
        tk.Label(parent, text="🧍 Onde sente desconforto?", bg=BG_CINZA_ESCURO).pack(anchor="w", pady=(15, 5))
        botoes_desconforto = tk.Frame(parent, bg=BG_CINZA_ESCURO)
        botoes_desconforto.pack(anchor="w")

        for local in ["Ombros", "Costas", "Mãos", "Olhos"]:
            tk.Button(botoes_desconforto, text=local, bg=BG_BOTAO_CINZA, relief="flat").pack(side="left", padx=(0 if local=="Ombros" else 5, 5))
        
        tk.Button(parent, text="Nenhum", bg=BG_BOTAO_CINZA, relief="flat").pack(anchor="w", pady=(5, 0))

    def _montar_lembretes_e_resumo(self, parent):
        # 1. Lembretes
        tk.Label(parent, text="🔔 Lembrar a cada", bg=BG_CINZA_ESCURO).pack(anchor="w", pady=(0, 5))
        botoes_lembrete = tk.Frame(parent, bg=BG_CINZA_ESCURO)
        botoes_lembrete.pack(anchor="w") 

        for min in ["25m", "30m", "50m"]:
            tk.Button(botoes_lembrete, text=min, bg=BG_BOTAO_CINZA, relief="flat").pack(side="left", padx=(0 if min=="25m" else 5, 5))
        tk.Entry(botoes_lembrete, bg=BG_BOTAO_CINZA, width=4).pack(side="left", padx=5)

        # 2. Resumo da Sessão
        caixa_resumo = tk.Frame(parent, bg=BG_BRANCO, padx=15, pady=15)
        caixa_resumo.pack(anchor="w", fill="x", pady=(20, 0))

        tk.Label(caixa_resumo, text="Resumo da sessão", bg=BG_BRANCO, fg="#555555", font=("Helvetica", 10)).pack(anchor="w")
        tk.Label(caixa_resumo, text="6h de jornada · pausa a cada 30 min", bg=BG_BRANCO, font=("Helvetica", 12, "bold")).pack(anchor="w", pady=(2, 5))
        tk.Label(caixa_resumo, text="Foco inicial: Ombros", bg=BG_BRANCO, fg=COR_TEXTO, font=("Helvetica", 10)).pack(anchor="w")

    def alternar_detalhes(self):
        """Lógica para abrir e fechar o cartão"""
        if self.detalhes.winfo_ismapped():
            self.detalhes.pack_forget() 
        else:
            self.detalhes.pack(fill="x") 


# ==========================================
# PÁGINA PRINCIPAL
# ==========================================
class HomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=BG_CINZA_ESCURO)
        self.f_titulo = tkfont.Font(family="Helvetica", size=24, weight="bold")
        self._build()

    def _build(self):
        # Título da página
        tk.Label(
            self,
            text="Página inicial - Saúde e Produtividade",
            bg=BG_CINZA_ESCURO,
            fg=COR_TITULO,
            font=self.f_titulo,
        ).pack(anchor="w", pady=(20, 20))

        # Contorno principal (Caixa branca)
        self.contorno = tk.Frame(self, bg=BG_BRANCO, width=1400, height=700)
        self.contorno.pack(anchor="c", expand=True, fill="both") 
        self.contorno.pack_propagate(False) 

        self._build_area_input()
        self._build_lista_tarefas()

    def _build_area_input(self):
        """Monta a barra superior de adicionar tarefa"""
        frame_topo = tk.Frame(self.contorno, bg=BG_BRANCO)
        frame_topo.pack(pady=20, fill="x", padx=40)

        campo_tarefa = tk.Entry(frame_topo, font=("Helvetica", 14))
        campo_tarefa.pack(side="left", ipady=8, padx=(0, 20), fill="x", expand=True)

        tk.Button(
            frame_topo, 
            text="+ Adicionar", 
            bg=BG_BOTAO_VERDE, 
            font=("Helvetica", 12, "bold"),
            relief="flat", 
            padx=20, pady=5
        ).pack(side="right")

    def _build_lista_tarefas(self):
        """Instancia os cartões de tarefa na tela"""
        
        # Veja como fica MUITO mais fácil adicionar tarefas agora!
        CartaoTarefa(self.contorno, nome_tarefa="Fazer atividade X", tempo_info="⏱ 6h   🔔 30mx12")
        
        # Se quiser adicionar outra no futuro, é só descomentar a linha abaixo:
        # CartaoTarefa(self.contorno, nome_tarefa="Reunião de Alinhamento", tempo_info="⏱ 1h   🔔 0m")