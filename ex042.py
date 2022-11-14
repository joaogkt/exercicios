dados = dict()
lista = list()
mulher = list()
velhos = list()
opcao = 'Ss'
media = 0
while True:
    dados['nome'] = str(input("Nome: "))
    dados['sexo'] = str(input("Sexo [M/F]: ")).upper()
    while dados['sexo'] not in {'M', 'F'}:
        print('Dados invalidos [M/F]')
        dados['sexo'] = str(input("Sexo [M/F]: ")).upper()
    dados['idade'] = int(input("Idade: "))
    media += dados['idade']
    lista.append(dados.copy())
    if dados['sexo'] == 'F':
        mulher.append(dados.copy())
    opcao = str(input("Deseja continuar? [S/N]: "))
    if opcao in 'Nn':
        break
media /= len(lista)
if dados['idade'] > media:
    velhos.append(dados.copy)

print(lista)
print(f"Foram cadastradas {len(lista)} pessoas")
print(f'A media de idade do grupo é: {media}')
print(f'A lista de mulheres: {mulher}')
print(f'Lista de pessoas mais velhas: {velhos}')