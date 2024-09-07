''' Crie um programa que leia a idade e o 
    sexo de várias pessoas. A cada pessoa 
    cadastrada, o programa deverá perguntar
    se o usuário quer ou não continuar.
    No final, mostre: 
    
    A) quantas pessoas tem mais de 18 anos.
    B) Quantos homens foram cadastrados.
    C) Quantas mulheres tem menos de 20 anos.'''

contMaiorDe18 = contHomens = contMulheresMenoresDe20 = 0
while True:
    idade = int(input('Digite a idade: '))
    if idade > 18:
        contMaiorDe18 = contMaiorDe18 + 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo (M/F): ')).strip().upper()[0]
        if sexo == 'M':
            contHomens = contHomens + 1
        if sexo == 'F' and idade < 20:
            contMulheresMenoresDe20 = contMulheresMenoresDe20 + 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? (S/N):')).strip().upper()[0]
    if resposta == 'N':
        print('Programa Finalizado!')
        break
print(f'{contMaiorDe18} pessoas tem mais de 18 anos')
print(f'{contHomens} homem(ns) foram cadastrados')
print(f'{contMulheresMenoresDe20} mulher(es) tem menos de 20 anos')
print('Fim do programa!')