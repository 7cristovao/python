#!/usr/bin/env python3


#  (1) módulo colorize 
#  (2) padrão ANSI escape sequence para cores

\033[ m
#    |
#    V
#
\033[          m
#         |
#         V
#
#     STYLE       BACK
\033[       :    :       
#            TEXT
#
\033[   0   : 33 : 44m
#
\033[0:33:44m

# STYLE
# 0 None (Nenhum)
# 1 Bold (Negrito)
# 2 Faint
# 3 Italic (Itálico)
# 4 Underline (Sublinhado)
# 5 Blink (Pisca)
# 7 Negative (Negativo)
# 9 Crossed (Tachado)
# 
# TEXT
# 30 branco 
# 31 vermelho 
# 32 verde
# 33 amarelo
# 34 azul
# 35 magenta
# 36 ciano
# 37 cinza
# 
# BACK
# 40 branco fundo
# 41 vermelho fundo
# 42 verde fundo
# 43 amarelo fundo
# 44 azul fundo
# 45 magenta fundo
# 46 ciano fundo
# 47 cinza fundo

'''
 BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"'''



