#!/usr/bin/env python3


# Crie um programa que sorteie um aluno da sala de aula
# para apagar a lousa


#    CLASSE        METODO
from random import choice
a = str(input('Primeiro Aluno: '))
b = str(input('Segundo Aluno: '))
c = str(input('Terceiro Aluno: '))
d = str(input('Quarto Aluno: '))
lista = [a,b,c,d]
sorteado = choice(lista)
print('O aluno escolhido foi: {}'.format(sorteado))
