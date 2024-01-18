from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = 'https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500'

argumentos_url = ExtratorArgumentosUrl(url)
moeda_origem, moeda_destino = argumentos_url.extrairArgumentos()
valor = argumentos_url.extrairValor()

print(argumentos_url)
