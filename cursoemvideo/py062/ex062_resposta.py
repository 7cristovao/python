#!/usr/bin/env python3
#   
# 
# Melhore o exercício 61, perguntando 
# para o usuário se ele quer mostrar
# mais alguns termos. O programa encerra
# quando ele disser que quer mostrar
# ZERO TERMOS

print('Gerador de PA')

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão de PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ¬ '.format(termo), end='')
        termo += razão
        cont += 1
    print('pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
