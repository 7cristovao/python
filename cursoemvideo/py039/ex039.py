#!/usr/bin/env python3


# Escreva um programa que lê o ano de nascimento de um jovem e informa
# de acordo com sua idade:
# (1) Se ele AINDA VAI SE ALISTAR à junta
# (2) Se é a HORA DE SE ALISTAR
# (3) Se já PASSOU DO TEMPO do alistamento

# Seu programa tambem deverá informar o tempo que falta ou que passou do prazo

# an : ano de nascimento
# AA : ano atual

import datetime

an = input('Digite o ano de nascimento: ')
AA = str(datetime.date.today())
AA = AA[0:4]
idade = int(AA) - int(an)
print(idade)
if idade < 17:
    print('Ainda vai se alistar à junta')
elif idade == 17:
    print('Hora de se alistar')
else:
    print('Alistado servindo, reservista ou já passou do tempo do alistamento')
