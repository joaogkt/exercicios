def notas(*nota, sit = False):
    """
    -> Função para calcular notas e retornar dicionario com total, maior, menor, media
    :param -> *nota
    :param -> sit=False,(opcional) se for verdadeiro retorna a situação do aluno, 'boa', 'mediana' e 'ruim'.
    """
    count = soma = maior = menor = media = 0
    dicionario = dict()
    for valor in nota:
        if count == 0:
            maior = menor = valor
        else:
            if valor > maior:
                maior = valor
            elif valor < menor:
                menor = valor
        soma += valor
        count += 1
    media = soma/count
    dicionario = {'total': count,
    'maior': maior,
    'menor': menor,
    'média': media,
    'soma': soma}
    if sit == True:
        if media >= 7:
            dicionario['situação'] = 'Boa'
        elif media < 5:
            dicionario['situação'] = 'Ruim'
        else:
            dicionario['situação'] = 'Mediana'

    return dicionario

resposta = notas(5.5, 7.3, 5, 8, 10, 6, 7, 10, 5, sit=True)
print(resposta)