#!/usr/bin/env python3


# Desenvolva um programa que lê duas notas de um estudante, 
# calcula e apresenta a média dele
 
nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
input('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(nota1, nota2, (nota1 + nota2) / 2))
