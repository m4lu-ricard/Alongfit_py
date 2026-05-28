class Pausas:
    def __init__(self, idPausas, inicio, fim, concluida, Usuario_idUsuario):
        self.idPausas = idPausas
        self.inicio = inicio
        self.fim = fim
        self.concluida = concluida
        self.Usuario_idUsuario = Usuario_idUsuario

    @property
    def idPausas(self):
        return self._idPausas

    @idPausas.setter
    def idPausas(self, valor):
        self._idPausas = valor

    @property
    def inicio(self):
        return self._inicio

    @inicio.setter
    def inicio(self, valor):
        if not valor:
            raise ValueError("O horário de início da pausa é obrigatório.")
        self._inicio = valor

    @property
    def fim(self):
        return self._fim

    @fim.setter
    def fim(self, valor):
        self._fim = valor

    @property
    def concluida(self):
        return self._concluida

    @concluida.setter
    def concluida(self, valor):
        opcoes_validas = ['SIM', 'NAO']
        if valor in opcoes_validas:
            self._concluida = valor
        else:
            raise ValueError("O status de conclusão deve ser 'SIM' ou 'NAO'.")

    @property
    def Usuario_idUsuario(self):
        return self._Usuario_idUsuario

    @Usuario_idUsuario.setter
    def Usuario_idUsuario(self, valor):
        if valor is not None and int(valor) <= 0:
            raise ValueError("O ID do usuário deve ser um número válido.")
        self._Usuario_idUsuario = valor