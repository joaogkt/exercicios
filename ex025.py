cont = homem = mulher = mulherVelha = homemNovo = maiores = maior = menor = 0

while True:
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo [M/F]: ")).upper().strip()
    cont += 1
    opcao = str(input("Quer cadastrar mais pessoas? [S/N] --> "))
    if cont == 1:
        maior = menor = idade
    else:
        if idade > maior:
            maior = idade
        elif idade < menor:
            menor = idade

    if sexo == 'M':
        homem += 1
    else:
        mulher += 1

    if sexo == 'F' and idade > 18:
        mulherVelha += 1
    elif sexo == 'M' and idade < 18:
        homemNovo += 1

    if idade >= 18:
        maiores += 1
    if opcao in 'Nn':
        break

print("Foram cadastrados {} pessoas".format(cont))
print("Entre elas, {} são mulheres e {} são homens".format(mulher, homem))
print("Dessas pessoas {} são maiores de idade".format(maiores))
print("Dessas mulheres, {} são maiores de idade".format(mulherVelha))
print("Desses homens {} são menores de idade".format(homemNovo))
print("A maior idade digitada foi {} e a menor foi {}".format(maior, menor))
