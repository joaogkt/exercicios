from random import randint

tupla = (randint(0, 30), randint(0, 30), randint(0, 30), randint(0, 30), randint(0, 30))
print("Os valores sorteados foram:", end='')
for i in tupla:
    print(" {} ".format(i), end='')

print("\nO maior valor sorteado foi", max(tupla))
print("O menor valor sorteado foi", min(tupla))
