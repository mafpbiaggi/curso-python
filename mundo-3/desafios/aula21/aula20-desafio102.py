'''
Desafio 102: https://youtu.be/etjJ_4Eqrk8?t=2480
Correção: 

'''
sub = 'Função para fatorial'

'''
Enunciado:
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e o outro chamado show, que será
um valor lógico (opcional) indicando se será mostrado ou não na tela o PROCESSO
de cálculo do fatorial.

Criar o docstring para a função fatorial:

    fatorial(n, show=False)
        -> Calcula o Fatorial de um número
        :param n: O número a ser calculado.
        :param show: (Opcional) Mostrar ou não a conta.
        :return: O valor do Fatorial de um número n.

Exemplo:

    print(fatorial(5))
    >>> 120

    print(fatorial(5, show=True))
    >>> 5 x 4 x 3 x 2 x 1 = 120
'''

def fatorial(n, show=False):
    """
    fatorial(n, show=False)
    -> Calcula o Fatorial de um número
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """

    f = 1
    for c in range(n, 0, -1):
        if show == True:
            if c != 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
        
        f *= c
    return f


# Main
print('=' * 60)
print(f'{"Desafio 102":^60}')
print('-' * 60)
print(f'{sub:^60}')
print('-' * 60)

print(fatorial(5, show=True))
print(fatorial(4))
print(fatorial(6, show=False))
print(fatorial(7, show=True))
print(help(fatorial))
print('=' * 60)
