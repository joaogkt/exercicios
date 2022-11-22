def fatorial(n, show = False):
    """
-> Calcula o fatorial de um numero.
:param n: Numero a ser calculado
:param show: (opcional) Mostrar ou não a conta
:return: O valor do fatorial de um numero n
    """
    f = 1

    for c in range(n, 0, -1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c

    return f

fatorial(5, show=True)
