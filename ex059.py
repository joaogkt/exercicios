from Uteis import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, form=True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, form=True)}')
print(f'Aumentando 10% temos {moeda.aumentar(p, 10, form=True)}')
print(f'Reduzindo 13% temos {moeda.diminuir(p, 13, form=True)}')
