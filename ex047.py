from random import randint

def sorteia(lst):
    for cont in range(0, 5):
        n = lst.append(randint(0, 20))

def somaPar(lst):
    soma = 0
    for i, v in enumerate(lst):
        if v % 2 == 0:
            soma += v
    return soma

numeros = list()
sorteia(numeros)
print(f'A lista de numeros sorteados: {numeros}')
print(f'Soma dos numeros pares: {somaPar(numeros)}')
