# Definindo uma função com parâmetros
def soma(a, b):
    s = a + b
    print(f'{soma}')


soma(10, 10)

# mudando e explicitando a ordem dos parâmetros
def somar(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

# Programa principal
# Passando 4 pro 'b' e 5 pro 'a'
somar(b=4, a=5)
somar(7, 2)

# Se passar mais parâmetros que o necessário o programa dá erro

# Desempacotar parâmetros
# Vou receber parâmetros. Quantos? Não sei.
# Python cria uma tupla com a quantidade de parâmetros indefinidos
def contador(* num):
    print(num)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# Exibir valor por valor em uma linha
def contador1(* num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')

contador1(2, 1, 7)
contador1(8, 0)
contador1(4, 4, 7, 6, 2)

# Exibir valor por valor e usar o CONTADOR
def contador2(* num):
    tamanho = len(num)
    print(f'Recebi os valores {num} e são ao todo {tamanho} números')

contador2(2, 1, 7)
contador2(8, 0)
contador2(4, 4, 7, 6, 2)

# usando listas em funções
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

# Para o Python toda passagem de parâmetro é por referência
# Tudo que eu fizer na minha lista vai interferir em valores
# diferente de C e Java que a passagem de parâmetro é por valor


# Outro exemplo de desempacotamento
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)