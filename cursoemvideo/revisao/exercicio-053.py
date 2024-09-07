''' Crie um programa que leia uma frase 
    qualquer e diga se ela é um palindromo,
    desconsiderando os espaços. 
    
    Ex: 
    APOS A SOPA 
    A SACADA DA CASA
    A TORRE DA DERROTA
    O LOBO AMA O BOLO
    ANOTARAM A DATA DA MARATONA '''

# pede para o usuário digitar uma frase e a armazena em uma variável
# método remove os espaços extras digitados à esquerda e à direita
frase = str(input('Digite uma frase: ')).split().upper()

# método separa a frase em palavras e a atribui a outra variável
fraseSeparada = frase.split()

# modifica o separador 'espaço' pelo separador '' (vazio)
fraseSemEspacos = ''.join(fraseSeparada)

# atribui a variável inverso uma string vazia
inverso = ''

# varre da última até a primeira letra
# INÍCIO: a última letra é conseguida através de len(fraseSemEspaços) - 1
# FIM: vai até a primeira letra
# PASSO: anda um passo negativo
for letra in range(len(fraseSemEspacos) -1, -1, -1):
    # inverte a frase
    inverso += fraseSemEspacos[letra]
# verifica se é ou não um palíndromo e exibe na tela
if fraseSemEspacos == inverso:
    print('E um palíndromo.')
else:
    print('Não é um palíndromo.')