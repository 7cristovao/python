''' Escreva um programa 
    que leia um valor 
    em metros e o exiba
    convertido em 
    centímetros e milímetros. '''

num = float(input('Digite um valor em metros: '))
print(f'Este valor em centímetros é de {num * 100:.2f}')
print(f'Este valor em milímetros é de {num * 1000:.2f}')
