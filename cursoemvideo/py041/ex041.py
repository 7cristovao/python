#!/usr/bin/env python3


# A Confeder. Nac. de Natação precisa de um código que lê
# o ano de nascimento de um atleta e mostre sua categoria
# de acordo com a idade
#
# Até 9 anos: MIRIM
# Até 14 anos:  INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER #

from datetime import timedelta, date


year = timedelta(days=365)
another_year = timedelta(weeks=40, days=84, hours=23, minutes=50, seconds=600)
# year == another_year
# print(year.total_seconds())

# dn : data de nascimento do atleta
# dh : data de hoje
dat = str(input('Digite a data de nascimento do atleta, formato dd/mm/aaaa: '))
data = dat.split("/")
# print(data)
dia = int(data[0])
# print(dia)
mes = int(data[1])
# print(mes)
ano = int(data[2])
# print(ano)
dn = date(int(ano), int(mes), int(dia))
# print(dn)
# print(type(dn))
dh = date.today()
# print(dh)
# print(type(dh))
diferença = dh - dn
# print(diferença)
# print(type(diferença))
dea = diferença // year
print(f'A idade do atleta é de {dea} anos.')
# dea : diferença em anos  | 10, 15, 20, 21
if dea < 10:
    print('Mirim')
elif dea < 15:
    print('Infantil')
elif dea < 20:
    print('Junior')
elif dea < 21:
    print('Senior')
else:
    print('Master')
