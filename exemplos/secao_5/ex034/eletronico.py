from log import LogPrintMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if not self._ligado:
            self._ligado = False


class Smartphone(Eletronico, LogPrintMixin):
    def ligar(self):
        super().ligar()
        
        if self._ligado:
            mensagem = f'{self._nome} está ligado'
            self.log_sucess(mensagem)

    def desligar(self):
        super().desligar()
        
        if not self._ligado:
            mensagem = f'{self._nome} está desligado'
            self.log_error(mensagem)
