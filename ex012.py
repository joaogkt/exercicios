while True:
    tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
         'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
         'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    numero = int(input("Digite um numero de 1 a 20 para ve-lo por extenso: "))
    while numero > 20 or numero < 0:
        print("Tente novamente. ", end='')
        numero = int(input("Digite um numero de 1 a 20 para ve-lo por extenso: "))
    print(tupla[numero])
    opcao = str(input("Deseja continuar? [S/N]: "))
    if opcao in 'Nn':
        break
print("PROGRAMA FINALIZADO")
