# erro sintático
primt(x)

# erro de significado, erro semântico
# x não existe
# exceção NameError
print(x)

# exceção ValueError 
# quando não se digita um número inteiro
n = int(input("Número: "))
print(f'Você digitou o número {n}')

# exceção ZeroDivisionError
# quando b = 0
a = int(input('Numerador: '))
b = int(input('Denominador: '))
r = a / b
print(f'O resultado é {r}')

# exceção TypeError
r = 2 / '2'

# exceção indexError
# pois esse índice 3 não existe
lst = [3, 6, 4]
print(lst[3])

# exceção ModuleNotFoundError
import moduloInexistente

'''
Lista de tipos de exceções:

NameError
ValueError
ZeroDivisionError
TypeError
IndexError
KeyError
EOFError
KeyboardInterrupt
OSError
MemoryError
ConnectionError
RuntimeError
'''

'''
Lista completa: Python Exception List
'''

# Código para tratamento de erros
try: # tentar
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except: # se der problema
    print('Infelizmente tivemos um problema :(')

print(f'O resultado é {r}')

# Usando a clausula ELSE (opcional)
try: 
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except: 
    print('Infelizmente tivemos um problema :(')
else:
    print(f'O resultado é {r}')

# Usando a clausula FINALLY (opcional)
# Você desenvolvedor pode capturar o erro
try: 
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro: 
    print(f'Problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito obrigado!')

# Um mesmo TRY pode ter vários EXCEPT
try: 
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito obrigado!')
