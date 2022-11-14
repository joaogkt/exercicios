from random import randint

print("-"*40)
print("JOGO NA MEGA SENA")
print("-"*40)
list = []
jogos = int(input("Quantos jogos você quer sortear ?"))
for i in range(jogos):
    list.append(randint(0,60), randint(0,60), randint(0,60), randint(0,60), randint(0,60))
    print(list)
    list.clear()