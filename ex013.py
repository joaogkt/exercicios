times = ("Palmeiras", "Internacional", "Flamengo", "Fluminense", "Corinthians",
         "Athletico-PR", "Atletico-MG", "America Mineiro", "Fortaleza",
         "São Paulo", "Botafogo", "Santos", "Bragantino", "Goias", "Coritiba",
         "Ceará", "Cuiabá", "Atletico-GO", "Avaí", "Juventude")

print("Os 5 primeiros:", times[:5])
print("Os 4 ultimos:", times[-4:])
print("O Fortaleza esta na", times.index('Fortaleza') + 1, "ª posição")
#Listar os times em ordem alfabetica
print("Os times em ordem alfabetica:", sorted(times))
