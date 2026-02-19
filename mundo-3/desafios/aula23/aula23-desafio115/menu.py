from cria import addPessoa
from lista import listaPessoa


def inicio():
        while True:
            try:
                print('=' * 60)
                print(f'{"Menu":^60}')
                print('-' * 60)
                menu = int(input('0 - Sair\n1 - Cadastrar\n2 - Listar\n\n>>> '))
                print('-' * 60)

                if menu == 1:
                    addPessoa()
                    
                elif menu == 2:
                    listaPessoa()
                    
                elif menu == 0:
                    print(f'\033[34m{"Finalizando operações ... Até breve.":^60}\033[m')
                    print('-' * 60)
                    break

                else:
                    print(f'\033[31mOpção inválida. Tente novamente.\033[m')

            except (ValueError, TypeError):
                print(f'\033[31mValor incorreto, insira apenas números.\033[m')

            except (KeyboardInterrupt, EOFError):
                print()
                print('-' * 60)
                print(f'\033[33m{"Encerramento forçado do sistema ... Até mais.":^60}\033[m')
                print('-' * 60)
                break
