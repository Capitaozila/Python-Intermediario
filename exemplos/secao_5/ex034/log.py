from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, mensagem):
        raise NotImplementedError('Implemente o método log')

    def log_error(self, mensagem):
        return self._log(f'Error: {mensagem}')

    def log_sucess(self, mensagem):
        return self._log(f'Sucess: {mensagem}')


class LogFileMixin(Log):
    def _log(self, mensagem):
        mensagem_formatada = f'{mensagem} ({self.__class__.__name__})'
        print('SALVANDO NO LOG...', mensagem_formatada)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(mensagem_formatada)
            arquivo.write('\n')


class LogPrintMixin(Log):
    def _log(self, mensagem):
        print(f'{mensagem} ({self.__class__.__name__})')


if __name__ == '__main__':
    log_print = LogPrintMixin()
    log_print.log_error('qualquer coisa')
    log_print.log_sucess('deu certo!')
    log_file = LogFileMixin()
    log_file.log_error('qualquer coisa')
    log_file.log_sucess('deu certo!')
