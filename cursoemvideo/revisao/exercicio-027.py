''' Faça um programa que leia 
    o nome completo de uma pessoa
    mostrando em seguida o 
    primeiro e o último nome
    separadamente.

    Ex: Ana Maria de Souza
    primeiro = Ana
    último = Souza '''

nome = str(input('Digite uma frase: '))
nomeDividido = nome.split()
primeiroNome = nomeDividido[0]
ultimoNome = nomeDividido[-1]

print(f'primeiro = {primeiroNome}')
print(f'último = {ultimoNome}')