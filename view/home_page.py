import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#D9D9D9")

        # Título da página
        tk.Label(
            self,
            text="Página inicial - Saúde e Produtividade",
            bg="#D9D9D9",
            fg="#1A1A1A",
            font=("Helvetica", 24, "bold"),
        ).pack(anchor="w", pady=(20, 20))

        # Contorno principal (Caixa branca)
        contorno = tk.Frame(
            self,
            bg="white",
            width=1400,
            height=700,
        )
        contorno.pack(anchor="w")
        contorno.pack_propagate(False) 

        # ==========================================
        # 1. ÁREA SUPERIOR (INPUT + BOTÃO)
        # ==========================================
        frame_topo = tk.Frame(contorno, bg="white")
        frame_topo.pack(pady=20, fill="x", padx=40)

        campo_tarefa = tk.Entry(frame_topo, font=("Helvetica", 14), width=40)
        campo_tarefa.pack(side="left", ipady=8, padx=(0, 20))

        btn_adicionar = tk.Button(
            frame_topo, 
            text="+ Adicionar", 
            bg="#a7f3d0", 
            font=("Helvetica", 12, "bold"),
            relief="flat", 
            padx=20, pady=5
        )
        btn_adicionar.pack(side="left")


        # ==========================================
        # 2. CARTÃO DE TAREFA
        # ==========================================
        container_tarefa = tk.Frame(contorno, bg="#f0f0f0")
        container_tarefa.pack(fill="x", padx=40, pady=10)

        # --- A) PARTE DE CIMA (CABEÇALHO) ---
        cartao_frame = tk.Frame(container_tarefa, bg="#f0f0f0", padx=15, pady=10)
        cartao_frame.pack(fill="x")

        # --- B) PARTE DE BAIXO (DETALHES) ---
        detalhes_frame = tk.Frame(container_tarefa, bg="#d9d9d9", padx=15, pady=15)

        coluna_esquerda = tk.Frame(detalhes_frame, bg="#d9d9d9")
        coluna_esquerda.pack(side="left", anchor="nw") 

        coluna_direita = tk.Frame(detalhes_frame, bg="#d9d9d9")
        coluna_direita.pack(side="right", anchor="ne") 

        # ==========================================
        # COLUNA ESQUERDA (Jornada e Desconforto)
        # ==========================================
        # 1. Jornada
        tk.Label(coluna_esquerda, text="🕒 Jornada de trabalho", bg="#d9d9d9").pack(anchor="w", pady=(0, 5))
        
        botoes_jornada = tk.Frame(coluna_esquerda, bg="#d9d9d9")
        botoes_jornada.pack(anchor="w")

        tk.Button(botoes_jornada, text="4h", bg="#c8d6ce", relief="flat").pack(side="left", padx=(0, 5))
        tk.Button(botoes_jornada, text="6h", bg="#c8d6ce", relief="flat").pack(side="left", padx=5)
        tk.Button(botoes_jornada, text="8h", bg="#c8d6ce", relief="flat").pack(side="left", padx=5)
        tk.Entry(botoes_jornada, bg="#c8d6ce", width=4).pack(side="left", padx=5)

        # 2. Desconforto (Adicionado!)
        tk.Label(coluna_esquerda, text="🧍 Onde sente desconforto?", bg="#d9d9d9").pack(anchor="w", pady=(15, 5))
        
        botoes_desconforto = tk.Frame(coluna_esquerda, bg="#d9d9d9")
        botoes_desconforto.pack(anchor="w")

        tk.Button(botoes_desconforto, text="Ombros", bg="#c8d6ce", relief="flat").pack(side="left", padx=(0, 5))
        tk.Button(botoes_desconforto, text="Costas", bg="#c8d6ce", relief="flat").pack(side="left", padx=5)
        tk.Button(botoes_desconforto, text="Mãos", bg="#c8d6ce", relief="flat").pack(side="left", padx=5)
        tk.Button(botoes_desconforto, text="Olhos", bg="#c8d6ce", relief="flat").pack(side="left", padx=5)
        
        tk.Button(coluna_esquerda, text="Nenhum", bg="#c8d6ce", relief="flat").pack(anchor="w", pady=(5, 0))


        # ==========================================
        # COLUNA DIREITA (Lembretes e Resumo)
        # ==========================================
        # 1. Lembretes
        tk.Label(coluna_direita, text="🔔 Lembrar a cada", bg="#d9d9d9").pack(anchor="w", pady=(0, 5))
        
        botoes_lembrete = tk.Frame(coluna_direita, bg="#d9d9d9")
        botoes_lembrete.pack(anchor="w") # Correção: alterado de "right" para "w"

        tk.Button(botoes_lembrete, text="25m", bg="#c8d6ce", relief="flat").pack(side="left", padx=(0, 5))
        tk.Button(botoes_lembrete, text="30m", bg="#c8d6ce", relief="flat").pack(side="left", padx=5)
        tk.Button(botoes_lembrete, text="50m", bg="#c8d6ce", relief="flat").pack(side="left", padx=5)
        tk.Entry(botoes_lembrete, bg="#c8d6ce", width=4).pack(side="left", padx=5)

        # 2. Resumo da Sessão (Caixa Branca - Adicionado!)
        caixa_resumo = tk.Frame(coluna_direita, bg="white", padx=15, pady=15)
        caixa_resumo.pack(anchor="w", fill="x", pady=(20, 0))

        tk.Label(caixa_resumo, text="Resumo da sessão", bg="white", fg="#555555", font=("Helvetica", 10)).pack(anchor="w")
        tk.Label(caixa_resumo, text="6h de jornada · pausa a cada 30 min", bg="white", font=("Helvetica", 12, "bold")).pack(anchor="w", pady=(2, 5))
        tk.Label(caixa_resumo, text="Foco inicial: Ombros", bg="white", fg="#444444", font=("Helvetica", 10)).pack(anchor="w")


        # --- FUNÇÃO DE ABRIR E FECHAR ---
        def alternar_detalhes():
            if detalhes_frame.winfo_ismapped():
                detalhes_frame.pack_forget() 
            else:
                detalhes_frame.pack(fill="x") 


        # Título da atividade (Botão para alternar)
        lbl_titulo = tk.Button(
            cartao_frame, 
            text="Fazer atividade X", 
            font=("Helvetica", 14, "bold"), 
            bg="#f0f0f0", 
            relief="flat", 
            cursor="hand2", 
            command=alternar_detalhes
        )
        lbl_titulo.pack(side="left")

        # Informações de tempo
        lbl_tempo = tk.Label(cartao_frame, text="⏱ 6h   🔔 30mx12", bg="#f0f0f0", fg="#555555")
        lbl_tempo.pack(side="left", padx=20)

        # Botões de ação alinhados à direita
        btn_excluir = tk.Button(cartao_frame, text="excluir", bg="#bcbcbc", relief="flat")
        btn_excluir.pack(side="right", padx=(10, 0))

        btn_iniciar = tk.Button(cartao_frame, text="Iniciar", bg="#c8d6ce", relief="flat")
        btn_iniciar.pack(side="right")