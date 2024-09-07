''' Crie um programa que tenha uma função 
    chamada voto() que vai receber como 
    parâmetro o ano de nascimento de uma
    pessoa, retornando um valor literal
    indicando se uma pessoa tem voto 
    NEGADO, OPCIONAL ou OBRIGATÓRIO nas 
    eleições. '''



def voto(anoNascimento):
    from datetime import datetime
    
    anoAtual = datetime.now().year
    idade = anoAtual - anoNascimento
    if idade >= 65 or idade >=16 and idade <= 17:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: VOTO NEGADO.'

anoNascimento = int(input('Em que ano você nasceu? '))
print(voto(2000))
