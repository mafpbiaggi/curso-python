def listaPessoa():
    try:
        a = open('mundo-3/desafios/aula23/aula23-desafio115/cadastro.txt', 'r', encoding='utf-8')
        print(a.read())
        a.close()
    
    except (FileNotFoundError): 
        print('\033[33mO arquivo de cadastro não existe ou está vazio.\033[m')
    