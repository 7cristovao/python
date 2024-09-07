def aumentar(p, q, f):
    if f == True:
        return f'R$ {p * (1 + q / 100):.2f}'
    else:
        return p * (1 + q / 100)
def diminuir(p, q, f):
    if f == True:
        return f'R$ {p * (1 - q / 100):.2f}'
    else:
        return p * (1 - q / 100)
def dobro(p, f):
    if f == True:
        return f'R$ {p * 2:.2f}'
    else:
        return p * 2
def metade(p, f):
    if f == True:
        return f'R$ {p / 2:.2f}'
    else:
        return p / 2
def moeda(p):
    return f'R$ {p:.2f}'