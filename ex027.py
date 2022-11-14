dados = list()
lista = list()
pesados = list()
leves = list()
opcao = 'Ss'
maior = menor = 0
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    lista.append(dados[:])
    if len(lista) == 1:
        maior = menor = dados[1]
    else:
        if maior < dados[1]:
            maior = dados[1]
        elif menor > dados[1]:
            menor = dados[1]
    dados.clear()
    opcao = str(input("Quer continuar? [S/N]: "))
    if opcao in 'Nn':
        break
print(lista)
for p in lista:
    if p[1] >= 80:
        pesados.append(p[0])
    else:
        if p[1] < 70:
            leves.append(p[0])

print(f'Foram cadastradas {len(lista)} pessoas')
print(f'O maior peso cadastrado foi {maior}Kg. ', end='')
print(f'Pesados: {pesados}')
print(f'O menor peso cadastrado foi {menor}Kg. ', end='')
print(f'Leves:  {leves}')
