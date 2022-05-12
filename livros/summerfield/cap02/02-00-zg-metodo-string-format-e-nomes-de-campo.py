Python 3.7.3 (default, Jan 22 2021, 20:04:44) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> "The novel '{0}' was published in {1}".format("Hard Times", 1854)
"The novel 'Hard Times' was published in 1854"
>>> "{{{0}}} {1}; -}}".format("I'm in braces", "I'm not")
"{I'm in braces} I'm not; -}"
>>> "{0}{1}".format("The amount due is $", 200)
'The amount due is $200'
>>> x = "three"
>>> s = "{0} {1} {2}"
>>> s = s.format("The", x, "tops")
>>> s
'The three tops'
>>> "{who} turned {age} this year".format(who="She", age=88)
'She turned 88 this year'
>>> 'The boy was 12 last week'
'The boy was 12 last week'
>>> "The {who} was {0} last week".format(12, who="boy")
'The boy was 12 last week'
>>> stock = ["paper", "envelopes", "notepads", "pens", "paper clips"]
>>> "We have{0[1]} and {0[2]} in stock".format(stock)
'We haveenvelopes and notepads in stock'
>>> We have{0[1] } and {0[2]} in stock".format(stock)
SyntaxError: invalid syntax
>>> "We have {0[1]} and {0[2]} in stock".format(stock)
'We have envelopes and notepads in stock'
>>> d = dict(animal="elephant", weight=12000)
>>> "The {0[animal]} weighs {0[weight]}kg".format(d)
'The elephant weighs 12000kg'
>>> import math
>>> import sys
>>> "math.pi=={0.pi} sys.maxunicode=={1.maxunicode}".format(math, sys)
'math.pi==3.141592653589793 sys.maxunicode==1114111'
>>> 
