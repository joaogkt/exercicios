n = cont = soma = 0
n = int(input("Digite um numero, [999 para sair]: "))
while True:
    if n == 999:
        break
    soma += n
    cont += 1
    n = int(input("Digite um numero, [999 para sair]: "))
print("Você digitou {} numeros e a soma entre eles foi {}".format(cont, soma))
