def maior(* args):
    cont = maior = 0
    print('-=' * 20)
    print("Analisando os valores passados...")
    for valor in args:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo')
    print(f'O maior valor é: {maior}')

maior(2, 9, 6)
maior(9, 221, 20, 90, 56)
maior(22, 29, 26)
