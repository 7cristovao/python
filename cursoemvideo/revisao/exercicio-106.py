''' Faça um mini-sistema que utilize o interactive Help 
    do Python. O usuário vai digitar o comando e o 
    manual vai aparecer.
    Quando o usuário digitar a palavra 'FIM', o
    programa se encerrará. 
    
    OBS: use cores. '''

c = ('\033[m',         # 0 : sem cor
     '\033[0;30;41m',  # 1 : vermelho
     '\033[0;30;42m',  # 2 : verde
     '\033[0;30;43m',  # 3 : amarelo
     '\033[0;30;44m',  # 4 : azul
     '\033[0;30;45m',  # 5 : roxo
     '\033[7;30m'      # 6 : branco
    )

def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}', 4)
    print(c[6], end='')
    help(comando)
    print(c[0], end='')

def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(f'   {msg}')
    print('~' * tamanho)
    print(c[0], end='')

# Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper().strip() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)