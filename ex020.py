lista = list()
opcao = 'S'

while True:
    valor = int(input("Digite um valor: "))
    if valor not in lista:
        lista.append(valor)
        print("Valor adicionado com sucesso")
    else:
        print("Valor duplicado... Não será adicionado")
    opcao = str(input("Quer continuar? [S/N] -->  ").upper().strip())
    if opcao == 'N':
        break
print(sorted(lista))
