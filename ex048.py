def escreva(txt):
    print('-' * (len(txt) + 4))
    print(f'  {txt}')
    print('-' * (len(txt)+ 4))

escrita = str(input("Digite algo: "))
escreva(escrita)
