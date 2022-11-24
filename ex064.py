def testeSite(url):
    import requests
    if requests.get(url).status_code == 200:
        print('O site está disponivel')
    else:
        print('O servidor está indisponivel')

url = str(input('Digite a URL do site para descobrir se ele está ativo: '))
testeSite(url)
