class UserDor:
    def __init__(self, tipoDor_idTipoDor, usuario_idUsuario):
        self.tipoDor_idTipoDor = tipoDor_idTipoDor
        self.usuario_idUsuario = usuario_idUsuario

    @property
    def tipoDor_idTipoDor(self):
        return self._tipoDor_idTipoDor

    @tipoDor_idTipoDor.setter
    def tipoDor_idTipoDor(self, valor):
        if valor is None or (isinstance(valor, int) and valor <= 0):
            raise ValueError("O ID do Tipo de Dor deve ser um número inteiro maior que zero.")
        self._tipoDor_idTipoDor = valor

    @property
    def usuario_idUsuario(self):
        return self._usuario_idUsuario

    @usuario_idUsuario.setter
    def usuario_idUsuario(self, valor):
        if valor is None or (isinstance(valor, int) and valor <= 0):
            raise ValueError("O ID do Usuário deve ser um número inteiro maior que zero.")
        self._usuario_idUsuario = valor