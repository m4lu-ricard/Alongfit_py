import tkinter as tk
from datetime import datetime
from controller.auth_controller import AuthController


BG_VERDE_CLARO  = "#EEF4EF"
BG_BRANCO       = "#FFFFFF"
BG_CAMPO        = "#F7FAF8"
BG_BOTAO_VERDE  = "#A7F3D0"
BG_BOTAO_CINZA  = "#E5E7EB"
COR_BORDA       = "#D9E4DA"
COR_TEXTO       = "#000000"
COR_LABEL_SEC   = "#888888"


def botao_redondo(parent, text, command, bg, fg, width=120, height=40, radius=20):
    canvas = tk.Canvas(parent, width=width, height=height, bg=parent["bg"], highlightthickness=0)

    canvas.create_oval(0, 0, radius*2, radius*2, fill=bg, outline=bg)
    canvas.create_oval(width-radius*2, 0, width, radius*2, fill=bg, outline=bg)
    canvas.create_oval(0, height-radius*2, radius*2, height, fill=bg, outline=bg)
    canvas.create_oval(width-radius*2, height-radius*2, width, height, fill=bg, outline=bg)
    canvas.create_rectangle(radius, 0, width-radius, height, fill=bg, outline=bg)
    canvas.create_rectangle(0, radius, width, height-radius, fill=bg, outline=bg)

    canvas.create_text(width//2, height//2, text=text, fill=fg,
                       font=("Helvetica", 13, "bold"))

    canvas.bind("<Button-1>", lambda e: command())
    return canvas


def campo_com_label(parent, texto_label, **entry_kwargs):
    tk.Label(
        parent, text=texto_label, bg=parent["bg"],
        fg=COR_LABEL_SEC, font=("Helvetica", 10, "bold")
    ).pack(fill="x", pady=(10, 3))

    entry = tk.Entry(
        parent,
        font=("Helvetica", 13),
        bg="#FFFFFF",
        fg="#000000",
        relief="solid",
        bd=1,
        highlightthickness=2,
        highlightbackground="#2e7d52", 
        highlightcolor="#2e7d52",
        insertbackground="#000000",
        **entry_kwargs
    )
    entry.pack(fill="x", ipady=10, pady=(0, 6))
    return entry


