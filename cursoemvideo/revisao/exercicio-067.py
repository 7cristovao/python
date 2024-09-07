''' Faça um programa que mostre a tabuada 
    de vários números, um de cada vez, 
    para cada valor digitado pelo usuário.
    O programa será interrompido quando o
    número solicitado for negativo. '''

fator2 = 0
while True:
    fator1 = int(input('Digite qual tabuada você quer: '))
    if fator1 < 0:
        break
    else:
        for fator2 in range (1, 11):
            print(f'{fator1} x {fator2} = {fator1 * fator2}')
print('Fim do programa')