class RecomendacaoAlong:
    def __init__(self, tipoDor_idTipoDor, Alongamento_idAI):
        self.tipoDor_idTipoDor = tipoDor_idTipoDor
        self.Alongamento_idAI = Alongamento_idAI

    @property
    def tipoDor_idTipoDor(self):
        return self._tipoDor_idTipoDor

    @tipoDor_idTipoDor.setter
    def tipoDor_idTipoDor(self, valor):
        if valor is None or (isinstance(valor, int) and valor <= 0):
            raise ValueError("O ID do Tipo de Dor deve ser um número inteiro maior que zero.")
        self._tipoDor_idTipoDor = valor

    @property
    def Alongamento_idAI(self):
        return self._alongamento_idAI

    @Alongamento_idAI.setter
    def Alongamento_idAI(self, valor):
        if valor is None or (isinstance(valor, int) and valor <= 0):
            raise ValueError("O ID do Alongamento deve ser um número inteiro maior que zero.")
        self._alongamento_idAI = valor