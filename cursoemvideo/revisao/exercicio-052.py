''' Faça um programa que leia um número 
    inteiro e diga se ele é ou não um
    número primo. '''

print('VERIFICADOR DE NÚMEROS PRIMOS\n')
num = int(input("Digite um número inteiro: "))
if num > 1:
    eh_primo = True  # Assume que o número é primo
    for c in range(2, int(num ** 0.5) + 1):
        if num % c == 0:
            eh_primo = False  # Se encontrar um divisor, não é primo
    if eh_primo:
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")
else:
    print(f"{num} não é um número primo.")