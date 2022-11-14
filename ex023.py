lista = list()
par = list()
impar = list()
while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    opcao = str(input("Deseja continuar? [S/N] --> "))
    if opcao in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print("A lista completa: {}".format(lista))
print("Lista de numeros pares: {}".format(par))
print("Lista de numeros impares: {}".format(impar))
