cadastro = dict()
gols = list()
total = 0
cadastro['nome'] = str(input("Nome: "))
cadastro['npartida'] = int(input("Numero de partidas jogadas: "))
for i in range(0, cadastro['npartida']):
    gol = gols.append(int(input(f"Quantos gols na partida {i}")))
    cadastro['gols'] = gols[:]

cadastro['total'] = sum(gols)

for k, v in cadastro.items():
    print(f"O campo {k} tem valor {v}")

print(f'O jogador {cadastro["nome"]} jogou {cadastro["npartida"]}.')
for i in range(0, cadastro['npartida']):
    print(f'=> Na partida {i}, fez {gols[i]} gol')
