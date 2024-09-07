# Ajuda interativa dentro do IDLE
help()

# Exibe a ajuda interativa do código input
help(input)

# Exibe também a ajuda interativa do código input
print(input,__doc__)


# String de documentação
def contador(i, f, p):
    """
    → Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    função criada por Gustavo Guanabara do canal Curso em Vídeo
    """
    c = i
    while c<= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')


contador(0, 100, 10)

help(contador)


# conceito de parametros opcionais
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar()
somar(c=5, b=4)

# ESCOPO DE VARIÁVEIS
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

# Programa principal
n = 2
print(f'No programa principal, n vale{n}')
teste()
# print(x) dá erro aqui por causa do escopo

# outro exemplo de escopo global e local
# escopo local
def teste(b):
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


# escopo global
a = 5
teste(a)
print(f'A fora vale {a}')

# se há uma variável declarada localmente e globalmente o python prioriza a global
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
print(f'N1 fora vale {n1}')
funcao()

# uso da palavra chave GLOBAL
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'A dentro vale {b}')
    print(f'C dentro vale {c}')


# escopo global
a = 5
teste(a)
print(f'A fora vale {a}')

# RETORNO DE VALORES
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')

# Exemplo de função fatorial manualmente
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

# Exemplo de função PAR ou ÍMPAR
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('É ímpar!')