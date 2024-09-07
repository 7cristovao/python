''' Refaça o exercício 35 dos 
    triângulos, acrescentando 
    o recurso de mostrar que
    tipo de triângulo será formado:

    - Equilátero: todos os lados iguais
    - Isóceles: dois lados iguais
    - Escaleno: todos os lados diferentes '''

a = float(input('Digite a medida de uma reta: '))
b = float(input('Digite outra medida de reta: '))
c = float(input('Digite mais uma medida: '))
if a + b > c and a + c > b and b + c > a:
    print('As retas podem formar este triângulo.')
    if a == b == c:
        print('Ele é equilátero')
    elif a == b or b == c or a == c:
        print('Ele é isóceles')
    else:
        print('Ele é escaleno')
else:
    print('O triângulo não existe porque as retas não podem formar este triângulo.')