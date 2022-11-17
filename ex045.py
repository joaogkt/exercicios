from time import sleep


def contador(i, f, p):

    if p < 0:
        p = -p
    elif p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            cont += p
            sleep(0.2)
    if f < i:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            cont -= p
            sleep(0.2)
    print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
print("Agora sua vez!!")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
