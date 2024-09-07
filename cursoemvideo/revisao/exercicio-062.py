''' Melhore o desafio 061, perguntando 
    para o usuário se ele quer mostrar 
    mais alguns termos. O programa 
    encerra quando ele disser que quer 
    mostrar 0 termos. '''

# lê a informação do primeiro termo
a1 = int(input('Digite o primeiro termo de uma PA: '))

# lê a informação da razão
r = int(input('Digite a RAZÃO de uma PA: '))

# inicializa termo
termo = a1

# inicializa contador
cont = 1

# inicializa total
total = 0

# inicializa mais
quantosTermosAMais = 10

# exibe os 10 primeiros termos desta progressão
while quantosTermosAMais != 0:
    total = total + quantosTermosAMais
    while cont <= total:
        print(f'{termo} → ', end='' )
        termo = termo + r
        cont = cont + 1
    print('PAUSA')
    quantosTermosAMais = int(input('Quantos termos você quer a mais? '))
print('\nFim do programa')