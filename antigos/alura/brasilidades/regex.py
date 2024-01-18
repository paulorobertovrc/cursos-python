from Telefones_br import Telefones_br
import re

telefone = '552126481234'
telefone_objeto = Telefones_br(telefone)
#padrao = '([0-9]{1,3})([0-9]{2})([0-9]{4,5})([0-9]{4})'
#resposta = re.search(padrao, telefone)
#print(resposta.group(1))

print(telefone_objeto)
