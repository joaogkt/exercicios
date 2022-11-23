def aumentar(valor, porc, form=False):
    valor = valor + (valor * porc / 100)
    if form:
        return moeda(valor)
    else:
        return valor


def diminuir(valor, porc, form=False):
    valor = valor - (valor * porc / 100)
    if form:
        return moeda(valor)
    else:
        return valor


def dobro(valor, form=False):
    valor *= 2
    if form:
        return moeda(valor)
    else:
        return valor


def metade(valor, form=False):
    valor /= 2
    if form:
        return moeda(valor)
    else:
        return valor


def moeda(valor= 0, moeda = 'R$'):
    return f'{moeda}{valor:>.2f}'.replace('.', ',')


def resumo(valor, aumento, diminui):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print('-' * 30)
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{diminui}% de redução: \t{diminuir(valor, diminui, True)}')
    print('-' * 30)
