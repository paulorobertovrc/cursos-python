def notas(* n, sit=False):
    """
    -> Função para analisar notas e situações de alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional que indica se deve ou não exibir a situação
    :return: dicionário contendo várias informações sobre a situação da turma
    """
    boletim = dict()
    boletim['total'] = len(n)
    boletim['maior'] = max(n)
    boletim['menor'] = min(n)
    boletim['média'] = sum(n) / len(n)
    if sit:
        if boletim['média'] < 6:
            boletim['situação'] = 'RUIM'
        elif boletim['média'] < 7:
            boletim['situação'] = 'REGULAR'
        else:
            boletim['situação'] = 'BOA'
    return boletim


print(notas(5.5, 2.5, 1.5, sit=True))
print(notas(5.5, 6.5, 6.5, sit=True))
print(notas(7, 7, 7, 8, 9, 10, sit=True))
