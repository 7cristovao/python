''' Faça um programa que leia o peso 
    de cinco pessoas. No final, mostre
    qual foi o maior e o menor peso
    lidos. '''

# Inicializa as variáveis para armazenar o maior e o menor peso
maiorPeso = 0
menorPeso = 0

# Loop para solicitar o peso 5 vezes
for p in range(1, 6):
    # Solicita ao usuário que insira o peso
    peso = int(input('Digite o peso: '))
    
    # Se for a primeira iteração, inicializa maiorPeso e menorPeso
    if p == 1:
        maiorPeso = peso  # Define o primeiro peso como o maior
        menorPeso = peso  # Define o primeiro peso como o menor
    else:
        # Verifica se o peso atual é maior que o maiorPeso registrado
        if peso > maiorPeso:
            maiorPeso = peso  # Atualiza maiorPeso se o peso atual for maior
        # Verifica se o peso atual é menor que o menorPeso registrado
        elif peso < menorPeso:
            menorPeso = peso  # Atualiza menorPeso se o peso atual for menor

# Exibe o maior e o menor peso lido
print(f'O maior peso lido foi de {maiorPeso}')
print(f'O menor peso foi de {menorPeso}')