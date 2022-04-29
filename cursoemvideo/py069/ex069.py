#!/usr/bin/env python3 

# Crie um programa que lê a IDADE  e o SEXO  de 
# VÁRIAS PESSOAS. A cada pessoa cadastrada, o programa 
# deverá perguntar se o USUÁRIO  quer ou não continuar.
# No final mostre:

# (A) quantas pessoas tem mais de 18 ANOS
# (B) Quantos HOMENS foram cadastrados
# (C) Quantas MULHERES tem menos de 20 ANOS

c_idade_maior_18 = 0
c_sexo_m = 0
c_sexo_f_menor_20 = 0

while True:
    idade = int(input('idade = '))
    sexo = str(input('sexo M/F = ')).strip().upper()[0]
    continua = str(input('Quer continuar? S/N? ')).strip().upper()[0]
    if continua == 'N':
        if idade >= 18:
            c_idade_maior_18 += 1
            if sexo == 'M':
                c_sexo_m += 1
            elif sexo == 'F' and idade <= 20:
                c_sexo_f_menor_20 += 1
            else:
                print('Digitou errado')
                break
        elif idade < 18:
            c_idade_maior_18 = c_idade_maior_18
            if sexo == 'M':
                c_sexo_m += 1
            elif sexo == 'F' and idade <= 20:
                c_sexo_f_menor_20 += 1
            else:
                print('Digitou errado')
                break         
        else:
            print('Digitou errado')
            break       
        break  # fim do continua NAO
    elif continua == 'S':
        if idade >= 18:
            c_idade_maior_18 += 1
            if sexo == 'M':
                c_sexo_m += 1
            elif sexo == 'F' and idade <= 20:
                c_sexo_f_menor_20 += 1
            elif sexo == 'F' and idade > 20:
                c_sexo_f_menor_20 = c_sexo_f_menor_20
            else:
                print('Digitou errado')
                break

        elif idade < 18:
            c_idade_maior_18 = c_idade_maior_18
            if sexo == 'M':
                c_sexo_m += 1
            elif sexo == 'F' and idade <= 20:
                c_sexo_f_menor_20 += 1
            else:
                print('Digitou errado')
                break         
        else:
            print('Digitou errado')
            break
    else:
        print('Digitou errado')
        break

print('Com idade >= 18 tem {} pessoas'.format(c_idade_maior_18))
print('São {} homens'.format(c_sexo_m))
print('Há {} mulheres c/ idade menor ou = que 20 anos'.format(c_sexo_f_menor_20))
print('fim')
