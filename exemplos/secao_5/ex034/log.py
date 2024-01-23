class Log:
    def log(self, mensagem):
        raise NotImplementedError('Implemente o método log')
    

class LogFileMixin(Log):
    def log(self, mensagem):
        print(mensagem)
    
    
if __name__ == '__main__':
    l = LogFileMixin()
    l.log('qualquer coisa')