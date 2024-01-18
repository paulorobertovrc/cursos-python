class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.urlValida(url):
            self.url = url.lower()
        else:
            raise LookupError('URL inválida!')
    
    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        moeda_origem, moeda_destino = self.extrairArgumentos()
        representacao_string = f'Valor: {self.extrairValor()}\nMoeda Origem: {moeda_origem.capitalize()}\nMoeda Destino: {moeda_destino.capitalize()}\n'
        return representacao_string
    
    def __eq__(self, outra_instancia):
        return self.url == outra_instancia.url
    
    @staticmethod
    def urlValida(url):
        if url and url.startswith('https://www.bytebank.com.br'):
            return True
        else:
            return False
    
    def extrairArgumentos(self):
        busca_moeda_origem = 'moedaorigem='.lower()
        busca_moeda_destino = 'moedadestino='.lower()
        
        indice_inicial_moeda_origem = self.encontraIndiceInicial(busca_moeda_origem)
        indice_final_moeda_origem = self.url.find('&')

        indice_inicial_moeda_destino = self.encontraIndiceInicial(busca_moeda_destino)
        indice_final_moeda_destino = self.url.find('&', 52)
        
        moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]
        moeda_destino = self.url[indice_inicial_moeda_destino:indice_final_moeda_destino]

        return moeda_origem, moeda_destino
    
    def encontraIndiceInicial(self, moeda_buscada):
        return self.url.find(moeda_buscada) + len(moeda_buscada)
    
    def trocaMoedaOrigem(self):
        self.url = self.url.replace('moedadestino', 'real', 1)
    
    def extrairValor(self):
        busca_valor = 'valor='
        indice_inicial_valor = self.encontraIndiceInicial(busca_valor)
        valor = self.url[indice_inicial_valor:]

        return valor
