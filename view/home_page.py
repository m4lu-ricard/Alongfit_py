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
class CartaoTarefa(tk.Frame):
    def __init__(self, parent, nome_tarefa, horas, minutos, dor, app, jornada_id=None): 
        super().__init__(parent, bg=BG_CINZA_CLARO)
        self.app = app 
        self.nome_tarefa = nome_tarefa
        self.jornada_id = jornada_id
        
        # 1. Variáveis que guardam o valor REAL aprovado pelo sistema
        self.var_horas_jornada = tk.IntVar(value=horas)
        self.var_minutos_lembrete = tk.IntVar(value=minutos)
        self.var_id_dor = tk.IntVar(value=dor if dor else 0) 
        
        # 2. Variáveis de TEXTO apenas para os campos de digitação
        self.var_input_horas = tk.StringVar(value=str(horas))
        self.var_input_minutos = tk.StringVar(value=str(minutos))
        
        self.var_tempo_info = tk.StringVar(value=f"⏱ {horas}h   🔔 {minutos}m")
        
        self.pack(fill="x", padx=40, pady=10)
        self._build_cabecalho()
        self._build_detalhes()

    def _build_cabecalho(self):
        cabecalho = tk.Frame(self, bg=BG_CINZA_CLARO, padx=15, pady=10)
        cabecalho.pack(fill="x")

        tk.Button(cabecalho, text=self.nome_tarefa, font=("Helvetica", 14, "bold"), bg=BG_CINZA_CLARO, relief="flat", cursor="hand2", command=self.alternar_detalhes).pack(side="left")
        tk.Label(cabecalho, textvariable=self.var_tempo_info, bg=BG_CINZA_CLARO, fg="#555555").pack(side="left", padx=20)
        tk.Button(cabecalho, text="excluir", bg="#bcbcbc", relief="flat", command=self.acao_excluir_tarefa).pack(side="right", padx=(10, 0))
        tk.Button(cabecalho, text="Iniciar", bg=BG_BOTAO_CINZA, relief="flat", command=self.acao_iniciar_tarefa).pack(side="right")

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

        for h in [4, 6, 8]:
            tk.Button(botoes_jornada, text=f"{h}h", bg=BG_BOTAO_CINZA, relief="flat", command=lambda h=h: self._atualizar_jornada(h)).pack(side="left", padx=(0 if h==4 else 5, 5))
        
        # Campo de Horas Customizado
        campo_horas = tk.Entry(botoes_jornada, textvariable=self.var_input_horas, bg=BG_BOTAO_CINZA, width=4)
        campo_horas.pack(side="left", padx=5)
        campo_horas.bind("<Return>", self._validar_horas_enter) # <- Ouve a tecla Enter

        tk.Label(parent, text="🧍 Onde sente desconforto?", bg=BG_CINZA_ESCURO).pack(anchor="w", pady=(15, 5))
        botoes_desconforto = tk.Frame(parent, bg=BG_CINZA_ESCURO)
        botoes_desconforto.pack(anchor="w")

        # IDs baseados exatamente no seu INSERT no banco de dados!
        opcoes_dor = [
            ("Pescoço", 1), 
            ("Lombar", 2), 
            ("Punho", 3), 
            ("Mão", 4), 
            ("Costas", 5)
        ]
        
        for local, id_dor in opcoes_dor:
            # O 'if local=="Pescoço"' garante que o primeiro botão não tem margem extra à esquerda
            tk.Button(botoes_desconforto, text=local, bg=BG_BOTAO_CINZA, relief="flat", 
                      command=lambda id=id_dor: self._selecionar_dor(id)).pack(side="left", padx=(0 if local=="Pescoço" else 5, 5))
        
        tk.Button(parent, text="Nenhum", bg=BG_BOTAO_CINZA, relief="flat", 
                  command=lambda: self._selecionar_dor(0)).pack(anchor="w", pady=(5, 0))

    def _montar_lembretes_e_resumo(self, parent):
        tk.Label(parent, text="🔔 Lembrar a cada", bg=BG_CINZA_ESCURO).pack(anchor="w", pady=(0, 5))
        botoes_lembrete = tk.Frame(parent, bg=BG_CINZA_ESCURO)
        botoes_lembrete.pack(anchor="w") 

        for min_val in [25, 30, 50]:
            tk.Button(botoes_lembrete, text=f"{min_val}m", bg=BG_BOTAO_CINZA, relief="flat", command=lambda m=min_val: self._atualizar_lembrete(m)).pack(side="left", padx=(0 if min_val==25 else 5, 5))
        
        # Campo de Minutos Customizado
        campo_minutos = tk.Entry(botoes_lembrete, textvariable=self.var_input_minutos, bg=BG_BOTAO_CINZA, width=4)
        campo_minutos.pack(side="left", padx=5)
        campo_minutos.bind("<Return>", self._validar_minutos_enter) # <- Ouve a tecla Enter

        caixa_resumo = tk.Frame(parent, bg=BG_BRANCO, padx=15, pady=15)
        caixa_resumo.pack(anchor="w", fill="x", pady=(20, 0))

        tk.Label(caixa_resumo, text="Resumo da sessão", bg=BG_BRANCO, fg="#555555", font=("Helvetica", 10)).pack(anchor="w")
        self.lbl_resumo_sessao = tk.Label(caixa_resumo, text="", bg=BG_BRANCO, font=("Helvetica", 12, "bold"))
        self.lbl_resumo_sessao.pack(anchor="w", pady=(2, 5))
        self.lbl_resumo_dor = tk.Label(caixa_resumo, text="", bg=BG_BRANCO, fg=COR_TEXTO, font=("Helvetica", 10))
        self.lbl_resumo_dor.pack(anchor="w")
        self._atualizar_textos_resumo()

    # ==========================================
    # VALIDAÇÕES AO CLICAR NO ENTER
    # ==========================================
    def _validar_horas_enter(self, event):
        try:
            novo_valor = int(self.var_input_horas.get())
            if novo_valor < 0:
                raise ValueError
            self._atualizar_jornada(novo_valor)
            self.focus() # Tira o cursor de dentro da caixinha
        except ValueError:
            # Se for letra ou negativo, volta pro número anterior que estava salvo
            self.var_input_horas.set(str(self.var_horas_jornada.get()))

    def _validar_minutos_enter(self, event):
        try:
            novo_valor = int(self.var_input_minutos.get())
            if novo_valor < 0:
                raise ValueError
            self._atualizar_lembrete(novo_valor)
            self.focus()
        except ValueError:
            self.var_input_minutos.set(str(self.var_minutos_lembrete.get()))

    # ==========================================
    # FUNÇÕES DE ATUALIZAÇÃO E SALVAMENTO
    # ==========================================
    def _salvar_alteracoes(self):
        if self.jornada_id: 
            horas = self.var_horas_jornada.get()
            minutos = self.var_minutos_lembrete.get()
            dor = self.var_id_dor.get()
            self.app.config_controller.atualizar_tarefa_existente(self.jornada_id, horas, minutos, dor)

    def _atualizar_jornada(self, horas):
        self.var_horas_jornada.set(horas)
        self.var_input_horas.set(str(horas)) # Atualiza a caixinha caso clique nos botões (4h, 6h)
        self._atualizar_textos_resumo()
        self._salvar_alteracoes() 

    def _atualizar_lembrete(self, minutos):
        self.var_minutos_lembrete.set(minutos)
        self.var_input_minutos.set(str(minutos)) # Atualiza a caixinha caso clique nos botões (25m, 30m)
        self._atualizar_textos_resumo()
        self._salvar_alteracoes() 
        
    def _selecionar_dor(self, id_dor):
        self.var_id_dor.set(id_dor)
        self._atualizar_textos_resumo()
        self._salvar_alteracoes() 

    def _atualizar_textos_resumo(self):
        h = self.var_horas_jornada.get()
        m = self.var_minutos_lembrete.get()
        id_dor = self.var_id_dor.get()
        
        self.lbl_resumo_sessao.config(text=f"{h}h de jornada · pausa a cada {m} min")
        
        # Dicionário atualizado com os novos IDs e nomes
        nomes_dor = {
            0: "Nenhum", 
            1: "Pescoço", 
            2: "Lombar", 
            3: "Punho", 
            4: "Mão", 
            5: "Costas"
        }
        nome_dor = nomes_dor.get(id_dor, "Desconhecido")
        self.lbl_resumo_dor.config(text=f"Foco inicial: {nome_dor}")
        
        self.var_tempo_info.set(f"⏱ {h}h   🔔 {m}m")

    def alternar_detalhes(self):
        if self.detalhes.winfo_ismapped():
            self.detalhes.pack_forget() 
        else:
            self.detalhes.pack(fill="x") 

    def acao_iniciar_tarefa(self):
        self._salvar_alteracoes()
        horas_trabalho = self.var_horas_jornada.get()
        minutos_pausa = self.var_minutos_lembrete.get()
        id_dor_selecionada = self.var_id_dor.get()
        self.app.sessao_controller.configurar_sessao(horas_trabalho, minutos_pausa, id_dor_selecionada)
        self.app.show_page("timer")
        self.app.sessao_controller.iniciar_temporizador()
    
    def acao_excluir_tarefa(self):
        if self.jornada_id:
            self.app.config_controller.excluir_tarefa(self.jornada_id)
        self.destroy()

