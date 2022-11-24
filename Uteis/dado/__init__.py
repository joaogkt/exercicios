def leiaDinheiro(msg):
    ok = False
    while not ok:
        n = str(input(msg)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f"\033[0;31mErro: '{n}' não é um valor monetário!\033[m")
        else:
            ok = True
            return float(n)
