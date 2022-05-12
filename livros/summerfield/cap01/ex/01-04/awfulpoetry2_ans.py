#! usr/bin/env python3

import random
import sys

articles = ["a","uma","sua","dela"]

subjects = ["gata","cadela","égua","mulher","menina"]

verbs = ["cantou","correu","pulou","disse","lutou","nadou","viu","ouviu","sentiu","dormiu","esperou","criou","riu","andou"]

adverbs = ["bem quieto", "bem alto", "bem rápido", "bem lento","bem","maldosamente", "bem rude", "politicamente"]

lines = 5
if len(sys.argv) > 1:
    try:
        arg = int(sys.argv[1])
        if 1 <= arg <= 10:
            lines = arg
        else:
            print("linhas devem ser de 1 a 10 inclusive")

    except ValueError:
        print("usage: badpoetry.py [lines]")

    print()

while lines > 0:
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)

    line = f'{article} {subject} {verb}'

    if random.randint(0,1):
        adverb = random.choice(adverbs)
        line += f' {adverb}'

    print(line)
    lines -= 1

        
