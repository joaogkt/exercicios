print("Gerador de PA...")
n1 = int(input("Primeiro termo da sua pa: "))
razao = int(input("Razao de sua pa: "))
termo = n1
cont = 1
while cont <= 10:
    print("{} -> ".format(termo), end='')
    cont += 1
    termo += razao
print("FIM")