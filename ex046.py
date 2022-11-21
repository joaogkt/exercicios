def area(largura, comprimento):
    area = largura * comprimento
    print(f"A area de um terreno {largura}x{comprimento} é de {area}m²")

print("Controle de terrenos")
print('-' * 20)
largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))
area(largura, comprimento)
