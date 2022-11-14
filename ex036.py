lista = []
while True:
    nome = str(input("Nome: "))
    while len(nome) < 4:
        print("Nome deve ter mais de 3 caracteres")
        nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    while idade > 150 or idade < 0:
        print("A idade deve ser entre 0 e 150")
        idade = int(input("Idade: "))
    salario = float(input("Salario: "))
    while salario < 0:
        print("Salario deve ser maior que 0")
        salario = float(input("Salario: "))
    sexo = str(input("Sexo: [F/M]: ")).upper().strip()
    while sexo not in {'M', 'F'}:
        print("O sexo deve ser M ou F")
        sexo = str(input("Sexo: [F/M]: ")).upper()
    civil = str(input("Estado civil: [S/C/V/D]: ")).upper()
    while civil not in {'S', 'C', 'V', 'D'}:
        print("Deve ser uma das opcoes")
        civil = str(input("Estado civil: [S/C/V/D]: ")).upper()
    dados = [nome, idade, salario, sexo, civil]
    lista.append(dados[:])
    dados.clear()
    print(lista)
    opcao = str(input("Deseja cadastrar uma nova pessoa? [S/N]: "))
    if opcao in 'Nn':
        break
print(lista)
