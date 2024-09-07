''' Faça um programa que
    leia o ano de nascimento
    de um jovem e informe,
    de acordo com sua idade,
    se ele ainda vai se alistar
    ao serviço militar, se é
    a hora de se alistar ou se
    já passou do tempo do 
    alistamento.
    Seu programa também deverá
    mostrar o tempo que falta
    ou que passou do prazo. '''

from datetime import datetime 

anoAtual = datetime.now().year
print(f'O ano atual é {anoAtual}')
anoDeNascimento = int(input('Digite o ano de nascimento: '))
idade = anoAtual - anoDeNascimento

if idade < 17:
    print(f'Ainda vai se alistar. Falta {17 - idade} ano(s) para o alistamento')
elif idade == 17:
    print('Está na hora de se alistar')
else:
    print(f'Passou do prazo para se alistar.')