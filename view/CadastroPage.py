import tkinter as tk
from datetime import datetime
from controller.auth_controller import AuthController

class CadastroPage(tk.Frame):
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

        self.cartao = tk.Frame(self.contorno, bg="#FFFFFF", highlightthickness=1)
        self.cartao.pack(expand=True, fill="both", padx=40, pady=(0, 30))

        self.conteudo_cartao = tk.Frame(self.cartao, bg="#FFFFFF")
        self.conteudo_cartao.pack(expand=True)

        self.lbl_titulo = tk.Label(
            self.conteudo_cartao, text="Cadastro", bg="#FFFFFF", fg="#000000",
            font=("Helvetica", 28, "bold")
        )
        self.lbl_titulo.pack(pady=(0, 15))

        self.lbl_nome = tk.Label(self.conteudo_cartao, text="Nome:", bg="#FFFFFF", fg="#000000", font=("Helvetica", 14, "bold"), anchor="w")
        self.lbl_nome.pack(fill="x", pady=(2, 2))
        self.ent_nome = tk.Entry(self.conteudo_cartao, font=("Helvetica", 12), bg="#F5F5F5", fg="#000000", relief="flat", highlightthickness=1, highlightbackground="#CCCCCC")
        self.ent_nome.pack(fill="x", ipady=6, pady=(0, 10))

        self.lbl_email = tk.Label(self.conteudo_cartao, text="Email:", bg="#FFFFFF", fg="#000000", font=("Helvetica", 14, "bold"), anchor="w")
        self.lbl_email.pack(fill="x", pady=(2, 2))
        self.ent_email = tk.Entry(self.conteudo_cartao, font=("Helvetica", 12), bg="#F5F5F5", fg="#000000", relief="flat", highlightthickness=1, highlightbackground="#CCCCCC")
        self.ent_email.pack(fill="x", ipady=6, pady=(0, 10))

        self.lbl_senha = tk.Label(self.conteudo_cartao, text="Senha:", bg="#FFFFFF", fg="#000000", font=("Helvetica", 14, "bold"), anchor="w")
        self.lbl_senha.pack(fill="x", pady=(2, 2))
        self.ent_senha = tk.Entry(self.conteudo_cartao, font=("Helvetica", 12), bg="#F5F5F5", fg="#000000", show="*", relief="flat", highlightthickness=1, highlightbackground="#CCCCCC")
        self.ent_senha.pack(fill="x", ipady=6, pady=(0, 10))

        self.lbl_data = tk.Label(self.conteudo_cartao, text="Data de Nascimento (DD/MM/AAAA):", bg="#FFFFFF", fg="#000000", font=("Helvetica", 14, "bold"), anchor="w")
        self.lbl_data.pack(fill="x", pady=(2, 2))
        self.ent_data = tk.Entry(self.conteudo_cartao, font=("Helvetica", 12), bg="#F5F5F5", fg="#000000", relief="flat", highlightthickness=1, highlightbackground="#CCCCCC")
        self.ent_data.pack(fill="x", ipady=6, pady=(0, 10))

        self.lbl_status = tk.Label(self.conteudo_cartao, text="", bg="#FFFFFF", fg="#000000", font=("Helvetica", 12, "bold"))
        self.lbl_status.pack(pady=5)

        self.container_botoes = tk.Frame(self.conteudo_cartao, bg="#FFFFFF")
        self.container_botoes.pack(pady=(10, 0))

        self.btn_voltar = tk.Button(
            self.container_botoes, text="Voltar", bg="#E5E7EB", fg="#000000",
            font=("Helvetica", 14), relief="flat", cursor="hand2", padx=20, pady=5,
            command=lambda: self.app.show_page("login")
        )
        self.btn_voltar.pack(side="left", padx=10)

        self.btn_cadastrar = tk.Button(
            self.container_botoes, text="Cadastrar", bg="#A7F3D0", fg="#000000",
            font=("Helvetica", 14, "bold"), relief="flat", cursor="hand2", padx=20, pady=5,
            command=self._executar_cadastro
        )
        self.btn_cadastrar.pack(side="left", padx=10)

    def aplicar_tema(self, escuro: bool):
        cor_tela = "#AEB9B0" if escuro else "#EEF4EF"
        cor_cartao = "#F8FAF7" if escuro else "#FFFFFF"
        cor_campo = "#FFFFFF" if escuro else "#F7FAF8"
        cor_borda = "#7F8C82" if escuro else "#D9E4DA"
        cor_botao_neutro = "#DFE8E0" if escuro else "#E9EFEA"
        cor_botao_acao = "#B8E6C6" if escuro else "#A7F3D0"
        cor_texto = "#000000"

        self.configure(bg=cor_tela)
        self.contorno.configure(bg=cor_tela)
        self.barra_superior.configure(bg=cor_tela)
        self.cartao.configure(bg=cor_cartao, highlightbackground=cor_borda,
                              highlightcolor=cor_borda)
        self.conteudo_cartao.configure(bg=cor_cartao)
        self.container_botoes.configure(bg=cor_cartao)
        for label in [self.lbl_titulo, self.lbl_nome, self.lbl_email, self.lbl_senha, self.lbl_data, self.lbl_status]:
            label.configure(bg=cor_cartao, fg=cor_texto)
        for entrada in [self.ent_nome, self.ent_email, self.ent_senha, self.ent_data]:
            entrada.configure(bg=cor_campo, fg=cor_texto, insertbackground=cor_texto)
        self.btn_voltar.configure(bg=cor_botao_neutro, fg=cor_texto,
                                  activebackground="#D2DDD4", activeforeground=cor_texto)
        self.btn_cadastrar.configure(bg=cor_botao_acao, fg=cor_texto,
                                     activebackground="#9DE7B9", activeforeground=cor_texto)

    def _executar_cadastro(self):
        nome = self.ent_nome.get().strip()
        email = self.ent_email.get().strip()
        senha = self.ent_senha.get().strip()
        data_nasc_input = self.ent_data.get().strip()

        if not nome or not email or not senha or not data_nasc_input:
            self.lbl_status.config(fg="#000000", text="Preencha todos os campos.")
            return

        try:
            data_obj = datetime.strptime(data_nasc_input, "%d/%m/%Y")
            
            data_nasc_db = data_obj.strftime("%Y-%m-%d")
            
        except ValueError:
            self.lbl_status.config(fg="#000000", text="Data inválida. Use o formato DD/MM/AAAA.")
            return

        sucesso, mensagem = self.auth_controller.cadastrar_novo_usuario(nome, email, senha, data_nasc_db)

        if sucesso:
            self.lbl_status.config(fg="#000000", text=mensagem)
            self.after(2000, lambda: self.app.show_page("login"))
        else:
            self.lbl_status.config(fg="#000000", text=mensagem)
