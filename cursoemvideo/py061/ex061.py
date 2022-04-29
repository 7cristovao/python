# Refaça o exercício 51, lendo o PRIMEIRO TERMO
# e a razao de uma PROGRESSAO ARITIMÉTICA
# mostrando os 10 PRIMEIROS TERMOS da 
# progressão usando a estrutura WHILE



a_0 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont = -1  # i
while cont < 11:        
     cont += 1
     print ('O {}º termo da PA é igual a {} '.format(cont, a_0 + (r * (cont))))
print('fim\n')
