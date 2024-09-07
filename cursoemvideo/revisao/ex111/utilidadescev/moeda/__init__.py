# q : aumento
# r : desconto

def aumentar(p, q):
    return  p * (1 + q / 100)
def diminuir(p, r):
    return p * (1 - r / 100)
def dobro(p):
    return p * 2
def metade(p):
    return p / 2
def moeda(p):
    return f'R$ {p:.2f}'
def resumo(p, q, r):
    print('-' * 30)
    print('       RESUMO DO VALOR       ')
    print('-' * 30)
    print(f'Preço analisado:     R$ {p:.2f}')
    print(f'Dobro do preço:      R$ {dobro(p):.2f}')
    print(f'Metade do preço:     R$ {metade(p):.2f}')
    print(f'{q}% de aumento:     R$ {aumentar(p, q):.2f}')
    print(f'{r}% de redução:     R$ {diminuir(p, r):.2f}')
    print('-' * 30)