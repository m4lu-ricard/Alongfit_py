class TipoDor:
    def __init__(self, idTipoDor, nome, descricao, regiao_corpo):
        self.idTipoDor = idTipoDor
        self.nome = nome
        self.descricao = descricao
        self.regiao_corpo = regiao_corpo
        
        self._recomendacoes = []
        self._usuarios_com_dor = []

    @property
    def idTipoDor(self):
        return self._idTipoDor

    @idTipoDor.setter
    def idTipoDor(self, valor):
        self._idTipoDor = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor or str(valor).strip() == "":
            raise ValueError("O nome do tipo de dor não pode ser vazio.")
        self._nome = valor

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, valor):
        self._descricao = valor if valor else ""

    @property
    def regiao_corpo(self):
        return self._regiao_corpo

    @regiao_corpo.setter
    def regiao_corpo(self, valor):
        if not valor or str(valor).strip() == "":
            raise ValueError("A região do corpo associada à dor deve ser especificada.")
        self._regiao_corpo = valor

    @property
    def recomendacoes(self):
        return self._recomendacoes

    @recomendacoes.setter
    def recomendacoes(self, valor):
        if not isinstance(valor, list):
            raise TypeError("Recomendações deve ser uma lista.")
        self._recomendacoes = valor

    @property
    def usuarios_com_dor(self):
        return self._usuarios_com_dor

    @usuarios_com_dor.setter
    def usuarios_com_dor(self, valor):
        if not isinstance(valor, list):
            raise TypeError("Usuários com dor deve ser uma lista.")
        self._usuarios_com_dor = valor