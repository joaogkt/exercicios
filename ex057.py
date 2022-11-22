c = ('\033[m', # 0 - sem cor
    '\033[0;30;41m', # 1 - vermelho
    '\033[0;30;42m', # 2 - verde
    '\033[0;30;43m', # 3 - amarelo
    '\033[0;30;44m', # 4 - azul
    '\033[0;30;45m', # 5 - roxo
    '\033[7;30m', # 6 - branco
)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(msg)
    print('~' * tam)
    print(c[0], end='')




def ajuda(com):
    from time import sleep
    print('-' * 30)
    print(f"Acessando manual do comando '{com}'")
    print('-' * 30)
    sleep(2)
    print(help(com))


comando = ''
while True:
    titulo('   SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Insira uma função ou biblioteca -> '))
    if comando.lower() == 'fim':
        print('Obrigado por se consultar conosco!')
        break
    else:
        ajuda(comando)
titulo('Até Logo :)', 1)
