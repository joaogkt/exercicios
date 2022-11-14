n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))
n3 = int(input("Digite um valor: "))
n4 = int(input("Digite um valor: "))
tupla = (n1, n2, n3, n4)
print(tupla)
print("O 9 apareceu", tupla.count(9), "vezes")
if 3 in tupla:
    print("O 3 aparece na posição", tupla.index(3) + 1)
else:
    print("O 3 não aparece na lista")
#numeros pares :(
print("Numeros pares: ", end='')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')

