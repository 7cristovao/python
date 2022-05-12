#!/usr/bin/env python3


# Crie um prg onde o usuario possa digitar cinco VALORES
# NUMERICOS  e cadastre-os em uma LISTA, JA NA 
# POSICAO CORRETA  de insercao (sem usar o SORT).

# No final mostre a LISTA ORDENADA na tela

x = list() 
for c in range(0, 5):
    x.append(int(input('Dig. o valor: ')))
if x[0] > x[1] > x[2] > x[3] > x[4]:
                                    print(x[0], x[1], x[2], x[3], x[4])
elif x[0] > x[1] > x[2] > x[4] > x[3]:
                                    print(x[0], x[1], x[2], x[4], x[3])
elif x[0] > x[1] > x[4] > x[2] > x[3]:
                                    print(x[0], x[1], x[4], x[2], x[3])
elif x[0] > x[4] > x[1] > x[2] > x[3]:    
                                    print(x[0], x[4], x[1], x[2], x[3]) 
elif x[4] > x[0] > x[1] > x[2] > x[3]:
                                    print(x[4], x[0], x[1], x[2], x[3])
elif x[1] > x[0] > x[2] > x[3] > x[4]:
                                    print(x[1], x[0], x[2], x[3], x[4])
elif x[0] > x[2] > x[3] > x[4] > x[1]:
                                    print(x[0], x[2], x[3], x[4], x[1])
elif x[0] > x[2] > x[3] > x[1] > x[4]:
                                    print(x[0], x[2], x[3], x[1], x[4])
elif x[0] > x[2] > x[1] > x[3] > x[4]:
                                    print(x[0], x[2], x[1], x[3], x[4])
#lif x[0] > x[1] > x[2] > x[3] > x[4]:
#                                    print(x[0], x[1], x[2], x[3], x[4])
elif x[1] > x[2] > x[3] > x[4] > x[0]:
                                    print(x[1], x[2], x[3], x[4], x[0])
elif x[1] > x[2] > x[3] > x[0] > x[4]:
                                    print(x[1], x[2], x[3], x[0], x[4])
elif x[1] > x[2] > x[0] > x[3] > x[4]:
                                    print(x[1], x[2], x[0], x[3], x[4])
elif x[2] > x[0] > x[1] > x[3] > x[4]:
                                    print(x[2], x[0], x[1], x[3], x[4])
elif x[0] > x[1] > x[3] > x[4] > x[2]:
                                    print(x[0], x[1], x[3], x[4], x[2])
elif x[0] > x[1] > x[3] > x[2] > x[4]:
                                    print(x[0], x[1], x[3], x[2], x[4])
elif x[0] > x[2] > x[3] > x[1] > x[4]:
                                    print(x[0], x[2], x[3], x[1], x[4])
elif x[3] > x[0] > x[1] > x[2] > x[4]:
                                    print(x[3], x[0], x[1], x[2], x[4])
elif x[0] > x[3] > x[1] > x[2] > x[4]:
                                    print(x[0], x[3], x[1], x[2], x[4])
elif x[0] > x[1] > x[4] > x[3] > x[2]:
                                    print(x[0], x[1], x[4], x[3], x[2])
elif x[1] > x[0] > x[3] > x[4] > x[2]:
                                    print(x[1], x[0], x[3], x[4], x[2])
elif x[1] > x[0] > x[3] > x[2] > x[4]:
                                    print(x[1], x[0], x[3], x[2], x[4])
elif x[1] > x[0] > x[2] > x[4] > x[3]:
                                    print(x[1], x[0], x[2], x[4], x[3])


else:
        print('fim') 
     

 
