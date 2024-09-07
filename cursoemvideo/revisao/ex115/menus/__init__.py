def inserirLinha():
    print('-' * 40)

def menuPrincipal():
    inserirLinha()
    print('             MENU PRINCIPAL             ')
    inserirLinha()
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova Pessoa')
    print('3 - Sair do Sistema')
    inserirLinha()

def menuPessoasCadastradas():
    inserirLinha()
    print('           PESSOAS CADASTRADAS          ')
    inserirLinha()
    lerCadastro()

# Função Novo Cadastro
def menuNovoCadastro():
    inserirLinha()
    print('             NOVO CADASTRO              ')
    nome = str(input('Nome: '))
    while True:
        try:
            idade = int(input('Idade: '))
            gravarDados(nome, idade)
            print(f'Novo registro de {nome} adicionado.')
            break
        except ValueError:
            print('Digite um número inteiro: ')
        
# Função para gravar dados em um arquivo
def gravarDados(nome, idade):
    with open('dados.txt', 'a') as arquivo: # Abre o arquivo em modo de adição
        arquivo.write(f'{nome};{idade}\n') # Escreve os dados no arquivo

def lerCadastro():
    try:
        with open('dados.txt', 'r') as arquivo: # Abre o arquivo em modo de leitura
            conteudo = arquivo.readlines() # Lê todas as linhas do arquivo
            if conteudo: # Verifica se o arquivo não está vazio
                for linha in conteudo: # Itera sobre cada linha
                    print(f'{linha.strip()} anos') # Exibe a linha sem espaços em branco
            else:
                print('O arquivo está vazio.')
    except FileNotFoundError:
        print("O arquivo 'dados.txt' não foi encontrado.")

