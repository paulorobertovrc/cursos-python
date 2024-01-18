from datetime import datetime, timedelta

class Datas_br:
    def __init__(self):
        self.momento_cadastro = datetime.today()
    
    def __str__(self):
        return self.data_formatada()
    
    def mes_cadastro(self):
        meses_do_ano = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
        return meses_do_ano[self.momento_cadastro.month - 1]
    
    def semana_cadastro(self):
        dias_da_semana = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
        return dias_da_semana[self.momento_cadastro.weekday()]
    
    def data_formatada(self):
        return self.momento_cadastro.strftime('%d/%m/%Y %H:%M')
    
    def tempo_cadastro(self):
        return (datetime.today() + timedelta(days=30)) - self.momento_cadastro
