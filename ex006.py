from math import factorial
from time import sleep
n1 = int(input("Digite um numero para descobrir sua fatorial: "))
c = n1
f = 1
#f = factorial(n1)
print("Calculando {}!".format(n1))
sleep(1)
while c > 0:
    print("{}".format(c), end="")
    print(' x ' if c > 1 else ' = ',end='')
    f = f * c
    c -= 1
print("{}".format(f))
#print("O fatorial de {} é {}".format(n1, f))