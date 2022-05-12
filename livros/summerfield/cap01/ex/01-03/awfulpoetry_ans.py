#! usr/bin/env python3

import random

articles = ["o", "a", "os", "as", "um", "uma", "uns", "umas", "outro", "outra", "dele", "dela", "seu", "sua"]

subjects = ["gato","cachorro","cavalo","homem","mulher","menino","menina"]

verbs = ["cantou","correu","pulou","disse","lutou","nadou","viu","ouviu","sentiu","dormiu","esperou","criou","riu","andou"]

adverbs = ["bem quieto", "bem alto", "bem rápido", "bem lento","bem","maldosamente", "bem rude", "politicamente"]

counter = 5
while counter > 0:
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)

    if random.randint(0,1):
        print(article,subject,verb)
    else:
        adverb = random.choice(adverbs)
        print(article, subject, verb, adverb)
        counter =- 1


