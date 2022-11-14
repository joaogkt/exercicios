from time import sleep
lista = []

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("1ª nota: "))
    nota2 = float(input("2ª nota: "))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    opcao = str(input("Deseja continuar? [S/N]: "))
    if opcao in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-' * 35)
    opc = int(input('Mostra notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print("Finalizando...")
        break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
sleep(1)
print("<<< VOLTE SEMPRE >>>")
