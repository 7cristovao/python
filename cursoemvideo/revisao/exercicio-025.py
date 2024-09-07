''' Crie um programa
    que leia o nome de 
    uma pessoa e diga se
    ela tem "SILVA" no nome. '''

nome = str(input('Digite o nome: '))
nome = nome.lower()
existePalavra = nome.find('silva')
print(existePalavra)
if existePalavra != -1:
    print('Este nome possui a palavra "SILVA"')
else:
    print('Este nome NÃO possui a palavra "SILVA"')