def addPessoa():
        while True:
                try:
                        print('\033[35mAdicionando pessoa ...\033[m\n')
                        nome = str(input('  Digite o nome: ')).upper().strip()
                        idade = int(input('  Digite a idade: '))
                        prep = f'{nome}, {idade} anos.\n'

                        a = open('mundo-3/desafios/aula23/aula23-desafio115/cadastro.txt', 'a+', encoding='utf-8')
                        a.write(prep)
                        a.close()
                        print(f'\n\033[32mCadastro realizado com sucesso.\033[m')
                        break

                except (ValueError, TypeError):
                        print(f'\033[31mValor inválido para o campo idade. Tente novamente.\033[m')
                
                except (KeyboardInterrupt):
                        print(f'\n\n\033[33mPreenchimento cancelado pelo usuário.\033[m')
                        break
