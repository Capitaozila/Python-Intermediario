from log import LogPrintMixin, LogFileMixin

log_print = LogPrintMixin()
log_print.log_error('qualquer coisa')
log_print.log_sucess('deu certo!')
log_file = LogFileMixin()
log_file.log_error('qualquer coisa')
log_file.log_sucess('deu certo!')