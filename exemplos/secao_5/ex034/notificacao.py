from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('Email: enviando: -', self.mensagem)
        return True


class NotificacaoSms(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando: -', self.mensagem)
        return False


def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')

    else:
        print('\rNotificação NÃO enviada')


noticacao_email = NotificacaoEmail('testando notificação de email')
notificar(noticacao_email)
# noticacao_email.enviar()

notificacao_sms = NotificacaoSms('testando notificação de SMS')
notificar(notificacao_sms)
# notificacao_sms.enviar()
