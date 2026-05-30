import tkinter as tk
from datetime import datetime
from controller.auth_controller import AuthController

class CadastroPage(tk.Frame):
    def __init__(self, parent, app=None):
        super().__init__(parent, bg="#D9D9D9")
        self.app = app
        self.auth_controller = AuthController()
        self._build()

    def _build(self):
        self.contorno = tk.Frame(self, bg="#D9D9D9")
        self.contorno.pack(expand=True, fill="both")

        barra_superior = tk.Frame(self.contorno, bg="#D9D9D9")
        barra_superior.pack(fill="x", padx=20, pady=10)

        cartao = tk.Frame(self.contorno, bg="#FFFFFF")
        cartao.pack(expand=True, fill="both", padx=40, pady=(0, 30))

        conteudo_cartao = tk.Frame(cartao, bg="#FFFFFF")
        conteudo_cartao.pack(expand=True)

        tk.Label(
            conteudo_cartao, text="Cadastro", bg="#FFFFFF", fg="#000000",
            font=("Helvetica", 28, "bold")
        ).pack(pady=(0, 15))

        tk.Label(conteudo_cartao, text="Nome:", bg="#FFFFFF", fg="#1A1A1A", font=("Helvetica", 14, "bold"), anchor="w").pack(fill="x", pady=(2, 2))
        self.ent_nome = tk.Entry(conteudo_cartao, font=("Helvetica", 12), bg="#F5F5F5", relief="flat", highlightthickness=1, highlightbackground="#CCCCCC")
        self.ent_nome.pack(fill="x", ipady=6, pady=(0, 10))

        tk.Label(conteudo_cartao, text="Email:", bg="#FFFFFF", fg="#1A1A1A", font=("Helvetica", 14, "bold"), anchor="w").pack(fill="x", pady=(2, 2))
        self.ent_email = tk.Entry(conteudo_cartao, font=("Helvetica", 12), bg="#F5F5F5", relief="flat", highlightthickness=1, highlightbackground="#CCCCCC")
        self.ent_email.pack(fill="x", ipady=6, pady=(0, 10))

        tk.Label(conteudo_cartao, text="Senha:", bg="#FFFFFF", fg="#1A1A1A", font=("Helvetica", 14, "bold"), anchor="w").pack(fill="x", pady=(2, 2))
        self.ent_senha = tk.Entry(conteudo_cartao, font=("Helvetica", 12), bg="#F5F5F5", show="*", relief="flat", highlightthickness=1, highlightbackground="#CCCCCC")
        self.ent_senha.pack(fill="x", ipady=6, pady=(0, 10))

        tk.Label(conteudo_cartao, text="Data de Nascimento (DD/MM/AAAA):", bg="#FFFFFF", fg="#1A1A1A", font=("Helvetica", 14, "bold"), anchor="w").pack(fill="x", pady=(2, 2))
        self.ent_data = tk.Entry(conteudo_cartao, font=("Helvetica", 12), bg="#F5F5F5", relief="flat", highlightthickness=1, highlightbackground="#CCCCCC")
        self.ent_data.pack(fill="x", ipady=6, pady=(0, 10))

        self.lbl_status = tk.Label(conteudo_cartao, text="", bg="#FFFFFF", fg="#FF3333", font=("Helvetica", 12, "bold"))
        self.lbl_status.pack(pady=5)

        container_botoes = tk.Frame(conteudo_cartao, bg="#FFFFFF")
        container_botoes.pack(pady=(10, 0))

        tk.Button(
            container_botoes, text="Voltar", bg="#E5E7EB", fg="#1A1A1A",
            font=("Helvetica", 14), relief="flat", cursor="hand2", padx=20, pady=5,
            command=lambda: self.app.show_page("login")
        ).pack(side="left", padx=10)

        tk.Button(
            container_botoes, text="Cadastrar", bg="#A7F3D0", fg="#1A1A1A",
            font=("Helvetica", 14, "bold"), relief="flat", cursor="hand2", padx=20, pady=5,
            command=self._executar_cadastro
        ).pack(side="left", padx=10)

    def _executar_cadastro(self):
        nome = self.ent_nome.get().strip()
        email = self.ent_email.get().strip()
        senha = self.ent_senha.get().strip()
        data_nasc_input = self.ent_data.get().strip()

        if not nome or not email or not senha or not data_nasc_input:
            self.lbl_status.config(fg="#FF3333", text="Preencha todos os campos.")
            return

        try:
            data_obj = datetime.strptime(data_nasc_input, "%d/%m/%Y")
            
            data_nasc_db = data_obj.strftime("%Y-%m-%d")
            
        except ValueError:
            self.lbl_status.config(fg="#FF3333", text="Data inválida. Use o formato DD/MM/AAAA.")
            return

        sucesso, mensagem = self.auth_controller.cadastrar_novo_usuario(nome, email, senha, data_nasc_db)

        if sucesso:
            self.lbl_status.config(fg="#10B981", text=mensagem)
            self.after(2000, lambda: self.app.show_page("login"))
        else:
            self.lbl_status.config(fg="#FF3333", text=mensagem)