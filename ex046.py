def area(largura, comprimento):
    area = largura * comprimento
    print("Controle de terrenos")
    print(f"A area de um terreno {largura}x{comprimento} é de {area}m²")

largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))
area(largura, comprimento)