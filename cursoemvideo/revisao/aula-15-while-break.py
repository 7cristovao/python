# contador básico usando o while
cont = 0
while cont <= 10:
    print(cont)
    cont = cont + 1
print('Fim')

# contador utilizando flags
num = 0
cont = 0
while num != 999:
    num = int(input('Digite um número: '))
    cont = cont + 1
print('Fim')

# somatorio utilizando flags
num = soma = 0
while num != 999:
    num = int(input('Digite um número: '))
    soma = soma + num
soma = soma - 999
print(f'A soma vale {soma}')

# somatorio utilizando while true
num = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma = soma + num
print(f'A soma vale {soma}')