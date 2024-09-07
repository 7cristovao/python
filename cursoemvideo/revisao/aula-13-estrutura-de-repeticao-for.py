# conta de 0 a 5 progressivamente
for c in range(0,6):
    print(c)
print('FIM!')

# conta de 5 a 0 regressivamente
for c in range(6, 0, -1):
    print(c)
print('FIM!')

# conta de 0 a 6 pulando de 2 em 2
for c in range(0, 7, 2):
    print(c)
print('FIM!')   

# conta de 0 até o enésimo número inserido
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM!')

# imprime de acordo com início, fim e passo
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM!')    

# para executar repetidamente 10 vezes um comando
for c in range(0, 10):
    n = int(input('Digite um valor'))
print('FIM!')

# somatorio
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor'))
    s += n # também se escreve s = s + n
print(f'O somatório de todos os valores foi {s}')