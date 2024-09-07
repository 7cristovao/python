''' Faça um programa que leia
    uma frase pelo teclado e 
    mostre: 
    
    - Quantas vezes aparece a letra "A".
    - Em que posição ela aparece a primeira vez.
    - Em que posição ela aparece a última vez. '''

frase = str(input('Digite uma frase: '))
frase = frase.lower()
quantasVezesApareceALetraA = frase.count('a')
emQuePosicaoElaApareceAPrimeiraVez = frase.find('a')
emQuePosicaoElaApareceAUltimaVez = frase.rfind('a')
print(f'A letra A aparece {quantasVezesApareceALetraA} vez(es).')
print(f'A letra A apareceu na primeira vez na posição {emQuePosicaoElaApareceAPrimeiraVez}.')
print(f'A letra A apareceu na última vez na posição {emQuePosicaoElaApareceAUltimaVez}')