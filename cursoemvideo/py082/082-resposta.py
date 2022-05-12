num = list()
pares = list()
impares = list()
while True:
	num.append(int(input('Digite um número: ')))
	resp = str(input('Quer continuar? (S/N) '))
	if resp in 'Nn':
		break
	elif resp in 'Ss':
		num.append(int(input('Digite um número: ')))
		resp = str(input('Quer continuar? (S/N) '))
	else:
		while resp not in 'SsNn':
			resp = str(input('Quer continuar? (S/N) '))
print(f'lista completa {num}')
for i, v in enumerate(num):
	if v % 2 == 0:
		pares.append(v)
	elif v % 2 == 1:
		impares.append(v)
print(f'pares {pares}')
print(f'impares {impares}')