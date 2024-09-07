''' Faça um programa que tenha uma função 
    chamada área(), que receba as dimensões
    de um terreno retangular (largura e 
    comprimento) e mostre a área do terreno. '''

def area(largura, comprimento):
    print('Controle de terrenos')
    print('--------------------')
    largura = float(input('LARGURA (m): '))
    comprimento = float(input('COMPRIMENTO (m): '))
    areaDoTerreno = largura * comprimento
    print(f'A área de um terreno {largura:.1f}x{comprimento:.1f} é de {areaDoTerreno:.1f}m²')

area(2, 5)