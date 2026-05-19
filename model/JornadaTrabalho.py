class JornadaTrabalho:
    def __init__(self, id, inicioJornd, tempoLembrete, usuario_idUsuario, fimJond=None):
        self.id = id
        self.inicioJornd = inicioJornd
        self.tempoLembrete = tempoLembrete
        self.usuario_idUsuario = usuario_idUsuario
        self.fimJond = fimJond

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
    def usuario_idUsuario(self):
        return self._usuario_idUsuario

    @usuario_idUsuario.setter
    def usuario_idUsuario(self, valor):
        if valor is not None and int(valor) <= 0:
            raise ValueError("O ID do usuário deve ser um número maior que zero.")
        self._usuario_idUsuario = valor

    @property
    def fimJond(self):
        return self._fimJond

    @fimJond.setter
    def fimJond(self, valor):
        self._fimJond = valor