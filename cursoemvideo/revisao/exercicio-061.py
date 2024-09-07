''' Refaça o desafio 051, lendo o primeiro
    termo e a razão de uma PA, mostrando
    os 10 primeiros termos da progressão
    usando a estrutura while. '''

# lê a informação do primeiro termo
a1 = int(input('Digite o primeiro termo de uma PA: '))

# lê a informação da razão
r = int(input('Digite a RAZÃO de uma PA: '))

# inicializa termo
termo = a1

# inicializa contador
cont = 1

# exibe os 10 primeiros termos desta progressão
while cont <= 10:
    print(f'{termo} → ', end='') # end='' retira o final da linha
    termo = termo + r
    cont = cont + 1
print('\nFim do programa')