import tkinter as tk
from controller.auth_controller import AuthController

class LoginPage(tk.Frame):
    def __init__(self, parent, app=None):
        super().__init__(parent, bg="#D9D9D9")
        self.app = app
        self.auth_controller = AuthController()
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

        self.cartao = tk.Frame(self.contorno, bg="#FFFFFF")
        self.cartao.pack(expand=True, fill="both", padx=40, pady=(0, 30))

        self.conteudo_cartao = tk.Frame(self.cartao, bg="#FFFFFF")
        self.conteudo_cartao.pack(expand=True)

        self.lbl_titulo = tk.Label(
            self.conteudo_cartao, text="Login", bg="#FFFFFF", fg="#000000",
            font=("Helvetica", 32, "bold")
        )
        self.lbl_titulo.pack(pady=(0, 20))

        self.lbl_email = tk.Label(
            self.conteudo_cartao, text="Email:", bg="#FFFFFF", fg="#000000",
            font=("Helvetica", 16, "bold"), anchor="w"
        )
        self.lbl_email.pack(fill="x", pady=(5, 5))
        
        self.ent_email = tk.Entry(
            self.conteudo_cartao, font=("Helvetica", 14), bg="#F5F5F5", fg="#000000",
            relief="flat", highlightthickness=1, highlightbackground="#CCCCCC"
        )
        self.ent_email.pack(fill="x", ipady=8, pady=(0, 15))

        self.lbl_senha = tk.Label(
            self.conteudo_cartao, text="Senha:", bg="#FFFFFF", fg="#000000",
            font=("Helvetica", 16, "bold"), anchor="w"
        )
        self.lbl_senha.pack(fill="x", pady=(5, 5))
        
        self.ent_senha = tk.Entry(
            self.conteudo_cartao, font=("Helvetica", 14), bg="#F5F5F5", fg="#000000",
            show="*", relief="flat", highlightthickness=1, highlightbackground="#CCCCCC"
        )
        self.ent_senha.pack(fill="x", ipady=8, pady=(0, 10))

        self.lbl_erro = tk.Label(self.conteudo_cartao, text="", bg="#FFFFFF", fg="#000000", font=("Helvetica", 12, "bold"))
        self.lbl_erro.pack(pady=5)

        self.btn_login = tk.Button(
            self.conteudo_cartao, text="Login", bg="#FFFFFF", fg="#000000",
            font=("Helvetica", 18), relief="groove", bd=2, cursor="hand2",
            padx=30, command=self._executar_login
        )
        self.btn_login.pack(pady=(10, 0))

        self.btn_cadastro = tk.Button(
            self.conteudo_cartao, text="Não tem uma conta? Cadastre-se", bg="#FFFFFF", fg="#000000",
            font=("Helvetica", 12, "underline"), relief="flat", cursor="hand2",
            activebackground="#FFFFFF", activeforeground="#000000",
            command=lambda: self.app.show_page("cadastro")
        )
        self.btn_cadastro.pack(pady=(20, 0))

    def aplicar_tema(self, escuro: bool):
        cor_tela = "#CFCFCF" if escuro else "#D9D9D9"
        cor_cartao = "#F2F2F2" if escuro else "#FFFFFF"
        cor_campo = "#FFFFFF" if escuro else "#F5F5F5"
        cor_texto = "#000000"

        self.configure(bg=cor_tela)
        self.contorno.configure(bg=cor_tela)
        self.barra_superior.configure(bg=cor_tela)
        self.btn_fechar.configure(bg=cor_tela, fg=cor_texto,
                                  activebackground=cor_tela, activeforeground=cor_texto)
        self.cartao.configure(bg=cor_cartao)
        self.conteudo_cartao.configure(bg=cor_cartao)
        for label in [self.lbl_titulo, self.lbl_email, self.lbl_senha, self.lbl_erro]:
            label.configure(bg=cor_cartao, fg=cor_texto)
        for entrada in [self.ent_email, self.ent_senha]:
            entrada.configure(bg=cor_campo, fg=cor_texto, insertbackground=cor_texto)
        for botao in [self.btn_login, self.btn_cadastro]:
            botao.configure(bg=cor_cartao, fg=cor_texto,
                            activebackground=cor_cartao, activeforeground=cor_texto)

    def _executar_login(self):
        email = self.ent_email.get().strip()
        senha = self.ent_senha.get().strip()
        self.lbl_erro.config(text="")

        if not email or not senha:
            self.lbl_erro.config(fg="#000000", text="Por favor, preencha todos os campos.")
            return

        sucesso, mensagem = self.auth_controller.realizar_login(email, senha)

        if sucesso:
            id_usuario = self.auth_controller.identificador_usuario_ativo
            if self.app:
                self.app.inicializar_sistema_pos_login(id_usuario)
        else:
            self.lbl_erro.config(fg="#000000", text=mensagem)

    def _fechar_aplicativo(self):
        if self.app:
            self.app.quit()
