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
    return f'R$ {n:.2f}'
