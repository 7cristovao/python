#!/usr/bin/env python3


#                  11111111112
#        012345678901234567890
frase = 'Curso em Vídeo Python'

print(frase)
print(frase[9])            # V
print(frase[9:13])         # Víde
print(frase[9:21])         # Vídeo Python
print(frase[9:21:2])       # VdoPto
print(frase[2:5])          # rso
print(frase[:5])           # Curso
print(frase[15:])          # Python
print(frase[9::3])         # VePh
#-------------------------------------------
print(frase.upper().count('o'))
print(frase.lower().count('o'))