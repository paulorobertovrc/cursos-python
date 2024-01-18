import requests

class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_valido(cep):
            self.cep = cep
        else:
            raise ValueError('CEP inválido!')
    
    def __str__(self):
        return self.cep_formatado()
    
    def cep_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
    
    def cep_formatado(self):
        return f'{self.cep[:5]}-{self.cep[5:]}'
    
    def acessa_via_cep(self):
        r = requests.get(f'https://viacep.com.br/ws/{self.cep}/json/').json()
        return (
            r['cep'],
            r['logradouro'],
            r['complemento'],
            r['bairro'],
            r['localidade'],
            r['uf']
        )