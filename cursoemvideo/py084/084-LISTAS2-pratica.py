#!/usr/bin/env python3


#   AQUI FICOU LIGA«√O APENAS
teste = list()
teste.append('Gustavo')
teste.append(48)
galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)


# PRECISA FAZER UMA CÛPIA
teste = list()
teste.append('Gustavo')
teste.append(48)
galera = list()
galera.append(teste[:])   # <<<<<<<<<<<<<,
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])  #  <<<<<<<<<<<<<
print(galera)


# Lista principal e depois listas internas
galera = [[],[],[],[]]

# Exemplo Lista principal e depois listas internas
galera = [['Jo„o',19], ['Ana',33], ['Joaquim',13], ['Maria',45]]
print(galera) # exibe todo mundo
print(galera[0])  # exibe os dados do joao
print(galera[0][0])  #  exibe sÛ Jo„o
print(galera[2][1])   #  idade do joao   exibe 13


# usando FOR
galera = [['Jo„o',19], ['Ana',33], ['Joaquim',13], ['Maria',45]]
for p in galera:    #  p : pessoa
    print(p)   
    #  exibe ['Jo„o',19] 
    #           ['Ana',33] 
    #           ['Joaquim',13]
    #           ['Maria',45]

#
galera = [['Jo„o',19], ['Ana',33], ['Joaquim',13], ['Maria',45]]
for p in galera:
    print(p[0])   # exibe os nomes


#
galera = [['Jo„o',19], ['Ana',33], ['Joaquim',13], ['Maria',45]]
for p in galera:
    print(p[1])   # exibe as idades
    
#
galera = [['Jo„o',19], ['Ana',33], ['Joaquim',13], ['Maria',45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')   # exibe os nomes e idades
    
# mais um exemplo
galera = list()
dado = list()
for c in range[0, 3]:
	dado.append(str(input('Nome: ')))
	dado.append(int(input('Idade: ')))
	galera.append(dado[:])    # <<<<<<<<<  N√O esquecer
	dado.clear()

print(galera)


    
# outro exemplo
galera = list()     
dado = list()      # criei duas estruturas de dados para depois criar a auxiliar
totmai = totmen = 0   #  vou ver o total de maior e menor de idade
for c in range[0, 3]:        # serve para ler os dados e jogar dentro da galera
	dado.append(str(input('Nome: ')))
	dado.append(int(input('Idade: ')))
	galera.append(dado[:])    # <<<<<<<<<  N√O esquecer
	dado.clear()

for p in galera:
	if p[1] >=21:
		print(f'{p[0]} È maior de idade.')
		totmai += 1
	else:
		print(f'{p[0]} È menor de idade.')
		totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')





