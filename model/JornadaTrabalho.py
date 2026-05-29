class JornadaTrabalho:
    def __init__(self, id, inicioJornd, nome, tempoLembrete, usuario_idUsuario, fimJornd):
        self.id = id
        self.inicioJornd = inicioJornd
        self.nome = nome
        self.tempoLembrete = tempoLembrete
        self.usuario_idUsuario = usuario_idUsuario
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
        # Permite que a tarefa nasça sem data de início (pendente)
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
    def fimJornd(self):
        return self._fimJornd

    @fimJornd.setter
    def fimJornd(self, valor):
        self._fimJornd = valor