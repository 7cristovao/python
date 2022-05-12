#!/usr/bin/env python3

import sys

Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]

One = ["   *   ",
       "  **   ",
       " * *   ",
       "   *   ",
       "   *   ",
       "   *   ",
       " ***** "]

Two = ["  ***  ",
       " *   * ",
       "     * ",
       "    *  ",
       "   *   ",
       "  *    ",
       " ******"]

Three = ["  ***  ",
         " *   * ",
         "     * ",
         "   **  ",
         "     * ",
         " *   * ",
         "  ***  "]
Four = ["    *  ",
        "   **  ",
        "  * *  ",
        " *  *  ",
        " ******",
        "    *  ",
        "    *  "]
Five = [" ******",
        " *     ",
        " *     ",
        " ******",
        "      *",
        " *    *",
        "  **** "]
Six = ["  ***  ",
       " *     ",
       "*      ",
       "****** ",
       "*     *",
       " *   * ",
       "  ***  "]

Seven = [" ***** ",
         "     * ",
         "    *  ",
         "   *   ",
         "  *    ",
         " *     ",
         " *     "]

Eight = ["  ***  ",
         " *   * ",
         " *   * ",
         "  ***  ",
         " *   * ",
         " *   * ",
         "  ***  "]

Nine = ["  **** ",
        " *   * ",
        " *   * ",
        "  **** ",
        "     * ",
        "     * ",
        "     * "]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:  # se nenhum erro ocorrer TENTE
    digits = sys.argv[1]  # recuperar argumento
    row = 0  # item que esta na posicao ZERO do indice
    while row < 7:  # ler as 7 linhas de strings contando a partir do ZERO
        line = ""  # guarda a linha de string
        column = 0  # envia para a saida a linha do topo de cada digito
        while column < len(digits):  # itera cada linha   # (1) len()
            number = int(digits[column])  # atribuir o vetor como number
            digit = Digits[number]  # atribuir outro vetor como digit
            line += digit[row] + " "   # incrementa vetor
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)
                                     # (1) retorna o tamanho do item como int
