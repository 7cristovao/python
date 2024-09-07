''' Faça um programa que 
    leia a largura e a
    altura de uma parede 
    em metros, calcule a
    sua área e a quantidade
    de tinta necessária para
    pintá-la, sabendo que 
    cada litro de tinta, 
    pinta uma área de 2m² '''

larguraDaParede = float(input('Digite a largura de uma parede em metros: '))
alturaDaParede = float(input('Digite a altura de uma parede em metros: '))
areaDaParede = larguraDaParede * alturaDaParede
print('Cada litro de tinta pinta uma área de 2m²')
quantidadeDeTintaNecessaria = areaDaParede / 2
print(f'A area da parede é de {areaDaParede}')
print(f'A quantidade necessária de tinta é de {quantidadeDeTintaNecessaria:.1f} litros')
