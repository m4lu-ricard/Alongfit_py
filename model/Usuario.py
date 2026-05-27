class Usuario:
    def __init__(self, idUsuario, Nome, email, senha, dataNasc=None):
        self.idUsuario = idUsuario
        self.Nome = Nome
        self.email = email
        self.senha = senha
        self.dataNasc = dataNasc
        
        self._historicos = []
        self._jornadas = []
        self._pausas = []
        self._dores = []

    @property
    def idUsuario(self):
        return self._idUsuario

    @idUsuario.setter
    def idUsuario(self, valor):
        self._idUsuario = valor

    @property
    def Nome(self):
        return self._Nome

    @Nome.setter
    def Nome(self, valor):
        if not valor or str(valor).strip() == "":
            raise ValueError("O nome do usuário não pode ser vazio.")
        self._Nome = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if not valor or "@" not in str(valor):
            raise ValueError("E-mail inválido.")
        self._email = valor

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if not valor or len(str(valor)) < 6:
            raise ValueError("A senha deve conter pelo menos 6 caracteres.")
        self._senha = valor

    @property
    def dataNasc(self):
        return self._dataNasc

    @dataNasc.setter
    def dataNasc(self, valor):
        self._dataNasc = valor

    @property
    def historicos(self):
        return self._historicos

    @historicos.setter
    def historicos(self, valor):
        if not isinstance(valor, list):
            raise TypeError("Históricos deve ser uma lista.")
        self._historicos = valor

    @property
    def jornadas(self):
        return self._jornadas

    @jornadas.setter
    def jornadas(self, valor):
        if not isinstance(valor, list):
            raise TypeError("Jornadas deve ser uma lista.")
        self._jornadas = valor

    @property
    def pausas(self):
        return self._pausas

    @pausas.setter
    def pausas(self, valor):
        if not isinstance(valor, list):
            raise TypeError("Pausas deve ser uma lista.")
        self._pausas = valor

    @property
    def dores(self):
        return self._dores

    @dores.setter
    def dores(self, valor):
        if not isinstance(valor, list):
            raise TypeError("Dores deve ser uma lista.")
        self._dores = valor