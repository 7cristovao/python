#!/usr/bin/env python3


#quero somar todos 
# COM CONTADOR
n = cont = 0  # (1) contador começando com ZERO
while n < 3:  # (2) enquanto contador for menor do que TRÊS...
    n = int(input('Digite um número: '))  # (3) executa isso 
    cont += 1

# fiz ele começar com zero enquanto ele for menor do que três ele faz isso (3)
# se eu quiser ler 5 numeros, coloque n < 5 na linha 7
# se eu não quiser dizer quantos números são, coloque n != 999  (utilizando flag)
# flag é o meu ponto de parada
# se n = 0 ele sequer inicia a contagem porque n é igual ao contador