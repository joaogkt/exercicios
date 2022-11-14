tupla = ("Hamburguer", 23, "Batata Frita", 15, "Refrigerante", 10,
         "Cerveja", 12, "Sorvete", 9)
print("-"*50)
print(' '*10, "LISTAGEM DE PREÇO")
print("-"*50)

for i in range(0, len(tupla)):
    if i % 2 == 0:
        print(f'{tupla[i]:.<30}', end='')
    else:
        print(f'R${tupla[i]:>3.2f}')
