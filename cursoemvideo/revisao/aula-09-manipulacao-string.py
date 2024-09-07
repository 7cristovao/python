frase = 'Curso em Vídeo Python'

# Fatiamento

print(frase[9])              # exibe caractere 9
print(frase[9:14])           # exibe caractere 9 inicial, caractere 21 final
print(frase[9:21])           # exibe caractere 9 inicial, caractere 21 final
print(frase[9:21:2])         # exibe caracteres do 9 ao 21 pulando de dois em dois
print(frase[15:])            # exibe caractere 15 até o caractere final 
print(frase[9::3])           # exibe caractere 9 até o caractere final pulando de três em três
print(len(frase))            # exibe o comprimento da string
print(frase.count('o'))      # conta quantas vezes aparece a letra 'o'
print(frase.count('o',0,13)) # conta quantas vezes aparece a letra 'o' entre os caracteres 0 e 13
print(frase.find('deo'))     # exibe em qual caractere se encontra a string 'deo'
print(frase.find('Android')) # exibe -1 indicando que essa string não foi encontrada
print('Curso' in frase)      # verifica se existe a string 'Curso' na variável e imprime verdadeiro

# Extra

print(frase.rfind('o'))      # exibe em qual caractere se encontra 'o' da direita para a esquerda

# Transformação

print(frase.replace('Python','Android')) # substitui a primeira string pela segunda string
print(frase.upper())                     # deixa string em maiúsculas
print(frase.lower())                     # deixa string em minúsculas
print(frase.capitalize())                # a primeira letra da string em maiúscula
print(frase.title())                     # deixa a primeira letra de cada palavra em maiúscula

frase = '   Aprenda Python  '

print(frase.strip())                     # remove os espaços em branco à esquerda e à direita
print(frase.rstrip())                    # remove os espaços em branco à direita
print(frase.lstrip())                    # remove os espaços em branco à esquerda

# Divisão

frase = 'Curso em Vídeo Python'

print(frase.split())                    # aloca cada palavra em um índice de uma lista
                                        # separa frase em palavras

# Junção

frase2 = frase.split()
print('-'.join(frase2))                  # modifica o separador 'espaço' pelo separador '-'