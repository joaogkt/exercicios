from Uteis import dado, moeda

n = dado.leiaDinheiro('Digite o preço: R$')
porc = int(input('Aumento de quantos %? [999 para ser igual a 0]: '))
porcd = int(input('Diminuir quantos %? [999 para ser igual a 0]: '))

if porc == 999:
    porc = 0
if porcd == 999:
    porcd = 0

moeda.resumo(n, porc, porcd)