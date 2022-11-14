from time import sleep
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
opcao = 0
while opcao != 5:
    print("""Menu de opções
    Escolha uma opção: 
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa""")
    opcao = int(input(">>> Qual a sua opcao: "))
    if opcao == 1:
        print("A soma de {} + {} = {}".format(n1, n2, n1+n2))
    elif opcao == 2:
        print("A multiplicação de {} * {} = {}".format(n1, n2, n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print("O maior numero entre {} e {} é {}".format(n1, n2, n1))
        else:
            print("O maior numero entre {} e {} é {}".format(n1, n2, n2))
    elif opcao == 4:
        print("Informe novamente os numeros")
        n1 = float(input("Digite o primeiro valor: "))
        n2 = float(input("Digite o segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opção invalida, tente novamente")
    sleep(2)
print("Fim do programa, volte sempre")