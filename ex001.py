from datetime import date

ano = int(input("Digite o ano em que voce nasceu: "))
agora = date.today()
idade = agora.year - ano
print("{} anos".format(idade))
