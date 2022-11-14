lista = list()
maior = menor = 0
for i in range(0, 5):
    valor = int(input("Digite um numero: "))
    if i == 0 or valor > lista[-1]:
        lista.append(valor)
        print("Adicionado ao final da lista...")
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print("Adicionado na posição {} da lista...".format(pos))
                break
            pos += 1

print(lista)
