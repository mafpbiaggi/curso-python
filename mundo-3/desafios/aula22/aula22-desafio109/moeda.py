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


'''
# Solução do Professor:

def aumentar (preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, format=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}.replace(".", ",")'
'''
