import tkinter as tk
from pathlib import Path
from controller.auth_controller import AuthController

class LoginPage(tk.Frame):
    def __init__(self, parent, app=None):
        super().__init__(parent, bg="#D9D9D9")
        self.app = app
        self.auth_controller = AuthController()
        self.assets_dir = Path(__file__).resolve().parent.parent / "assets"
        self._build()
        if self.app and hasattr(self.app, 'config_tema_escuro'):
            self.aplicar_tema(self.app.config_tema_escuro)

    def _build(self):
        self.contorno = tk.Frame(self, bg="#D9D9D9")
        self.contorno.pack(expand=True, fill="both")

        self.barra_superior = tk.Frame(self.contorno, bg="#D9D9D9")
        self.barra_superior.pack(fill="x", padx=20, pady=10)
        
        self.btn_fechar = tk.Button(
            self.barra_superior, text="X", bg="#D9D9D9", fg="#000000",
            font=("Helvetica", 18, "bold"), relief="flat", 
            cursor="hand2", command=self._fechar_aplicativo
        )
        self.btn_fechar.pack(side="right")

        self.cartao = tk.Frame(self.contorno, bg="#FFFFFF", highlightthickness=1)
        self.cartao.pack(expand=True, padx=80, pady=(20, 60), ipadx=70, ipady=45)

        self.conteudo_cartao = tk.Frame(self.cartao, bg="#FFFFFF")
        self.conteudo_cartao.pack(expand=True)

        try:
            self.logo_login = tk.PhotoImage(file=self.assets_dir / "logo.png").subsample(2, 2)
            self.lbl_logo = tk.Label(self.conteudo_cartao, image=self.logo_login, bg="#FFFFFF")
            self.lbl_logo.pack(pady=(0, 8))
        except Exception:
            self.lbl_logo = None

        self.lbl_titulo = tk.Label(
            self.conteudo_cartao, text="AlongFit", bg="#FFFFFF", fg="#000000",
            font=("Helvetica", 34, "bold")
        )
        self.lbl_titulo.pack(pady=(0, 4))

        self.lbl_subtitulo = tk.Label(
            self.conteudo_cartao, text="Entre para organizar suas pausas e alongamentos",
            bg="#FFFFFF", fg="#000000", font=("Helvetica", 13)
        )
        self.lbl_subtitulo.pack(pady=(0, 28))

        self.lbl_email = tk.Label(
            self.conteudo_cartao, text="Email", bg="#FFFFFF", fg="#000000",
            font=("Helvetica", 13, "bold"), anchor="w"
        )
        self.lbl_email.pack(fill="x", pady=(5, 5))
        
        self.ent_email = tk.Entry(
            self.conteudo_cartao, font=("Helvetica", 14), bg="#F5F5F5", fg="#000000",
            relief="flat", highlightthickness=1, highlightbackground="#CCCCCC"
        )
        self.ent_email.pack(fill="x", ipady=10, pady=(0, 16))

        self.lbl_senha = tk.Label(
            self.conteudo_cartao, text="Senha", bg="#FFFFFF", fg="#000000",
            font=("Helvetica", 13, "bold"), anchor="w"
        )
        self.lbl_senha.pack(fill="x", pady=(5, 5))
        
        self.ent_senha = tk.Entry(
            self.conteudo_cartao, font=("Helvetica", 14), bg="#F5F5F5", fg="#000000",
            show="*", relief="flat", highlightthickness=1, highlightbackground="#CCCCCC"
        )
        self.ent_senha.pack(fill="x", ipady=10, pady=(0, 10))

        self.lbl_erro = tk.Label(self.conteudo_cartao, text="", bg="#FFFFFF", fg="#000000", font=("Helvetica", 12, "bold"))
        self.lbl_erro.pack(pady=5)

        self.btn_login = tk.Button(
            self.conteudo_cartao, text="Entrar", bg="#FFFFFF", fg="#000000",
            font=("Helvetica", 16, "bold"), relief="flat", bd=0, cursor="hand2",
            padx=34, pady=10, command=self._executar_login
        )
        self.btn_login.pack(fill="x", pady=(10, 0))

        self.btn_cadastro = tk.Button(
            self.conteudo_cartao,
            text="Criar uma nova conta",
            bg="#F3F7F4",
            fg="#2E2E2E",
            font=("Helvetica", 12, "bold"),
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=18,
            pady=10,
            activebackground="#E6EFE8",
            activeforeground="#000000",
            command=lambda: self.app.show_page("cadastro")
        )
        self.btn_cadastro.pack(pady=(20, 0))

        def on_enter_cadastro(e):
            self.btn_cadastro.configure(bg="#E6EFE8")

        def on_leave_cadastro(e):
            self.btn_cadastro.configure(bg="#F3F7F4")

        self.btn_cadastro.bind("<Enter>", on_enter_cadastro)
        self.btn_cadastro.bind("<Leave>", on_leave_cadastro)

    def aplicar_tema(self, escuro: bool):
        cor_tela = "#AEB9B0" if escuro else "#EEF4EF"
        cor_cartao = "#F8FAF7" if escuro else "#FFFFFF"
        cor_campo = "#FFFFFF" if escuro else "#F7FAF8"
        cor_borda = "#7F8C82" if escuro else "#D9E4DA"
        cor_botao = "#B8E6C6" if escuro else "#EAF7EE"
        cor_hover = "#9DE7B9" if escuro else "#B8E6C6"
        cor_texto = "#000000" if escuro else "#000000"

        self.configure(bg=cor_tela)
        self.contorno.configure(bg=cor_tela)
        self.barra_superior.configure(bg=cor_tela)
        self.btn_fechar.configure(bg=cor_tela, fg=cor_texto,
                                  activebackground=cor_tela, activeforeground=cor_texto)
        self.cartao.configure(bg=cor_cartao, highlightbackground=cor_borda,
                              highlightcolor=cor_borda)
        self.conteudo_cartao.configure(bg=cor_cartao)
        labels = [self.lbl_titulo, self.lbl_subtitulo, self.lbl_email, self.lbl_senha, self.lbl_erro]
        if self.lbl_logo:
            self.lbl_logo.configure(bg=cor_cartao)
        for label in labels:
            label.configure(bg=cor_cartao, fg=cor_texto)
        for entrada in [self.ent_email, self.ent_senha]:
            entrada.configure(bg=cor_campo, fg=cor_texto, insertbackground=cor_texto,
                              highlightbackground=cor_borda, highlightcolor=cor_botao)
        for botao in [self.btn_login, self.btn_cadastro]:
            botao.configure(bg=cor_botao, fg=cor_texto,
                            activebackground=cor_hover, activeforeground=cor_texto)

    def _executar_login(self):
        email = self.ent_email.get().strip()
        senha = self.ent_senha.get().strip()
        self.lbl_erro.config(text="")

        if not email or not senha:
            self.lbl_erro.config(text="Por favor, preencha todos os campos.")
            return

        sucesso, mensagem = self.auth_controller.realizar_login(email, senha)

        if sucesso:
            id_usuario = self.auth_controller.identificador_usuario_ativo
            if self.app:
                self.app.inicializar_sistema_pos_login(id_usuario)
        else:
            self.lbl_erro.config(text=mensagem)

    def _fechar_aplicativo(self):
        if self.app:
            self.app.quit()
