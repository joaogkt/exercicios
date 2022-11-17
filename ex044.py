from random import randint
from time import sleep
numero = int(input("Quantas pessoas irão participar do seu sorteio? "))
qnt = int(input("Quantos numeros você quer sortear? "))
print(f"O sorteio será realizado do numero 1 ao {numero}")
print(f"Você sorteou {qnt} numeros")
print("E os numeros sorteados foram...")
sleep(2)
for i in range(0, qnt):
    sorteio = randint(1, numero)
    sleep(3)
    print(f'{i+1}º vencedor -> {sorteio}')
if qnt == 1:
    print("  <<  PARABÉNS AO VENCEDOR  >>")
else:
    print('  <<  PARABÉNS AOS VENCEDORES  >>  ')