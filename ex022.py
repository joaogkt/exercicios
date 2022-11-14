lista = list()
cont = 0
while True:
    valor = lista.append(int(input("Digite um valor: ")))
    cont += 1
    opcao = str(input("Quer continuar? [S/N] --> "))
    if opcao in 'Nn':
        break

if 5 in lista:
    print("O valor 5 foi digitado e está na lista")
else:
    print("O valor 5 NÃO foi digitado, e NÃo está na lista")
print("Foram digitados {} numeros".format(cont))
print(sorted(lista, reverse=True))
