print("Sequencia de Fibonacci")
print('-=-'* 10)
n = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
cont = 3
print("{} -> {}".format(t1, t2), end="")
while cont <= n:
    cont += 1
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(" -> {}".format(t3), end='')
print(" -> FIM")