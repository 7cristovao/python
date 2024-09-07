# EXEMPLOS DE PROGRAMAS USANDO WHILE

# contador de 1 até 9
c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')

num = 1
# quando digitar o valor zero ele pára (chamado de FLAG)
while num != 0:
    num = int(input('Digite um valor: '))
print('Fim')

# programa pergunta se quer continuar ou não
resposta = 'S'
while resposta == 'S': 
    num = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? (S/N)')).upper()
print('Fim')

num = 1
par = impar = 0
while num != 0:
    num = int(input('Digite um número: '))
    if num != 0:
        if num % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print(f'Você digitou {par} número(s) par(es) e {impar} número(s) ímpar(es)')