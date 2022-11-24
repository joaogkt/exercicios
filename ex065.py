import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('ERRO, Não foi possivel acessar o site')
else:
    print('Site acessado com sucesso!!')