lista = list()
par = list()
impar = list()
for i in range(1, 8):
    lista.append(int(input(f"{i}º valor: ")))
print(lista)
for p in lista:
    if p % 2 == 0:
        par.append(p)
    else:
        impar.append(p)
sorted(par)
sorted(impar)
print(f"Os valores pares digitados foram: {par}")
print(f"Os valores impares digitados foram: {impar}")
