''' Crie um programa
    que leia o nome de
    uma cidade e diga 
    se ela começa ou não
    com o nome "SANTO". '''

cidade = str(input('Digite o nome de uma cidade: '))
cidade = cidade.lower()
existeCidade = cidade.find('santo')

if existeCidade == 0:
    print("O nome desta cidade começa com SANTO")
else:
    print("O nome desta cidade NÃO começa com SANTO")
