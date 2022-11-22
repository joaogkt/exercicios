def notas(*args, sit=False):
    dic = dict()
    dic['total'] = len(args)
    dic['maior'] = max(args)
    dic['menor'] = min(args)
    dic['media'] = sum(args)/len(args)
    if sit:
        if dic['media'] >= 7:
            dic['situação'] = 'Boa'
        elif dic['media'] >= 5:
            dic['situação'] = 'Razoavel'
        else:
            dic['situação'] = 'Ruim'
    return dic

resp = notas(7.4, 2.5, 8, 6,5, sit=True)
print(resp)
