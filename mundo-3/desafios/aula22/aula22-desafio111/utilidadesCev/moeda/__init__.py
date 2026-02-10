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
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{moeda(dobro(n))}')
    print(f'Metade do preço: \t{moeda(metade(n))}')
    print(f'{a}% de aumento: \t{moeda(aumentar(n, a))}')
    print(f'{d}% de redução: \t{moeda(diminuir(n, d))}')

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


def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-' * 30)
'''
