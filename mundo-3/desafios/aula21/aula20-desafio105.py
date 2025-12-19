'''
Desafio 105: https://youtu.be/etjJ_4Eqrk8?t=2692
Correção: 

'''
sub = 'Analisando e gerando dicionários'

'''
Enunciado:
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:

    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação (Opcional)

Valores da situação:
    - Acima de 7 = Boa
    - Entre 5 e 7 = Razoável
    - Abaixo de 5 = Ruim

Esse programa precisa ter o docstring para ajuda interativa.
'''

def notas(*nota, sit=False):
    """
    Analisa notas inseridas pelo usuário e retorna um dicionário
    com informações.
    
    :param nota: Valores para cada nota de cada aluno.
    :param sit: Campo validador de situação.
                False = padrão
                True  = Gera e adiciona situação ao dicionário
    :return: Dicionário com o resultado da análise
    """
    result = dict()
    
    result['total_notas'] = len(nota)
    result['maior_nota'] = max(nota)
    result['menor_nota'] = min(nota)
    
    media = sum(nota) / len(nota)
    result['media'] = f'{media:.2f}'
    
    if sit == True:
        if media < 5:
            result['situacao'] = 'Ruim'
        
        if media >= 5 and media < 7:
            result['situacao'] = 'Razoável'

        if media > 7:
            result['situacao'] = 'Boa'

    return result


# Main
print('=' * 100)
print(f'{"Desafio 105":^100}')
print('-' * 100)
print(f'{sub:^100}')
print('-' * 100)

print(notas(5.5, 9, 8.5, 10))
print(notas(1, 3, 6.5, sit=True))
print(notas(1, 3, 6.5, sit=False))
print(notas(2, 3, 1.75, 5.5, 9, 8.5, 8.25, sit=True))
print(help(notas))
print('=' * 100)
