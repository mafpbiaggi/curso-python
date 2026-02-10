def aumentar(n, p, format=False):
    if format:
        return moeda(n + (n * (p / 100)))
    else:
        return n + (n * (p / 100))


def diminuir(n, p, format=False):
    if format:
        return moeda(n - (n * (p / 100)))
    else:
        return n - (n * (p / 100))


def dobro(n, format=False):
    if format:
        return moeda(n* 2)
    else:
        return n * 2


def metade(n, format=False):
    if format:
        return moeda(n / 2)
    else:
        return n / 2


def moeda(n):
    return f'R$ {n:>7.2f}'


def resumo(n, a, d):
    print('-' * 35)
    print(f'{"Resumo":^35}')
    print('-' * 35)
    print(f'Preço analisado: {moeda(n)}')
    print('-' * 35)
    print(f'Dobro do preço:  {moeda(dobro(n))}')
    print(f'Metade do preço: {moeda(metade(n))}')
    print(f'{a}% de aumento:  {moeda(aumentar(n, a))}')
    print(f'{d}% de redução:  {moeda(diminuir(n, d))}')
