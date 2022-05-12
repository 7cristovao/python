#!usr/bin/env python3
#encoding: utf-8

# Crie um programa onde o usuario digite uma EXPRESSAO qualquer
# que use PARENTESES. Seu aplicativo devera analisar se a 
# expressao passada esta com os parenteses abertos e fechados na
# ORDEM CORRETA.
expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
	if simb == '(':
		pilha.append('(')
		#cada ( joga nessa pilha
	elif simb == ')':
		#qdo tem ) remv oq abriu
		if len(pilha) > 0:
		    pilha.pop()
		else:
			pilha.append(')')
			break
if len(pilha) == 0:
	print('A função é válida!')
else:
	print('A função é inválida!')