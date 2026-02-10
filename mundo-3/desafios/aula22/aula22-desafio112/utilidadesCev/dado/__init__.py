def leiaDinheiro(msg):
    v = str(input(msg)).replace(',', '.').strip()

    while v.isalpha() or v == '' or v.isalnum() and v.isdecimal() == False:
        v = str(input('\033[31mValor inválido. Digite novo preço:\033[m ')).replace(',', '.').strip()

    return float(v)

'''
# Solução do Professor:

def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            válido = True
            return float(entrada)
'''
