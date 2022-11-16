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
    opcao = str(input("Deseja continuar? [S/N]: ")).upper()
    while opcao not in {'S', 'N'}:
        print("ERRO! Responda apenas com S ou N")
        opcao = str(input("Deseja continuar? [S/N]: ")).upper()
    if opcao in 'Nn':
        break

media /= len(lista)

for p in lista:
    if p['sexo'] == 'F':
        mulher.append(p['nome'])
        
for p in lista:
    if p['idade'] > media:
        velhos.append(p['nome'])
    
print(lista)
print(f"Foram cadastradas {len(lista)} pessoas")
print(f'A media de idade do grupo é: {media:5.2f}')
print(f'A lista de mulheres: {mulher}')
print(f'Lista de pessoas mais velhas: {velhos}')
