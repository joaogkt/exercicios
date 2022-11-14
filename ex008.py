print("Gerador de PA...")
n1 = int(input("Primeiro termo da sua pa: "))
razao  = int(input("Razao de sua pa: "))
termo = n1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print("{} -> ".format(termo), end='')
        termo += razao
        cont += 1
    print("Pausa")
    mais = int(input("Quantos termos você quer mostrar a mais ? "))
print("FIM")