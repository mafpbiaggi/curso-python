def leiaInt(msg):
    while True:
        try:
            n = str(input(msg)).strip()
            return int(n)

        except (ValueError, TypeError):
            print('\033[31mValor inválido.\033[m')

        except (KeyboardInterrupt):
            print('\n\033[33mO usuário não informou nenhum número inteiro.\033[m')
            return 0


def leiaFloat(msg):
    while True:
        try:
            n = str(input(msg)).replace(',', '.').strip()
            return float(n)

        except (ValueError, TypeError):
            print('\033[31mValor inválido.\033[m')

        except (KeyboardInterrupt):
            print('\n\033[33mO usuário não informou nenhum número real.\033[m')
            return 0
        