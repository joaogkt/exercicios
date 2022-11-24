from Uteis import Cadastro
from time import sleep


arq = 'listaDePessoas.txt'

if Cadastro.arqExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    Cadastro.criarArquivo(arq)


while True:
    resposta = Cadastro.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Listar conteúdo de um arquivo
        Cadastro.lerArquivo(arq)
    elif resposta == 2:
        Cadastro.cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = Cadastro.leiaint('Idade: ')
        Cadastro.cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(2)
