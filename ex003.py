print("Calculo do salario")
salario = float(input("Salario atual: R$"))
if salario < 500:
    desconto = salario * 0.15
    salario = salario + desconto
    print("Salario com reajuste: R$", salario)
elif 500 <= salario <= 1000:
    desconto = salario * 0.10
    salario = salario + desconto
    print("Salario com reajuste: R$", salario)
else:
    desconto = salario * 0.05
    salario = salario + desconto
    print("Salario com reajuste: R$", salario)
