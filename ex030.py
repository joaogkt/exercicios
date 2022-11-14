lista = []
notas = []
dados = []
opcao = 'Ss'
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Nota 1: ")))
    dados.append(float(input("Nota 2: ")))
    lista.append(dados[:])
    notas.insert(dados(1, 2))
    dados.clear()
    notas.clear()
    opcao = str(input("Quer continuar? [S/N]: "))
    if opcao in 'Nn':
        break
print(lista)
print(notas)
print(dados)