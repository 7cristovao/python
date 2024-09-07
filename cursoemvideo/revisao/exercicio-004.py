# Faça um programa que leia algo pelo teclado 
# e mostre na tela o seu tipo primitivo 
# e todas as informações possíveis sobre ele

# OBS: input sempre retorna uma STRING mesmo digitando NUMERO

entradaPeloTeclado = input('Primeiro teste: digite algo pelo teclado e aperte ENTER: ')
print(f'O tipo primitivo deste valor é {type(entradaPeloTeclado)}')

"""
#Para ver o tipo primitivo da variável:
x=10
y=10.0
z='a'
b=True
print(type(x), type(y), type(z), type(b))

"""
a = input('Segundo teste: digite algo: ')

print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético: ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())
