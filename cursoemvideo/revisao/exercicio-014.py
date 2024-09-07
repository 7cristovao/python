''' Escreva um programa que 
    converta uma temperatura
    digitada em graus Celsius
    para graus Farenheit '''

# c : temperatura em graus Celsius
# f : temperatura em graus Farenheit

c = int(input('Digite a temperatura em graus Celsius: '))
f = (9/5) * c + 32
print(f'Esta temperatura em graus Farenheit corresponde a {f:.0f} °F') 
