
cadastro = dict()
lista = list()

cadastro['nome'] = str(input("Nome: "))
anonasc = int(input("Ano de nascimento: "))
cadastro['idade'] = 2022 - anonasc
cadastro['ctps'] = int(input("Carteira de trabalho: "))

if cadastro['ctps'] != 0:
    cadastro['anoContratacao'] = int(input("Ano de contratação: "))
    cadastro['salario'] = float(input("Salario: "))
    cadastro['aposenta'] = (cadastro['anoContratacao'] -  anonasc) + 35

for k, v in cadastro.items():
    print(f'{k} = {v}')
