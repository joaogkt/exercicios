aluno = dict()

aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f'Media de {aluno["nome"]}'))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual {v}')
