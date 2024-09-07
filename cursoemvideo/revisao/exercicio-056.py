''' Desenvolva um programa que leia o
    nome, idade e sexo de 4 pessoas.
    No final do programa, mostre:
    
    - A média de idade do grupo.
    - Qual é o nome do homem mais velho.
    - Quantas mulheres tem menos de
    20 anos.'''

somaDasIdades = 0
homemMaisVelho = None
idadeHomemMaisVelho = -1
mulheresComMenosDeVinteAnos = 0

for c in range(1, 5):
    nome = str(input('Digite o nome: '))
    idade = float(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: (M/F): ')).strip().upper()
    somaDasIdades = somaDasIdades + idade
    
    # Verifica se a pessoa é um homem e se a idade é maior que a do homem mais velho encontrado até agora
    if sexo == 'M' and idade > idadeHomemMaisVelho:
        homemMaisVelho = nome
        idadeHomemMaisVelho = idade
    if sexo == 'F' and idade < 20:
        mulheresComMenosDeVinteAnos = mulheresComMenosDeVinteAnos + 1
mediaDasIdades = somaDasIdades / 4
print(f'A média das idades é de {mediaDasIdades:.2f}')
if homemMaisVelho:
    print(f'O homem mais velho é {homemMaisVelho}')
else:
    print(f'Não foram informados homens')
print(f'Há {mulheresComMenosDeVinteAnos} mulher(es) com menos de 20 anos')