''' Desenvolva uma lógica que
    leia o peso e altura de
    uma pessoa, calcule seu
    IMC e mostre seu status,
    de acordo com a tabela
    abaixo:

    - Abaixo de 18.5: Abaixo do Peso
    - Entre 18.5 e 25: Peso ideal
    - 25 até 30: Sobrepeso
    - 30 até 40: Obesidade
    - Acima de 40: Obesidade mórbida '''

peso = float(input('Digite o peso de uma pessoa em kg: '))
altura = float(input('Digite a altura de uma pessoa em metros: '))
IMC = peso / (altura ** 2)
print(f'IMC = {IMC:.1f}')
if IMC < 18.5:
    print('Abaixo do peso')
elif IMC >= 18.5 and IMC <= 25:
    print('Peso ideal')
elif IMC > 25 and IMC <= 30:
    print('Sobrepeso')
elif IMC > 30 and IMC <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')


