def leiaDinheiro(msg):
    v = str(input(msg)).strip()

    while v.isalpha() or v == '' or v.isalnum() and v.isdecimal() == False:
        v = str(input('\033[31mValor inválido. Digite novo preço:\033[m ')).strip()

    if ',' in v:
        v = v.replace(',', '.')

    return float(v)
