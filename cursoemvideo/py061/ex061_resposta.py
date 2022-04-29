# Refaça o exercício 51, lendo o PRIMEIRO TERMO
# e a razao de uma PROGRESSAO ARITIMÉTICA
# mostrando os 10 PRIMEIROS TERMOS da 
# progressão usando a estrutura WHILE

print('Gerador de PA')

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão de PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ¬ '.format(termo), end='')
    termo = termo + razão
    cont += 1
print('fim')
