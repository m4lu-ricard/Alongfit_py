class TempoSessao:
    """Regras de tempo da jornada de trabalho, sem dependência de interface.

    Guarda quanto falta para a próxima pausa (ciclo) e quanto falta para o fim
    da jornada, e decide o que acontece a cada segundo. Quem agenda os segundos
    e mostra o relógio na tela é o SessaoController.
    """

    CICLO_EM_ANDAMENTO = "ciclo_em_andamento"
    FIM_DO_CICLO = "fim_do_ciclo"
    FIM_DA_JORNADA = "fim_da_jornada"

    def __init__(self):
        self.restante_ciclo = 0
        self.restante_jornada = 0
        self.duracao_ciclo = 0

    def configurar(self, horas_trabalho, minutos_pausa):
        self.restante_jornada = horas_trabalho * 3600
        self.duracao_ciclo = minutos_pausa * 60
        self.preparar_proximo_ciclo()

    def preparar_proximo_ciclo(self):
        """O próximo ciclo dura o intervalo configurado, sem passar do fim da jornada."""
        self.restante_ciclo = min(self.duracao_ciclo, self.restante_jornada)

    def avancar_um_segundo(self):
        """Desconta um segundo do ciclo e da jornada e informa a situação seguinte."""
        if self.restante_ciclo > 0:
            self.restante_ciclo -= 1
            self.restante_jornada -= 1
        if self.restante_ciclo > 0:
            return self.CICLO_EM_ANDAMENTO
        if self.jornada_encerrada():
            return self.FIM_DA_JORNADA
        return self.FIM_DO_CICLO

    def descontar_da_jornada(self):
        """Desconta um segundo só da jornada (usado durante o alongamento).

        Retorna False quando a jornada já tinha acabado e nada foi descontado.
        """
        if self.jornada_encerrada():
            return False
        self.restante_jornada -= 1
        return True

    def jornada_encerrada(self):
        return self.restante_jornada <= 0
