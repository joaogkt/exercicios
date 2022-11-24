def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um numero inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuario\033[m')
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um numero real válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuario\033[m')
            return 0
        else:
            return n


n = leiaint('Digite um numero: ')
n1 = leiaFloat('Digite um numero real: ')
print(f'Você acabou de digitar o numero {n} e o real foi {n1}')
