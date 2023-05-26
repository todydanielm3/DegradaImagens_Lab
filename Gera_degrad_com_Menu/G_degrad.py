import cv2
from matplotlib import pyplot as plt
import gerar_degradacoes

imagem = r'lenna.png'
obj_degradacao = gerar_degradacoes.Degradacoes(imagem)

def mostrar_imagem(imagem):
    plt.imshow(imagem, cmap='gray')
    plt.axis('off')
    plt.show()

def aplicar_degradacao(escolha):
    if escolha == 1:
        intensidade = int(input("Digite a intensidade do desfoque gaussiano: "))
        imagem_degradada = obj_degradacao.Gaussian_Blurring(intensidade)
        mostrar_imagem(imagem_degradada)
    elif escolha == 2:
        intensidade = int(input("Digite a intensidade do desfoque mediano: "))
        imagem_degradada = obj_degradacao.Median_Blurring(intensidade)
        mostrar_imagem(imagem_degradada)
    elif escolha == 3:
        parametros = [float(input("Digite o valor de 'alpha' (1.0 - 3.0): ")), int(input("Digite o valor de 'beta' (0 - 99): "))]
        imagem_degradada = obj_degradacao.Brightness(parametros)
        mostrar_imagem(imagem_degradada)
    # Adicione mais opções conforme necessário

# Execução do programa
if __name__ == "__main__":
    opcao = gerar_degradacoes.menu_degradacoes()
    aplicar_degradacao(opcao)
