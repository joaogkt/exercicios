def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um numero inteiro.')
        if ok == True:
            break
    return valor

n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')
