cadastro = dict()
lista = list()
gols = list()
opcao = 'Ss'
while True:
    cadastro.clear()
    cadastro['nome'] = str(input("Nome: "))
    numeropartidas = int(input("Numero de partidas jogadas: "))
    gols.clear()
    for i in range(0, numeropartidas):
        gols.append(int(input(f"Quantos gols na partida {i+1}")))
    cadastro['gols'] = gols[:]
    cadastro['total'] = sum(gols)
    lista.append(cadastro.copy())
    opcao = str(input("Deseja continuar? [S/N]: ")).upper()[0]
    while opcao not in {'S', 'N'}:
        print("ERRO, opcao deve ser S ou N")
        opcao = str(input("Deseja continuar? [S/N]: ")).upper()[0]
    if opcao in 'Nn':
        break
print('-=' * 30)
print('cod ', end='')
for i in cadastro.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)

for k, v in enumerate(lista):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input("Mostrar dados de qual jogador? [999 para parar]"))
    if busca == 999:
        break
    if busca >= len(lista):
        print(f"ERRO! Não existe jogador com o código {busca}")
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {lista[busca]["nome"]}')
        for i, g in enumerate(lista[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')

