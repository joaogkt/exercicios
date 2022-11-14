lista = list()

valor = str(input("Digite a expressão: "))

for simb in valor:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print("Sua expressão é valida")
else:
    print("Invalido")
print(lista)
print(valor)
