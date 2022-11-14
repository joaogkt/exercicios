tupla = ("Computador", "Lapis", "Caneta",
         "Caderno", "livro", 'folha', 'papel', 'tela', 'telefone', 'mochila')

for i in tupla:
    print(f'\nNa palavra {i} temos ', end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
