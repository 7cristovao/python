'''Crie um código em Python que teste se o site
   Pudim está acessível pelo computador usado. '''

# Com o pudim não funcionou, mas com o google.com.br funcionou

import urllib
import urllib.request

try:
    site=urllib.request.urlopen('https://www.sapo.pt/')
except urllib.request.URLError:
    print('O Sapo não está acessível no momento')
else:
    print('Consegui abrir o Sapo com sucesso!')

######### Actulizado###########################
import urllib
import urllib.request
site=str(input('Insira o site: '))
try:
    site1=urllib.request.urlopen('https://www.'+site+'/')
except urllib.request.URLError:
    print('O Site não está acessível no momento')
else:
    print('Consegui abrir o site com sucesso!')