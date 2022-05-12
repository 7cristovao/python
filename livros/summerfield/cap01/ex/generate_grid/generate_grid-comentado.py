#! usr/bin/env python3


# --------------IMPORTACAO-------------------------


import random  # importa biblioteca random em usr/lib/python3.7/random.py


# --------DEFINICAO DE FUNCAO GET_INT()---------


def get_int(msg, minimum, default):  # (1) (2) (3)
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            i = int(line)
            if i < minimum:
                print("must be >=", minimum)
            else:
                return i
        except ValueError as err:
            print(err)

# (1) string de mensagem
# (2) valor minimo
# (3) valor padrao
# (3.1) se DEFAULT eh NONE,
#       isto eh, nenhum valor padrao ali foi dado
#       o fluxo do controlador ira cair atraves da linha int()
#       conversao ira falhar(ja que "nao pode ser convertida em um inteiro")
#       e uma excecao ValueError sera lancada.
# (3.2) mas se DEFAULT nao for NONE, entao sera retornado
#       a funcao ira empreender a conversao do texto que o usuario entrou
#       em um inteiro, se a conversao eh bem sucedida, ela ira,
#       entao, checar se o inteiro possui um valor pelo menos igual ao minimo
#
#  -----------INTERACAO DO USUARIO------------------


rows = get_int("rows: ", 1, None)  #  O usuario tera que entrar c/ um inteiro
columns = get_int("columns: ", 1, None)  #  O usuario tera q entrar c/ int
minimum = get_int("minimum (or Enter for 0): ", -1000000, 0)  #  MIN vpad = 0

default = 1000  #  para MAX valor padrao de 1000
if default < minimum:  #  se isto
    default = 2 * minimum #  entao isto
maximum = get_int("maximum (or Enter for " + str(default) + "): ",
                 minimum, default)


# ---------PROCESSO POR SI MESMO-------------------


row = 0
while row < rows:  #  WHILE EXTERNO trabalha por linhas
    line = ""  #  acumula nº em cada linha e imprime a linha apos cada nº
    column = 0  #  nº de colunas ... (4)
    while column < columns:  #  WHILE CENTRAL funciona por colunas
        i = random.randint(minimum, maximum)  #  obt nº aleatorio nesta faixa
        s = str(i)  #  converter em uma string
        while len(s) < 10:  #  WHILE INTERIOR funciona por caracteres
            s = " " + s
        line += s
        column += 1  #  (4) ... ter sido adicionado
    print(line)
    row += 1
