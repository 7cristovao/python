''' Faça um programa que calcule a soma
    entre todos os números ímpares que 
    são múltiplos de três e que se
    encontram no intervalo de 1 até 500. '''

# Inicializa o contador
s = 0

# Se múltiplo de 3
for c in range(0, 500):
    if c % 3 == 0:
        s = s + c
        #print(c)
print(s)
print('FIM!')

# Calcula a soma entre todos
    

