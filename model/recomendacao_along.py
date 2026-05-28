class recomendacao_along:
    def __init__(self, TipoDor_idTipoDor, Alongamento_idAl, Usuario_idUsuario):
        self.TipoDor_idTipoDor = TipoDor_idTipoDor
        self.Alongamento_idAl = Alongamento_idAl
        self.Usuario_idUsuario = Usuario_idUsuario

    @property
    def TipoDor_idTipoDor(self):
        return self._TipoDor_idTipoDor

    @TipoDor_idTipoDor.setter
    def TipoDor_idTipoDor(self, valor):
        if valor is None or (isinstance(valor, int) and valor <= 0):
            raise ValueError("O ID do Tipo de Dor deve ser um número inteiro maior que zero.")
        self._TipoDor_idTipoDorr = valor

    @property
    def Alongamento_idAl(self):
        return self._Alongamento_idAl

    @Alongamento_idAl.setter
    def Alongamento_idAl(self, valor):
        if valor is None or (isinstance(valor, int) and valor <= 0):
            raise ValueError("O ID do Alongamento deve ser um número inteiro maior que zero.")
        self._Alongamento_idAl = valor

    @property
    def Usuario_idUsuario(self):
        return self._Usuario_idUsuario
    
    @Usuario_idUsuario.setter
    def Usuario_idUsuario(self, valor):
        if valor is None or (isinstance(valor, int) and valor <= 0):
            raise ValueError("O ID do Usuario deve ser um número inteiro maior que zero.")
        self._Usuario_idUsuario = valor