def voto(year):
    from datetime import date
    global age
    agora = date.today()
    age = agora.year - year
    if age < 16:
        return f'Com {age} anos: voto negado'
    elif 18 > age >= 16 or age >= 65:
        return f'Com {age} anos: voto opcional'
    else:
        return f'Com {age} anos: voto obrigatorio'

ano = int(input('Digite o ano de seu nascimento para saber a situação do seu voto: '))
print(voto(ano))
