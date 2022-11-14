lista = list()
maior = menor = 0
for c in range(0,5):
    lista.append(int(input(f"Digite um valor na posição {c}: ")))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print(f'Voce digitou essa lista {lista}')
print(f"O maior valor foi {maior} e foi digitado na posição ", end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}...", end='')
print()
print(f'O menor valor foi {menor} e foi digitado na posição ', end='')
for i, v in enumerate(lista):
    if v == menor:
       print(f'{i}...', end='')