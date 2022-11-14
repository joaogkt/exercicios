cadastro = dict()
gols = list()
total = 0
cadastro['nome'] = str(input("Nome: "))
numeropartidas = int(input("Numero de partidas jogadas: "))
for i in range(0, numeropartidas):
    gols.append(int(input(f"Quantos gols na partida {i}")))
    cadastro['gols'] = gols[:]

cadastro['total'] = sum(gols)

for k, v in cadastro.items():
    print(f"O campo {k} tem valor {v}")

print(f'O jogador {cadastro["nome"]} jogou {numeropartidas}.')
for i in range(0, numeropartidas):
    print(f'=> Na partida {i}, fez {gols[i]} gol')
print(f"Foi um total de {cadastro['total']} gols")