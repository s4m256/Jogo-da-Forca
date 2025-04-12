from PIL import Image

with Image.open("C:/Users/User/Desktop/imagem_base.jpg") as imagem:
    print(f"Formato da imagem: {imagem.format}")
    print(f"Dimensões da imagem: {imagem.size}")
    print(f"Modo da imagem: {imagem.mode}")
    imagem.show()

    