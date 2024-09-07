''' Faça um programa que tenha uma 
    função notas() que pode receber
    várias notas de alunos e vai 
    retornar um dicionário com as
    seguintes informações:
    
    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação (opcional) '''

def notas(* avaliacoes, sit):
    """
    → Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicionario = dict()
    soma = media = 0
    for valor in avaliacoes:
        soma = soma + valor
    media = soma / len(avaliacoes)
    dicionario = {'total':len(avaliacoes),
                  'maior':max(avaliacoes),
                  'menor':min(avaliacoes),
                  'média':media}
    if sit == True:
        if media >= 7:
            dicionario['situação'] = 'BOA'
            return dicionario
        elif media >=6 and media < 7:
            dicionario['situação'] = 'RAZOÁVEL'
            return dicionario
        else:
            dicionario['situação'] = 'RUIM'
            return dicionario
    else:
        return dicionario
'''BOA, RAZOÁVEL, RUIM'''


# Programa principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)