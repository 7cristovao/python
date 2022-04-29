#!/usr/bin/env python3


# Lê duas notas de um aluno e calcula sua média,
# mostrando uma mensagem no final, de acordo com
# a média apresentada:
#
# Média abaixo de 5.0 REPROVADO
#
# Média entre 5.0 e 6.9 RECUPERAÇÃO
#
# Média 7.0 ou superior APROVADO #

nota1 = float(input('Digite a primeira nota da(o) aluna(o): '))
nota2 = float(input('Digite a segunda nota da(o) aluna(o): '))
média = (nota1 + nota2) / 2
print('A média da(o) aluna(o) foi de {:.1f}:'.format(média))
if média >= 7:
    print('Aprovada(o)')
elif (média >= 5) and (média <= 6.9):
    print('Recuperação')
else:
    print('Reprovada(o)')