class CadastroPage(tk.Frame):
    def __init__(self, parent, app=None):
        super().__init__(parent, bg=BG_VERDE_CLARO)
        self.app = app
        self.auth_controller = AuthController()
        self._build()
        if self.app and hasattr(self.app, 'config_tema_escuro'):
            self.aplicar_tema(self.app.config_tema_escuro)

    def _build(self):
        self.contorno = tk.Frame(self, bg=BG_VERDE_CLARO)
        self.contorno.pack(expand=True, fill="both")

        self.barra_superior = tk.Frame(self.contorno, bg=BG_VERDE_CLARO)
        self.barra_superior.pack(fill="x", padx=20, pady=10)

        self.cartao = tk.Frame(
            self.contorno, bg=BG_BRANCO,
            highlightthickness=1, highlightbackground=COR_BORDA
        )
        self.cartao.pack(expand=True, fill="both", padx=40, pady=(0, 30))

        self.conteudo_cartao = tk.Frame(self.cartao, bg=BG_BRANCO)
        self.conteudo_cartao.pack(expand=True)

        # Título
        self.lbl_titulo = tk.Label(
            self.conteudo_cartao, text="Cadastro",
            bg=BG_BRANCO, fg=COR_TEXTO,
            font=("Helvetica", 28, "bold")
        )
        self.lbl_titulo.pack(pady=(0, 6))

        # Subtítulo 
        self.lbl_subtitulo = tk.Label(
            self.conteudo_cartao, text="Crie sua conta para começar",
            bg=BG_BRANCO, fg=COR_LABEL_SEC,
            font=("Helvetica", 12)
        )
        self.lbl_subtitulo.pack(pady=(0, 18))

        # Campos com helper function
        self.ent_nome  = campo_com_label(self.conteudo_cartao, "NOME")
        self.ent_email = campo_com_label(self.conteudo_cartao, "EMAIL")
        self.ent_senha = campo_com_label(self.conteudo_cartao, "SENHA", show="*")
        self.ent_data  = campo_com_label(self.conteudo_cartao, "DATA DE NASCIMENTO  ·  DD/MM/AAAA")

        # Status (erro / sucesso)
        self.lbl_status = tk.Label(
            self.conteudo_cartao, text="",
            bg=BG_BRANCO, fg="#888888",
            font=("Helvetica", 11)
        )
        self.lbl_status.pack(pady=(14, 0))

        # Separador fino
        tk.Frame(self.conteudo_cartao, bg=COR_BORDA, height=1).pack(
            fill="x", pady=(14, 0)
        )

        # Botões
        self.container_botoes = tk.Frame(self.conteudo_cartao, bg=BG_BRANCO)
        self.container_botoes.pack(pady=(16, 8))

        self.btn_voltar = botao_redondo(
            self.container_botoes, "Voltar",
            lambda: self.app.show_page("login"),
            bg=BG_BOTAO_CINZA, fg="#555555",
            width=110, height=40, radius=20
        )
        self.btn_voltar.pack(side="left", padx=8)

        self.btn_cadastrar = botao_redondo(
            self.container_botoes, "Cadastrar",
            self._executar_cadastro,
            bg=BG_BOTAO_VERDE, fg="#1a5c38",
            width=130, height=40, radius=20
        )
        self.btn_cadastrar.pack(side="left", padx=8)

    def _set_status(self, texto, cor="#888888"):
        self.lbl_status.config(text=texto, fg=cor)

    def _executar_cadastro(self):
        nome           = self.ent_nome.get().strip()
        email          = self.ent_email.get().strip()
        senha          = self.ent_senha.get().strip()
        data_nasc_input = self.ent_data.get().strip()

        if not nome or not email or not senha or not data_nasc_input:
            self._set_status("Preencha todos os campos.", "#B05050")
            return

        try:
            data_obj    = datetime.strptime(data_nasc_input, "%d/%m/%Y")
            data_nasc_db = data_obj.strftime("%Y-%m-%d")
        except ValueError:
            self._set_status("Data inválida. Use o formato DD/MM/AAAA.", "#B05050")
            return

        sucesso, mensagem = self.auth_controller.cadastrar_novo_usuario(
            nome, email, senha, data_nasc_db
        )

        if sucesso:
            self._set_status(mensagem, "#2e7d52")
            self.after(2000, lambda: self.app.show_page("login"))
        else:
            self._set_status(mensagem, "#B05050")

    def aplicar_tema(self, escuro: bool):
        cor_tela        = "#AEB9B0" if escuro else BG_VERDE_CLARO
        cor_cartao      = "#F8FAF7" if escuro else BG_BRANCO
        cor_campo       = "#FFFFFF" if escuro else BG_CAMPO
        cor_borda       = "#7F8C82" if escuro else COR_BORDA
        cor_botao_acao  = "#B8E6C6" if escuro else BG_BOTAO_VERDE
        cor_botao_neutro = "#D2DDD4" if escuro else BG_BOTAO_CINZA
        cor_texto       = COR_TEXTO
        cor_label_sec   = "#AAAAAA" if escuro else COR_LABEL_SEC

        self.configure(bg=cor_tela)
        self.contorno.configure(bg=cor_tela)
        self.barra_superior.configure(bg=cor_tela)
        self.cartao.configure(bg=cor_cartao, highlightbackground=cor_borda)
        self.conteudo_cartao.configure(bg=cor_cartao)
        self.container_botoes.configure(bg=cor_cartao)

        self.lbl_titulo.configure(bg=cor_cartao, fg=cor_texto)
        self.lbl_subtitulo.configure(bg=cor_cartao, fg=cor_label_sec)
        self.lbl_status.configure(bg=cor_cartao)

        # Labels dos campos (filhos diretos do conteudo_cartao do tipo Label)
        for widget in self.conteudo_cartao.winfo_children():
            if isinstance(widget, tk.Label) and widget not in (
                self.lbl_titulo, self.lbl_subtitulo, self.lbl_status
            ):
                widget.configure(bg=cor_cartao, fg=cor_label_sec)
            elif isinstance(widget, tk.Frame) and widget is not self.container_botoes:
                widget.configure(bg=cor_borda)  # separador

        for entry in (self.ent_nome, self.ent_email, self.ent_senha, self.ent_data):
            entry.configure(
                bg=cor_campo, fg=cor_texto,
                insertbackground=cor_texto,
                highlightbackground=cor_borda,
                highlightcolor=cor_botao_acao
            )

        # Atualiza bg dos Canvas dos botões
        self.btn_voltar.configure(bg=cor_cartao)
        self.btn_cadastrar.configure(bg=cor_cartao)