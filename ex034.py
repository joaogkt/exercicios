from random import randint
from time import sleep
print('-'*30)
print('    SORTEIO JOGO MEGA SENA    ')
print('-'*30)
lista = list()
jogos = list()
tot = 1
qnt = int(input("Quantos jogos você deseja sortear? "))
while tot <= qnt:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {qnt} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-=' * 3, '< BOA SORTE! >', '-=' * 3)
