import tkinter as tk


class TimerPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#D9D9D9")

        
        contorno = tk.Frame(
            self,
            bg="#d9d9d9",
            width=1300,
            height=1400,
        )
        contorno.pack(anchor="c")
        contorno.pack_propagate(False)

        coluna_esquerda = tk.Frame(contorno, bg="#d9d9d9")
        coluna_esquerda.pack(side="left", anchor="nw") 

        coluna_direita = tk.Frame(contorno, bg="#d9d9d9")
        coluna_direita.pack(side="right", anchor="n") 

        tk.Label(
            coluna_esquerda,
            text="Timer de Trabalho",
            bg="#d9d9d9",
            fg="#1A1A1A",
            font=("Helvetica", 24, "bold"),
        ).pack(pady=(30, 10), anchor="w")

        timer_iniciar = tk.Frame(coluna_esquerda, bg="#FFFFFF", width=630, height=900)
        timer_iniciar.pack(anchor="w")
        timer_iniciar.pack_propagate(False)

        pausa_programda = tk.Frame(coluna_direita, bg="#FFFFFF", width=630, height=350)
        pausa_programda.pack(anchor="w", pady=(83, 5))

        progresso_semanal = tk.Frame(coluna_direita, bg="#FFFFFF", width=630, height=350)
        progresso_semanal.pack(pady=(0, 5))

        frame_botoes_fundo = tk.Frame(timer_iniciar, bg="#FFFFFF")
        frame_botoes_fundo.pack(side="bottom", fill="x", pady=20, padx=20)

        # 2. Agora colocamos os botões DENTRO desse frame invisível usando side="left" ou "right"
        tk.Button(
            frame_botoes_fundo, 
            text="Iniciar Timer", 
            bg="#a7f3d0", 
            font=("Helvetica", 12, "bold"), 
            relief="flat",
            padx=15, pady=5
        ).pack(side="right", padx=5)

        tk.Button(
            frame_botoes_fundo, 
            text="Pausar Timer", 
            bg="#fca5a5", # Um vermelho bem suave para o botão pausar
            font=("Helvetica", 12, "bold"), 
            relief="flat",
            padx=15, pady=5
        ).pack(side="left", padx=5)

        tk.Label(timer_iniciar, text="Tarefa em Andamento:", bg="#FFFFFF", fg="#444444", font=("inter", 32, "bold")).pack(pady=(10, 0))
        tk.Label(timer_iniciar, text="Trabalho", bg="#FFFFFF", fg="#444444", font=("inter", 32)).pack(pady=(0, 20))

        centro_Timer = tk.Frame(timer_iniciar, bg="#FFFFFF")
        centro_Timer.pack(pady=(0, 2), anchor="c")

        tk.Label(centro_Timer, text="00:25:00", bg="#FFFFFF", fg="#1A1A1A", font=("inter", 48, "bold")).pack(anchor="c")