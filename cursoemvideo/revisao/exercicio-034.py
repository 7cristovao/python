''' Escreva um programa
    que pergunta o salário
    de um funcionário e 
    calcule o valor do seu
    aumento.
    Para salários superiores
    a R$ 1.250,00, calcule
    um aumento de 10%.
    Para os inferiores ou 
    iguais, o aumento é de
    15%. '''

salario = float(input('Digite o salário: '))
if salario > 1250:
    print(f'O valor do salário reajustado é {salario * 1.10:.2f}')
else:
    print(f'O valor do salário reajustado é {salario * 1.15:.2f}')