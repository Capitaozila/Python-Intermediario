class Log:
    def _log(self, mensagem):
        raise NotImplementedError('Implemente o método log')

    def log_error(self, mensagem):
        return self._log(f'Error: {mensagem}')
    
    def log_sucess(self, mensagem):
        return self._log(f'Sucess: {mensagem}')

class LogFileMixin(Log):
    def _log(self, mensagem):
        print(mensagem)


class LogPrintMixin(Log):
    def _log(self, mensagem):
        print(f'{mensagem} ({self.__class__.__name__})')


if __name__ == '__main__':
    l = LogPrintMixin()
    l.log_error('qualquer coisa')
    l.log_sucess('deu certo!')