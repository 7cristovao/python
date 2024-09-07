# Função para gravar dados em um arquivo
def gravar_dados(nome, idade):
    with open('dados.txt', 'a') as arquivo:  # Abre o arquivo em modo de adição
        arquivo.write(f'Nome: {nome}, Idade: {idade}\n')  # Escreve os dados no arquivo

# Função principal
def main():
    while True:
        nome = input("Digite seu nome (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break  # Encerra o loop se o usuário digitar 'sair'
        
        idade = input("Digite sua idade: ")
        
        # Chama a função para gravar os dados
        gravar_dados(nome, idade)
        print("Dados gravados com sucesso!")

# Executa a função principal
if __name__ == "__main__":
    main()