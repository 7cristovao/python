#! usr/bin/env python3
# 
# # NUMEROS DE PONTO-FLUTUANTE

# Todos os operadores e funções numéricas podem ser usados com 'floats'
# incluindo as versões de atribuição incremental. O tipo de dados 'floats'
# pode ser chamado como uma função - sem nenhum argumento, retorna 0.0;
# com um argumento 'float', retorna a cópia do argumento e, com qualquer
# outro argumento, tenta converter o objeto dado em um 'float'.

# Quando usadas conversões, um argumento string pode ser passado,
# usando notação decimal simples ou notação exponencial.

# É possível que NaN ("not a number") ou "infinito" possa ser produzido
# por um cálculo envolvendo 'floats' - infelizmente, o comportamento não
# é consistente o bastante através das implementações e pode diferir,
# dependendo da biblioteca matemática do sistema.

# Aqui está uma função simples para comparar 'floats' por igualdade, o
# limite da precisão do computador:

def equal_float(a,b):
    return abs(a - b) <= ( sys.float_info.epsilon(min(abs(a), abs(b)))

#  Isto exige que importemos o módulo 'sys'.
#  O objeto 'sys.float_info' possui muitos atributos; 'sys.float_info.epsilon'
#  é efetivamente a menor das diferenças que o computador pode distinguir 
#  entre dois números de ponto-flutuante. Em um dos computadores do autor
#  32-bits é mais de 0.000 000 000 000 0002. (Épsilon é o nome tradicional para
#  este número.) O 'float' do Python, normalmente, fornece precisão confiável
#  para mais de 17 dígitos significativos.

# Se você digitar 'sys.float_info' no IDLE, todos esses atributos serão 
# mostrados, incluindo os mínimos e máximos dos números de ponto-flutuante que
# o computador pode representar. E, digitando 'help(sys.float_info)' será 
# impressa alguma informação sobre o objeto 'sys.float_info'.

# Números de ponto-flutuante podem ser convertidos em inteiros usando a 
#  funcao int(), que retorna a parti inteira e joga fora a parte fracionada,
#  ou round(), que considera a parte fracionada, ou usando math.floor() ou
# math.ceil() que convertem abaixo ou acima para o inteiro mais próximo
# 
# O metodo float.is_integer() retorna True se a parte fracional do número
#  de ponto-flutuante é 0, e uma  representação fracional do float pode ser
# obtida usando i método float.as_integer_ratio. Por exemplo, dado
# x = 2.75, a chamada x.as_integer_ratio() retorna (11, 4).
# Inteiros podem ser convertidos em número de pontos flutuantes usando float()

# Números de ponto flutuante podem também ser representados como strings
# em formato hexadecimal usando o método float.hex(). 
# A conversão oposta pode ser realizada utilizando float.fromhex()*. Por exemplo:
# s = 14.25.hex()       # str s == '0x1.c800000000000p+3' 
# f = float.fromhex(s)  # float f == 14.25
# t = f.hex             # str t == '0x1.c800000000000p+3' 
# 
# O expoente é indicado usando o 'p' ('potencia') ao invés de 'e', uma vez 
# que seja um dígito hexadecimal válido.
# 
# Em adição à funcionalidade embutida de ponto flutuante, o módulo math 
# fornece muitas outras funções que operam em floats, como mostram as tabelas
# No próximo arquivo(IDLE) estão mais alguns códigos fragmentados que mostram  
# como fazer pra usar as funcionalidades do módulo: 
# 
# vide IDLE
# 
# A função math.hypot() calcula a distancia da origem aoponto (x,y) e produz o  
# mesmo resultado como em      math.sqtr(x**2) + (y**2)
# 
# O módulo math é muito dependente da biblioteca de matemática base em que
# Python é compilado. Isso significa que algumas condicoes de erro e alguns 
# casos de limites poderao comportarse variadamanete em diferentes 
# plataformas
