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

try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            add = digit[row]
            change = 0
            changes = ""
            while change < len(add):
                if add[change] == "*":
                    changes += str(number)
                else:
                    changes += " "
                change += 1
            add = changes
            line += add + " "    
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits_ans.py <number>")
except ValueError as err:
    print(err, "in", digits)
