matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for y in range(0, 3):
    for i in range(0, 3):
        matriz[y][i] = int(input(f"Valor para [{y} {i}]: "))
print('-='*30)

for y in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[y][i]:^5}]', end='')
    print()