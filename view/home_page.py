import tkinter as tk
from tkinter import font as tkfont


BG_BRANCO       = "#FFFFFF"
BG_CINZA_CLARO  = "#F3F7F4"
BG_CINZA_ESCURO = "#EEF4EF"
BG_BOTAO_VERDE  = "#A7F3D0"
BG_BOTAO_CINZA  = "#DDE8DF"
COR_TEXTO       = "#000000"
COR_TITULO      = "#000000"


def botao_redondo(parent, text, command, bg, fg, width=90, height=36, radius=18):
    canvas = tk.Canvas(parent, width=width, height=height, bg=parent["bg"], highlightthickness=0)

    canvas.create_oval(0, 0, radius*2, radius*2, fill=bg, outline=bg)
    canvas.create_oval(width-radius*2, 0, width, radius*2, fill=bg, outline=bg)
    canvas.create_oval(0, height-radius*2, radius*2, height, fill=bg, outline=bg)
    canvas.create_oval(width-radius*2, height-radius*2, width, height, fill=bg, outline=bg)
    canvas.create_rectangle(radius, 0, width-radius, height, fill=bg, outline=bg)
    canvas.create_rectangle(0, radius, width, height-radius, fill=bg, outline=bg)

    canvas.create_text(width//2, height//2, text=text, fill=fg, font=("Helvetica", 12, "bold"))

    canvas.bind("<Button-1>", lambda e: command())
    return canvas


def badge_tempo(parent, text, bg_cor="#E8F5EE", fg_cor="#2e7d52"):
    """Mini label estilo pill/badge para exibir tempo."""
    f = tk.Frame(parent, bg=bg_cor, padx=10, pady=3)
    tk.Label(f, text=text, font=("Helvetica", 11, "bold"), bg=bg_cor, fg=fg_cor).pack()
    return f


class CartaoTarefa(tk.Frame):
    def __init__(self, parent, nome_tarefa, horas, minutos, dor, app, jornada_id=None):
        super().__init__(parent, bg=BG_CINZA_CLARO, highlightthickness=1,
                         highlightbackground="#D9E4DA")
        self.app = app
        self.nome_tarefa = nome_tarefa
        self.jornada_id  = jornada_id

        self.var_horas_jornada    = tk.IntVar(value=horas)
        self.var_minutos_lembrete = tk.IntVar(value=minutos)
        self.var_id_dor           = tk.IntVar(value=dor if dor else 0)
        self.var_input_horas      = tk.StringVar(value=str(horas))
        self.var_input_minutos    = tk.StringVar(value=str(minutos))
        self.var_horas_badge      = tk.StringVar(value=f"⏱ {horas}h")
        self.var_minutos_badge    = tk.StringVar(value=f"🔔 {minutos}m")

        self.pack(fill="x", padx=60, pady=12)
        self._build_cabecalho()
        self._build_separador()
        self._build_detalhes()

    def _build_cabecalho(self):
        self.cabecalho = tk.Frame(self, bg=BG_CINZA_CLARO, padx=22, pady=14)
        self.cabecalho.pack(fill="x")

        # Nome como label clicável (não mais um botão feio)
        self.lbl_nome = tk.Label(
            self.cabecalho, text=self.nome_tarefa,
            font=("Helvetica", 18, "bold"),
            bg=BG_CINZA_CLARO, fg=COR_TITULO,
            cursor="hand2"
        )
        self.lbl_nome.pack(side="left")
        self.lbl_nome.bind("<Button-1>", lambda e: self.alternar_detalhes())

        # Badges de tempo (pill verde suave)
        self.badge_h = badge_tempo(self.cabecalho, text=f"⏱ {self.var_horas_jornada.get()}h")
        self.badge_h.pack(side="left", padx=(18, 0))

        self.badge_m = badge_tempo(self.cabecalho, text=f"🔔 {self.var_minutos_lembrete.get()}m")
        self.badge_m.pack(side="left", padx=(6, 0))

        botao_excluir = botao_redondo(
            self.cabecalho, "Excluir", self.acao_excluir_tarefa, "#F5DADA", "#8B2020"
        )
        botao_excluir.pack(side="right", padx=(10, 0))

        botao_iniciar = botao_redondo(
            self.cabecalho, "Iniciar", self.acao_iniciar_tarefa, BG_BOTAO_VERDE, "#1a5c38"
        )
        botao_iniciar.pack(side="right")

    def _build_separador(self):
        """Linha fina de separação entre cabeçalho e detalhes."""
        self.separador = tk.Frame(self, bg="#D9E4DA", height=1)
        # Só aparece quando detalhes estiver visível — gerenciado em alternar_detalhes

    def _build_detalhes(self):
        self.detalhes = tk.Frame(self, bg=BG_CINZA_ESCURO, padx=25, pady=25)
        col_esq = tk.Frame(self.detalhes, bg=BG_CINZA_ESCURO)
        col_esq.pack(side="left", anchor="nw")
        col_dir = tk.Frame(self.detalhes, bg=BG_CINZA_ESCURO)
        col_dir.pack(side="right", anchor="ne")
        self._montar_jornada_e_desconforto(col_esq)
        self._montar_lembretes_e_resumo(col_dir)

    def _montar_jornada_e_desconforto(self, parent):
        fonte_titulos = ("Helvetica", 13, "bold")

        tk.Label(parent, text="🕒 Jornada de trabalho", font=fonte_titulos, fg="#444444",
                 bg=BG_CINZA_ESCURO).pack(anchor="w", pady=(0, 8))

        frame_h = tk.Frame(parent, bg=BG_CINZA_ESCURO)
        frame_h.pack(anchor="w")
        for h in [4, 6, 8]:
            self._botao_opcao(frame_h, f"{h}h", lambda h=h: self._atualizar_jornada(h)).pack(
                side="left", padx=(0, 6))

        campo_h = tk.Entry(frame_h, textvariable=self.var_input_horas, font=("Helvetica", 13),
                           bg=BG_BRANCO, width=5, justify="center",
                           relief="flat", highlightthickness=1, highlightbackground="#C5D9C7")
        campo_h.pack(side="left", padx=(4, 0), ipady=5)
        campo_h.bind("<Return>", self._validar_horas_enter)

        tk.Label(parent, text="🧍 Onde sente desconforto?", font=fonte_titulos, fg="#444444",
                 bg=BG_CINZA_ESCURO).pack(anchor="w", pady=(22, 8))

        frame_d = tk.Frame(parent, bg=BG_CINZA_ESCURO)
        frame_d.pack(anchor="w")
        for local, id_dor in [("Pescoço", 1), ("Lombar", 2), ("Punho", 3), ("Mão", 4), ("Costas", 5)]:
            self._botao_opcao(frame_d, local, lambda id=id_dor: self._selecionar_dor(id)).pack(
                side="left", padx=(0, 6))

        self._botao_opcao(parent, "Nenhum", lambda: self._selecionar_dor(0)).pack(
            anchor="w", pady=(10, 0))

    def _montar_lembretes_e_resumo(self, parent):
        fonte_titulos = ("Helvetica", 13, "bold")

        tk.Label(parent, text="🔔 Lembrar a cada", font=fonte_titulos, fg="#444444",
                 bg=BG_CINZA_ESCURO).pack(anchor="w", pady=(0, 8))

        frame_m = tk.Frame(parent, bg=BG_CINZA_ESCURO)
        frame_m.pack(anchor="w")
        for m in [25, 30, 50]:
            self._botao_opcao(frame_m, f"{m}m", lambda m=m: self._atualizar_lembrete(m)).pack(
                side="left", padx=(0, 6))

        campo_m = tk.Entry(frame_m, textvariable=self.var_input_minutos, font=("Helvetica", 13),
                           bg=BG_BRANCO, width=5, justify="center",
                           relief="flat", highlightthickness=1, highlightbackground="#C5D9C7")
        campo_m.pack(side="left", padx=(4, 0), ipady=5)
        campo_m.bind("<Return>", self._validar_minutos_enter)

        # Caixa de resumo com visual mais limpo
        caixa = tk.Frame(parent, bg=BG_BRANCO, padx=18, pady=16,
                         highlightthickness=1, highlightbackground="#D9E4DA")
        caixa.pack(anchor="w", fill="x", pady=(28, 0))

        tk.Label(caixa, text="RESUMO DA SESSÃO", bg=BG_BRANCO,
                 fg="#888888", font=("Helvetica", 9, "bold")).pack(anchor="w")

        self.lbl_resumo_sessao = tk.Label(caixa, text="", bg=BG_BRANCO, fg=COR_TITULO,
                                          font=("Helvetica", 15, "bold"))
        self.lbl_resumo_sessao.pack(anchor="w", pady=(4, 2))

        self.lbl_resumo_dor = tk.Label(caixa, text="", bg=BG_BRANCO,
                                       fg="#555555", font=("Helvetica", 12))
        self.lbl_resumo_dor.pack(anchor="w")
        self._atualizar_textos_resumo()

    def _botao_opcao(self, parent, text, command):
        """Botão de seleção flat com borda fina — sem Canvas, sem relief horrível."""
        btn = tk.Button(
            parent, text=text, command=command,
            font=("Helvetica", 12), bg=BG_BOTAO_CINZA, fg="#333333",
            relief="flat", cursor="hand2", padx=12, pady=5,
            highlightthickness=1, highlightbackground="#C5D9C7",
            activebackground="#C8E6CF", activeforeground="#1a1a1a"
        )
        return btn

    def _validar_horas_enter(self, event):
        try:
            v = int(self.var_input_horas.get())
            if v < 0:
                raise ValueError
            self._atualizar_jornada(v)
            self.focus()
        except ValueError:
            self.var_input_horas.set(str(self.var_horas_jornada.get()))

    def _validar_minutos_enter(self, event):
        try:
            v = int(self.var_input_minutos.get())
            if v < 0:
                raise ValueError
            self._atualizar_lembrete(v)
            self.focus()
        except ValueError:
            self.var_input_minutos.set(str(self.var_minutos_lembrete.get()))

    def _salvar_alteracoes(self):
        if self.jornada_id:
            self.app.config_controller.atualizar_tarefa_existente(
                self.jornada_id,
                self.var_horas_jornada.get(),
                self.var_minutos_lembrete.get(),
                self.var_id_dor.get()
            )

    def _atualizar_jornada(self, horas):
        self.var_horas_jornada.set(horas)
        self.var_input_horas.set(str(horas))
        self._atualizar_textos_resumo()
        self._salvar_alteracoes()

    def _atualizar_lembrete(self, minutos):
        self.var_minutos_lembrete.set(minutos)
        self.var_input_minutos.set(str(minutos))
        self._atualizar_textos_resumo()
        self._salvar_alteracoes()

    def _selecionar_dor(self, id_dor):
        self.var_id_dor.set(id_dor)
        self._atualizar_textos_resumo()
        self._salvar_alteracoes()

    def _atualizar_textos_resumo(self):
        h = self.var_horas_jornada.get()
        m = self.var_minutos_lembrete.get()
        nomes = {0: "Nenhum", 1: "Pescoço", 2: "Lombar", 3: "Punho", 4: "Mão", 5: "Costas"}
        self.lbl_resumo_sessao.config(text=f"{h}h de jornada · pausa a cada {m} min")
        self.lbl_resumo_dor.config(text=f"Foco inicial: {nomes.get(self.var_id_dor.get(), 'Desconhecido')}")
        # Atualiza os badges no cabeçalho
        if hasattr(self, 'badge_h'):
            for w in self.badge_h.winfo_children():
                w.config(text=f"⏱ {h}h")
        if hasattr(self, 'badge_m'):
            for w in self.badge_m.winfo_children():
                w.config(text=f"🔔 {m}m")

    def alternar_detalhes(self):
        if self.detalhes.winfo_ismapped():
            self.separador.pack_forget()
            self.detalhes.pack_forget()
        else:
            self.separador.pack(fill="x")
            self.detalhes.pack(fill="x")

    def acao_iniciar_tarefa(self):
        self._salvar_alteracoes()
        self.app.sessao_controller.configurar_sessao(
            self.var_horas_jornada.get(),
            self.var_minutos_lembrete.get(),
            self.var_id_dor.get()
        )
        self.app.show_page("timer")
        self.app.sessao_controller.iniciar_temporizador()

    def acao_excluir_tarefa(self):
        if self.jornada_id and self.app:
            self.app.config_controller.excluir_tarefa(self.jornada_id)

        if self.app and self.app.sessao_controller:
            self.app.sessao_controller.pausar_temporizador()
            self.app.sessao_controller.tempo_restante_segundos = 0
            self.app.sessao_controller.tempo_trabalho_total_restante = 0
            self.app.sessao_controller.atualizar_interface_relogio()

        self.destroy()

    def aplicar_tema(self, escuro: bool):
        cor_card    = "#FFFFFF" if escuro else BG_CINZA_CLARO
        cor_detalhe = "#F8FAF7" if escuro else BG_CINZA_ESCURO
        cor_caixa   = "#AEB9B0" if escuro else BG_BRANCO
        cor_texto   = "#000000"
        cor_botao   = "#D2DDD4" if escuro else BG_BOTAO_CINZA
        cor_iniciar = "#B8E6C6" if escuro else BG_BOTAO_VERDE
        cor_excluir = "#F5DADA"
        badge_bg    = "#C8E0D0" if escuro else "#E8F5EE"
        badge_fg    = "#1a4a2e" if escuro else "#2e7d52"

        def aplicar(widget, bg_atual=cor_card):
            if isinstance(widget, tk.Frame):
                bg = cor_detalhe if widget is getattr(self, "detalhes", None) else bg_atual
                widget.configure(bg=bg)
                for filho in widget.winfo_children():
                    aplicar(filho, bg)
            elif isinstance(widget, tk.Label):
                widget.configure(bg=bg_atual, fg=cor_texto)
            elif isinstance(widget, tk.Entry):
                widget.configure(bg=cor_caixa, fg=cor_texto,
                                 insertbackground=cor_texto,
                                 highlightbackground="#7F8C82" if escuro else "#C5D9C7")
            elif isinstance(widget, tk.Button):
                texto = widget.cget("text")
                if texto == "Iniciar":
                    widget.configure(bg=cor_iniciar, fg="#1a5c38" if not escuro else "#000",
                                     activebackground=cor_iniciar)
                elif texto == "Excluir":
                    widget.configure(bg=cor_excluir, fg="#8B2020",
                                     activebackground=cor_excluir)
                else:
                    widget.configure(bg=cor_botao, fg=cor_texto,
                                     activebackground=cor_botao, activeforeground=cor_texto)

        self.configure(bg=cor_card, highlightbackground="#7F8C82" if escuro else "#D9E4DA")
        aplicar(self, cor_card)

        # Atualiza badges separadamente (são Frames filhos com Label dentro)
        if hasattr(self, 'badge_h') and self.badge_h.winfo_exists():
            self.badge_h.configure(bg=badge_bg)
            for w in self.badge_h.winfo_children():
                w.configure(bg=badge_bg, fg=badge_fg)
        if hasattr(self, 'badge_m') and self.badge_m.winfo_exists():
            self.badge_m.configure(bg=badge_bg)
            for w in self.badge_m.winfo_children():
                w.configure(bg=badge_bg, fg=badge_fg)


class HomePage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg=BG_CINZA_ESCURO)
        self.app = app
        self.f_titulo = tkfont.Font(family="Helvetica", size=32, weight="bold")
        self.f_subtitulo = tkfont.Font(family="Helvetica", size=13)
        self.var_input_tarefa = tk.StringVar()
        self._build()
        if hasattr(self.app, 'config_tema_escuro'):
            self.aplicar_tema(self.app.config_tema_escuro)

    def _build(self):
        self.cabecalho_pagina = tk.Frame(self, bg=BG_CINZA_ESCURO)
        self.cabecalho_pagina.pack(anchor="w", fill="x", pady=(30, 20), padx=40)

        self.lbl_titulo = tk.Label(
            self.cabecalho_pagina, text="Tarefas e pausas",
            bg=BG_CINZA_ESCURO, fg=COR_TITULO, font=self.f_titulo
        )
        self.lbl_titulo.pack(anchor="w")

        self.lbl_subtitulo = tk.Label(
            self.cabecalho_pagina,
            text="Crie jornadas, defina lembretes e escolha o foco do alongamento.",
            bg=BG_CINZA_ESCURO, fg="#555555", font=self.f_subtitulo
        )
        self.lbl_subtitulo.pack(anchor="w", pady=(4, 0))

        self.contorno = tk.Frame(self, bg=BG_BRANCO, highlightthickness=1,
                                 highlightbackground="#D9E4DA")
        self.contorno.pack(anchor="c", expand=True, fill="both", padx=34, pady=(0, 28))

        self._build_area_input()
        self._build_area_scroll()
        self._build_lista_tarefas()

    def _build_area_input(self):
        self.frame_topo = tk.Frame(self.contorno, bg=BG_BRANCO)
        self.frame_topo.pack(pady=(28, 18), fill="x", padx=60)

        self.lbl_nova_tarefa = tk.Label(
            self.frame_topo, text="Nova tarefa", bg=BG_BRANCO, fg="#888888",
            font=("Helvetica", 10, "bold")
        )
        self.lbl_nova_tarefa.pack(anchor="w", pady=(0, 8))

        self.linha_input = tk.Frame(self.frame_topo, bg=BG_BRANCO)
        self.linha_input.pack(fill="x")

        self.campo_tarefa = tk.Entry(
            self.linha_input, textvariable=self.var_input_tarefa,
            font=("Helvetica", 15), relief="flat",
            highlightthickness=1, highlightbackground="#D9E4DA"
        )
        self.campo_tarefa.pack(side="left", ipady=12, padx=(0, 16), fill="x", expand=True)
        self.campo_tarefa.bind("<Return>", lambda e: self._adicionar_nova_tarefa())

        # Botão adicionar arredondado (mesmo padrão dos outros)
        self.btn_adicionar = botao_redondo(
            self.linha_input, "+ Adicionar", self._adicionar_nova_tarefa,
            bg=BG_BOTAO_VERDE, fg="#1a5c38", width=130, height=42, radius=21
        )
        self.btn_adicionar.pack(side="right")

    def _build_label_secao(self):
        frame = tk.Frame(self.area_tarefas, bg=BG_BRANCO)
        frame.pack(fill="x", padx=60, pady=(8, 0))
        self.lbl_secao = tk.Label(
            frame, text="SUAS TAREFAS", bg=BG_BRANCO,
            fg="#AAAAAA", font=("Helvetica", 9, "bold")
        )
        self.lbl_secao.pack(anchor="w")

    def _build_area_scroll(self):
        container = tk.Frame(self.contorno, bg=BG_BRANCO)
        container.pack(fill="both", expand=True, pady=(0, 20))
        self.canvas = tk.Canvas(container, bg=BG_BRANCO, highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)
        sb = tk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
        sb.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=sb.set)
        self.area_tarefas = tk.Frame(self.canvas, bg=BG_BRANCO)
        self.janela_canvas = self.canvas.create_window(
            (0, 0), window=self.area_tarefas, anchor="nw"
        )
        self.area_tarefas.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.itemconfig(self.janela_canvas, width=e.width)
        )
        self.canvas.bind_all("<MouseWheel>", self._ao_rolar_mouse)

    def _ao_rolar_mouse(self, event):
        if self.area_tarefas.winfo_reqheight() > self.canvas.winfo_height():
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _build_lista_tarefas(self):
        tarefas = self.app.config_controller.buscar_tarefas_do_usuario()
        if tarefas:
            self._build_label_secao()
            for t in tarefas:
                tarefa = CartaoTarefa(
                    self.area_tarefas,
                    nome_tarefa=t['nome'], horas=t['horas'],
                    minutos=t['minutos'], dor=t['desconforto'],
                    app=self.app, jornada_id=t['id']
                )
                if hasattr(self.app, 'config_tema_escuro'):
                    tarefa.aplicar_tema(self.app.config_tema_escuro)
        else:
            self.lbl_vazio = tk.Label(
                self.area_tarefas, text="Nenhuma tarefa criada ainda.",
                bg=BG_BRANCO, fg="#AAAAAA", font=("Helvetica", 14)
            )
            self.lbl_vazio.pack(pady=60)

    def _adicionar_nova_tarefa(self):
        texto = self.var_input_tarefa.get()
        if texto.strip():
            sucesso, msg, id_nova = self.app.config_controller.salvar_nova_tarefa(
                nome_tarefa=texto, horas=6, minutos=30, id_dor=0
            )
            if sucesso:
                if hasattr(self, 'lbl_vazio') and self.lbl_vazio.winfo_exists():
                    self.lbl_vazio.destroy()
                    self._build_label_secao()
                tarefa = CartaoTarefa(
                    self.area_tarefas,
                    nome_tarefa=texto, horas=6, minutos=30, dor=0,
                    app=self.app, jornada_id=id_nova
                )
                if hasattr(self.app, 'config_tema_escuro'):
                    tarefa.aplicar_tema(self.app.config_tema_escuro)
                self.var_input_tarefa.set("")
                self.app.after(50, lambda: self.canvas.yview_moveto(1.0))

    def aplicar_tema(self, escuro: bool):
        cor_fundo    = "#AEB9B0" if escuro else BG_CINZA_ESCURO
        cor_cartao   = "#F8FAF7" if escuro else BG_BRANCO
        cor_texto    = "#000000"
        cor_campo    = "#FFFFFF" if escuro else "white"
        cor_borda    = "#7F8C82" if escuro else "#D9E4DA"
        cor_botao_bg = "#B8E6C6" if escuro else BG_BOTAO_VERDE

        self.configure(bg=cor_fundo)
        self.cabecalho_pagina.configure(bg=cor_fundo)
        self.lbl_titulo.configure(bg=cor_fundo, fg=cor_texto)
        self.lbl_subtitulo.configure(bg=cor_fundo, fg="#555555" if not escuro else "#CCCCCC")
        self.contorno.configure(bg=cor_cartao, highlightbackground=cor_borda)
        self.frame_topo.configure(bg=cor_cartao)
        self.linha_input.configure(bg=cor_cartao)
        self.lbl_nova_tarefa.configure(bg=cor_cartao, fg="#888888")
        self.campo_tarefa.configure(
            bg=cor_campo, fg=cor_texto,
            insertbackground=cor_texto,
            highlightbackground=cor_borda
        )
        # Recria botão adicionar com nova cor de fundo (Canvas não tem configure fácil)
        self.btn_adicionar.configure(bg=cor_cartao)

        self.canvas.configure(bg=cor_cartao)
        self.area_tarefas.configure(bg=cor_cartao)
        if hasattr(self, 'lbl_vazio') and self.lbl_vazio.winfo_exists():
            self.lbl_vazio.configure(bg=cor_cartao, fg="#AAAAAA")
        if hasattr(self, 'lbl_secao') and self.lbl_secao.winfo_exists():
            self.lbl_secao.configure(bg=cor_cartao)
        for tarefa in self.area_tarefas.winfo_children():
            if hasattr(tarefa, 'aplicar_tema'):
                tarefa.aplicar_tema(escuro)