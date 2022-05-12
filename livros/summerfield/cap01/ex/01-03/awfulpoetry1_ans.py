#! usr/bin/env python3

import random

articles = ["o","a","um","uma","os","as","uns","umas"]
subjects = ["gato","cachorro","homem","mulher"]
verbs = ["cantar","correr","pular"]
adverbs = ["vagarosamente","silenciosamente","bem","mal"]

for _ in [1, 2, 3, 4, 5]:
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    if random.randint(0, 1) == 0:
        print(article, subject, verb)
    else:
        adverb = random.choice(adverbs)
        print(article, subject, verb, adverb)
