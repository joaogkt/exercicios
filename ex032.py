matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somatot = soma = maior = cont = pares = 0
for y in range(0, 3):
    for i in range(0, 3):
        matriz[y][i] = int(input(f"Valor para [{y} {i}]: "))
        somatot += matriz[y][i]

for i in range(0, 3):
    if i == 0:
        maior = matriz[1][i]
    elif matriz[1][i] > maior:
        maior = matriz[1][i]

for y in range(0, 3):
    soma += matriz[y][2]

print('-='*30)
for y in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[y][i]:^5}]', end='')
        if matriz[y][i] % 2 == 0:
            pares += matriz[y][i]
    print()
print('-=' * 30)
print(f'A soma total é de {somatot}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {maior}')
print(f'A soma dos valores pares é {pares}')
