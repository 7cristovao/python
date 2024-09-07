''' Reescreva a função leiaInt() que fizemos no
    desafio 104, incluindo agora a possibilidade
    da digitação de um número de tipo inválido.
    Aproveite e crie também uma função 
    leiaFloat() com a mesma funcionalidade. '''

def leiaInt(msg):
    try: 
        ok = False
        valor = 0
        while True:
            numInt = str(input(msg))
            if numInt.isnumeric():
                valor = int(numInt)
                ok = True
            else:
                print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            if ok:
                break
        return valor
    except KeyboardInterrupt:
        print('\n\033[0;31mUsuário preferiu não digitar esse número.\033[m')
        return 0
    else:
        return numInt


def leiaFloat(msg):
    try:
        ok = False
        valor = 0
        while True:
            numFloat = str(input(msg))
            numFloatTratado = numFloat.replace('.','')
            if numFloatTratado.isnumeric():
                valor = float(numFloat)
                ok = True
            else:
                print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            if ok:
                break
        return valor
    except KeyboardInterrupt:
        print('\n\033[0;31mUsuário preferiu não digitar esse número.\033[m')
        return 0
    else:
        return numFloat

numInt = leiaInt('Digite um número inteiro: ')
numFloat = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {numInt} e o real foi {numFloat}')