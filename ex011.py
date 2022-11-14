opcao = 'S'
soma = cont = media = maior = menor = 0
while opcao in 'Ss':
    n = int(input("Digite um numero: "))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    opcao = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
media = soma / cont
print("Soma {}, Cont {}, Media {}".format(soma, cont, media))
print("O maior {}, o menor {}".format(maior, menor))
print("FIM")