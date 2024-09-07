''' Crie um pequeno sistema modularizado que 
    permita cadastrar pessoas pelo seu nome
    e idade em um arquivo de texto simples.
    
    O sistema só vai ter 2 opções: cadastrar uma
    nova pessoa e listar todas as pessoas cadastradas. '''

from ex115 import menus

menus.menuPrincipal()
while True:
    try: 
        resposta = int(input('Sua Opção: '))
        if resposta == 1:
            menus.menuPessoasCadastradas()
            menus.menuPrincipal()
        elif resposta == 2:
            menus.menuNovoCadastro()
        elif resposta == 3:
            break
        else:
            print('ERRO! Digite uma opção válida.')
    except ValueError:
        print('Digite um número inteiro: ')
