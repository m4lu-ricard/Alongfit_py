class HistoricoAlon:
    def __init__(self, idHisto, Alongamento_idAl, Usuario_idUsuario, Inicio, tempoTotal, dataFim):
        self.idHisto = idHisto
        self.Alongamento_idAl = Alongamento_idAl
        self.Usuario_idUsuario = Usuario_idUsuario
        self.Inicio = Inicio
        self.tempoTotal = tempoTotal
        self.dataFim = dataFim

    @property
    def idHisto(self):
        return self._idHisto

    @idHisto.setter
    def idHisto(self, valor):
        self._idHisto = valor

    @property
    def Alongamento_idAl(self):
        return self._Alongamento_idAl

    @Alongamento_idAl.setter
    def Alongamento_idAI(self, valor):
        if valor is not None and int(valor) <= 0:
            raise ValueError("O ID do alongamento deve ser um número maior que zero.")
        self._Alongamento_idAl = valor

    @property
    def Usuario_idUsuario(self):
        return self._Usuario_idUsuario

    @Usuario_idUsuario.setter
    def Usuario_idUsuario(self, valor):
        if valor is not None and int(valor) <= 0:
            raise ValueError("O ID do usuário deve ser um número maior que zero.")
        self._Usuario_idUsuario = valor

    @property
    def Inicio(self):
        return self._Inicio

    @Inicio.setter
    def Inicio(self, valor):
        if not valor:
            raise ValueError("A data/hora de início é obrigatória.")
        self._Inicio = valor

    @property
    def tempoTotal(self):
        return self._tempoTotal

    @tempoTotal.setter
    def tempoTotal(self, valor):
        if valor is not None and int(valor) < 0:
            raise ValueError("O tempo total não pode ser negativo.")
        self._tempoTotal = valor

    @property
    def dataFim(self):
        return self._dataFim

    @dataFim.setter
    def dataFim(self, valor):
        self._dataFim = valor