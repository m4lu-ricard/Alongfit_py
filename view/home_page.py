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

# ==========================================
# COMPONENTE: CARTÃO DE TAREFA
# ==========================================
# In home_page.py

class CartaoTarefa(tk.Frame):
    def __init__(self, parent, nome_tarefa, tempo_info, app, jornada_id=None): 
        super().__init__(parent, bg=BG_CINZA_CLARO)
        self.app = app 
        self.nome_tarefa = nome_tarefa
        
        # Determine initial values based on tempo_info string or default
        # (A more robust solution would pass these in directly instead of parsing a string)
        self.horas_trabalho_iniciais = 6 
        self.minutos_pausa_iniciais = 30
        
        # --- Create unique variables for THIS specific card ---
        self.var_horas_jornada = tk.IntVar(value=self.horas_trabalho_iniciais)
        self.var_minutos_lembrete = tk.IntVar(value=self.minutos_pausa_iniciais)
        self.var_id_dor = tk.IntVar(value=0) # Default to 'Nenhum'
        
        # Display text variable
        self.var_tempo_info = tk.StringVar(value=tempo_info)
        
        # Optional: Store an ID if this represents an existing database record
        self.jornada_id = jornada_id
        
        self.pack(fill="x", padx=40, pady=10)

        self._build_cabecalho()
        self._build_detalhes()

    def _build_cabecalho(self):
        cabecalho = tk.Frame(self, bg=BG_CINZA_CLARO, padx=15, pady=10)
        cabecalho.pack(fill="x")

        tk.Button(
            cabecalho, 
            text=self.nome_tarefa, 
            font=("Helvetica", 14, "bold"), 
            bg=BG_CINZA_CLARO, 
            relief="flat", 
            cursor="hand2", 
            command=self.alternar_detalhes
        ).pack(side="left")

        # Connect the display label to the dynamic variable
        tk.Label(cabecalho, textvariable=self.var_tempo_info, bg=BG_CINZA_CLARO, fg="#555555").pack(side="left", padx=20)

        tk.Button(cabecalho, text="excluir", bg="#bcbcbc", relief="flat").pack(side="right", padx=(10, 0))
        
        tk.Button(
            cabecalho, 
            text="Iniciar", 
            bg=BG_BOTAO_CINZA, 
            relief="flat",
            command=self.acao_iniciar_tarefa
        ).pack(side="right")

    def _build_detalhes(self):
        self.detalhes = tk.Frame(self, bg=BG_CINZA_ESCURO, padx=15, pady=15)

        coluna_esquerda = tk.Frame(self.detalhes, bg=BG_CINZA_ESCURO)
        coluna_esquerda.pack(side="left", anchor="nw") 

        coluna_direita = tk.Frame(self.detalhes, bg=BG_CINZA_ESCURO)
        coluna_direita.pack(side="right", anchor="ne") 

        self._montar_jornada_e_desconforto(coluna_esquerda)
        self._montar_lembretes_e_resumo(coluna_direita)

    def _montar_jornada_e_desconforto(self, parent):
        tk.Label(parent, text="🕒 Jornada de trabalho", bg=BG_CINZA_ESCURO).pack(anchor="w", pady=(0, 5))
        botoes_jornada = tk.Frame(parent, bg=BG_CINZA_ESCURO)
        botoes_jornada.pack(anchor="w")

        # Create quick-select buttons that update the variable
        for horas in [4, 6, 8]:
            tk.Button(botoes_jornada, text=f"{horas}h", bg=BG_BOTAO_CINZA, relief="flat",
                      command=lambda h=horas: self._atualizar_jornada(h)).pack(side="left", padx=(0 if horas==4 else 5, 5))
            
        # The entry field is connected directly to the variable
        tk.Entry(botoes_jornada, textvariable=self.var_horas_jornada, bg=BG_BOTAO_CINZA, width=4).pack(side="left", padx=5)

        tk.Label(parent, text="🧍 Onde sente desconforto?", bg=BG_CINZA_ESCURO).pack(anchor="w", pady=(15, 5))
        botoes_desconforto = tk.Frame(parent, bg=BG_CINZA_ESCURO)
        botoes_desconforto.pack(anchor="w")

        # Map discomfort types to IDs (assuming your DB has 1=Cervicalgia, 5=Dorsalgia, etc.)
        opcoes_dor = [
            ("Ombros", 1), 
            ("Costas", 5), 
            ("Mãos", 4), 
            ("Olhos", 0) # Assumed ID or handle separately
        ]
        
        for local, id_dor in opcoes_dor:
            tk.Button(botoes_desconforto, text=local, bg=BG_BOTAO_CINZA, relief="flat",
                      command=lambda id=id_dor: self._selecionar_dor(id)).pack(side="left", padx=(0 if local=="Ombros" else 5, 5))
        
        tk.Button(parent, text="Nenhum", bg=BG_BOTAO_CINZA, relief="flat",
                  command=lambda: self._selecionar_dor(0)).pack(anchor="w", pady=(5, 0))

    def _montar_lembretes_e_resumo(self, parent):
        tk.Label(parent, text="🔔 Lembrar a cada", bg=BG_CINZA_ESCURO).pack(anchor="w", pady=(0, 5))
        botoes_lembrete = tk.Frame(parent, bg=BG_CINZA_ESCURO)
        botoes_lembrete.pack(anchor="w") 

        for min_val in [25, 30, 50]:
            tk.Button(botoes_lembrete, text=f"{min_val}m", bg=BG_BOTAO_CINZA, relief="flat",
                      command=lambda m=min_val: self._atualizar_lembrete(m)).pack(side="left", padx=(0 if min_val==25 else 5, 5))
                      
        tk.Entry(botoes_lembrete, textvariable=self.var_minutos_lembrete, bg=BG_BOTAO_CINZA, width=4).pack(side="left", padx=5)

        caixa_resumo = tk.Frame(parent, bg=BG_BRANCO, padx=15, pady=15)
        caixa_resumo.pack(anchor="w", fill="x", pady=(20, 0))

        tk.Label(caixa_resumo, text="Resumo da sessão", bg=BG_BRANCO, fg="#555555", font=("Helvetica", 10)).pack(anchor="w")
        
        # Create dynamic summary labels
        self.lbl_resumo_sessao = tk.Label(caixa_resumo, text="", bg=BG_BRANCO, font=("Helvetica", 12, "bold"))
        self.lbl_resumo_sessao.pack(anchor="w", pady=(2, 5))
        
        self.lbl_resumo_dor = tk.Label(caixa_resumo, text="", bg=BG_BRANCO, fg=COR_TEXTO, font=("Helvetica", 10))
        self.lbl_resumo_dor.pack(anchor="w")
        
        # Initialize summary text
        self._atualizar_textos_resumo()

    def _atualizar_jornada(self, horas):
        self.var_horas_jornada.set(horas)
        self._atualizar_textos_resumo()

    def _atualizar_lembrete(self, minutos):
        self.var_minutos_lembrete.set(minutos)
        self._atualizar_textos_resumo()
        
    def _selecionar_dor(self, id_dor):
        self.var_id_dor.set(id_dor)
        self._atualizar_textos_resumo()

    def _atualizar_textos_resumo(self):
        """Updates the labels when user changes settings"""
        h = self.var_horas_jornada.get()
        m = self.var_minutos_lembrete.get()
        id_dor = self.var_id_dor.get()
        
        # Update summary labels
        self.lbl_resumo_sessao.config(text=f"{h}h de jornada · pausa a cada {m} min")
        
        # Map ID back to name for display
        nomes_dor = {0: "Nenhum", 1: "Ombros/Pescoço", 4: "Mãos/Punhos", 5: "Costas"}
        nome_dor = nomes_dor.get(id_dor, "Desconhecido")
        self.lbl_resumo_dor.config(text=f"Foco inicial: {nome_dor}")
        
        # Update header info
        self.var_tempo_info.set(f"⏱ {h}h   🔔 {m}m")

    def alternar_detalhes(self):
        if self.detalhes.winfo_ismapped():
            self.detalhes.pack_forget() 
        else:
            self.detalhes.pack(fill="x") 

    def acao_iniciar_tarefa(self):
        # Fetch the LIVE values from the variables
        horas_trabalho = self.var_horas_jornada.get()
        minutos_pausa = self.var_minutos_lembrete.get()
        id_dor_selecionada = self.var_id_dor.get()
        
        sucesso, msg, id_jornada = self.app.config_controller.salvar_preferencias_e_iniciar_jornada(horas_trabalho, minutos_pausa)

        if sucesso:
            self.app.sessao_controller.configurar_sessao(horas_trabalho, minutos_pausa, id_dor_selecionada)
            self.app.show_page("timer")
            self.app.sessao_controller.iniciar_temporizador()
            print("Jornada iniciada com sucesso!")
        else:
            print(f"Erro ao iniciar: {msg}")


# ==========================================
# PÁGINA PRINCIPAL (HOME)
# ==========================================
class HomePage(tk.Frame):
    def __init__(self, parent, app): 
        super().__init__(parent, bg=BG_CINZA_ESCURO)
        self.app = app
        self.f_titulo = tkfont.Font(family="Helvetica", size=24, weight="bold")
        self._build()

    def _build(self):
        tk.Label(
            self,
            text="Página inicial - Saúde e Produtividade",
            bg=BG_CINZA_ESCURO,
            fg=COR_TITULO,
            font=self.f_titulo,
        ).pack(anchor="w", pady=(20, 20))

        self.contorno = tk.Frame(self, bg=BG_BRANCO, width=1400, height=700)
        self.contorno.pack(anchor="c", expand=True, fill="both") 
        self.contorno.pack_propagate(False) 

        # 1. A barra de Input fica FIXA no topo
        self._build_area_input()
        
        # 2. Constrói a engrenagem do Scroll
        self._build_area_scroll()
        
        # 3. Adiciona as tarefas iniciais
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