# ==========================================
# PÁGINA PRINCIPAL (HOME)
# ==========================================
class HomePage(tk.Frame):
    def __init__(self, parent, app): 
        super().__init__(parent, bg=BG_CINZA_ESCURO)
        self.app = app
        self.f_titulo = tkfont.Font(family="Helvetica", size=24, weight="bold")
        self.var_input_tarefa = tk.StringVar()
        self._build()

    def _build(self):
        tk.Label(self, text="Página inicial - Saúde e Produtividade", bg=BG_CINZA_ESCURO, fg=COR_TITULO, font=self.f_titulo).pack(anchor="w", pady=(20, 20))
        self.contorno = tk.Frame(self, bg=BG_BRANCO, width=1400, height=700)
        self.contorno.pack(anchor="c", expand=True, fill="both") 
        self.contorno.pack_propagate(False) 

        self._build_area_input()
        self._build_area_scroll()
        self._build_lista_tarefas()

    def _build_area_input(self):
        frame_topo = tk.Frame(self.contorno, bg=BG_BRANCO)
        frame_topo.pack(pady=20, fill="x", padx=40)
        
        campo_tarefa = tk.Entry(frame_topo, textvariable=self.var_input_tarefa, font=("Helvetica", 14))
        campo_tarefa.pack(side="left", ipady=8, padx=(0, 20), fill="x", expand=True)
        tk.Button(frame_topo, text="+ Adicionar", bg=BG_BOTAO_VERDE, font=("Helvetica", 12, "bold"), relief="flat", padx=20, pady=5, command=self._adicionar_nova_tarefa).pack(side="right")

    def _build_area_scroll(self):
        container_scroll = tk.Frame(self.contorno, bg=BG_BRANCO)
        container_scroll.pack(fill="both", expand=True, pady=(0, 20))
        self.canvas = tk.Canvas(container_scroll, bg=BG_BRANCO, highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar = tk.Scrollbar(container_scroll, orient="vertical", command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.area_tarefas = tk.Frame(self.canvas, bg=BG_BRANCO)
        self.janela_canvas = self.canvas.create_window((0, 0), window=self.area_tarefas, anchor="nw")
        self.area_tarefas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(self.janela_canvas, width=e.width))
        self.canvas.bind_all("<MouseWheel>", self._ao_rolar_mouse)

    def _ao_rolar_mouse(self, event):
        altura_das_tarefas = self.area_tarefas.winfo_reqheight()
        altura_da_tela = self.canvas.winfo_height()
        if altura_das_tarefas > altura_da_tela:
            direcao = int(-1 * (event.delta / 120))
            self.canvas.yview_scroll(direcao, "units")

    def _build_lista_tarefas(self):
        tarefas_salvas = self.app.config_controller.buscar_tarefas_do_usuario()
        if tarefas_salvas:
            for t in tarefas_salvas:
                CartaoTarefa(self.area_tarefas, nome_tarefa=t['nome'], horas=t['horas'], minutos=t['minutos'], dor=t['desconforto'], app=self.app, jornada_id=t['id'])

    def _adicionar_nova_tarefa(self):
        texto = self.var_input_tarefa.get()
        if texto.strip():
            sucesso, msg, id_nova = self.app.config_controller.salvar_nova_tarefa(nome_tarefa=texto, horas=6, minutos=30, id_dor=0)
            if sucesso:
                CartaoTarefa(self.area_tarefas, nome_tarefa=texto, horas=6, minutos=30, dor=0, app=self.app, jornada_id=id_nova)
                self.var_input_tarefa.set("")
                self.app.after(50, lambda: self.canvas.yview_moveto(1.0))