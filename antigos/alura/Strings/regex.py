import re

email1 = 'Meu número é 712341234'
email2 = 'Fale comigo em 91234-1234 esse é meu telefone 1234-5678 99999-8877'
email3 = '12341234 é meu telefone 9876-5432. Meu número é 1234-5678 ou 1234-1234.'

padrao = '[0-9]{4,5}-?[0-9]{4}'

retorno = re.search(padrao, email1)
retorno2 = re.findall(padrao, email2)
retorno3 = re.findall(padrao, email3)
print(retorno.group())
print(retorno2)
print(retorno3)
