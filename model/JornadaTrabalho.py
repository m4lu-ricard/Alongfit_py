class JornadaTrabalho:
    def __init__(self, id, inicioJornd, tempoLembrete, Usuario_idUsuario, fimJornd):
        self.id = id
        self.inicioJornd = inicioJornd
        self.tempoLembrete = tempoLembrete
        self.Usuario_idUsuario = Usuario_idUsuario
        self.fimJornd = fimJornd

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def inicioJornd(self):
        return self._inicioJornd

    @inicioJornd.setter
    def inicioJornd(self, valor):
        if not valor:
            raise ValueError("O início da jornada de trabalho é obrigatório.")
        self._inicioJornd = valor

    @property
    def tempoLembrete(self):
        return self._tempoLembrete

    @tempoLembrete.setter
    def tempoLembrete(self, valor):
        if valor is not None and int(valor) < 0:
            raise ValueError("O tempo do lembrete não pode ser um valor negativo.")
        self._tempoLembrete = valor

    @property
    def Usuario_idUsuario(self):
        return self._Usuario_idUsuario

    @Usuario_idUsuario.setter
    def Usuario_idUsuario(self, valor):
        if valor is not None and int(valor) <= 0:
            raise ValueError("O ID do usuário deve ser um número maior que zero.")
        self._Usuario_idUsuario = valor

    @property
    def fimJornd(self):
        return self._fimJornd

    @fimJornd.setter
    def fimJornd(self, valor):
        self._fimJornd = valor