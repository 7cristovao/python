Python 3.7.3 (default, Jul 25 2020, 13:03:44) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> int("250")
250
>>> str(125)
'125'
>>> int(0.1)
0
>>> int("err")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("err")
ValueError: invalid literal for int() with base 10: 'err'
>>> ([])
[]
>>> str("dia") + str("e") + str("noite")
'diaenoite'
>>> str("diaenoite") += str("e madrugada")
SyntaxError: can't assign to function call
>>> "dia" += "madrugada"
SyntaxError: can't assign to literal
>>> name = "Dom"
>>> name + "Quixote"
'DomQuixote'
>>> name += "Quixote"
>>> name
'DomQuixote'
>>> len(name)
10
>>> even = [2,4,6,8]
>>> even
[2, 4, 6, 8]
>>> even.append(10)
>>> even
[2, 4, 6, 8, 10]
>>> even += [12]
>>> even
[2, 4, 6, 8, 10, 12]
>>> even[1]=16
>>> even
[2, 16, 6, 8, 10, 12]
>>> 
