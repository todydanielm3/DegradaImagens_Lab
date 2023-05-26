import gerar_degradacoes
import cv2
from matplotlib import pyplot as plt

imagem = r'lenna.png'

def mostrar_imagens(degradacao, intensidades, imagens):
    fig, axes = plt.subplots(nrows=1, ncols=len(intensidades) + 1, figsize=(30, 5), sharex=True, sharey=True)
    fig.suptitle(degradacao, fontsize=16)

    axes[0].imshow(imagens[0])
    axes[0].set_title('Imagem Original')

    for i in range(1, len(axes)):
        axes[i].imshow(imagens[i], cmap='gray', vmin=0, vmax=255)
        axes[i].set_title(f'Intensidade: {intensidades[i - 1]}')

    plt.tight_layout()
    plt.savefig(f'./graficos/{degradacao}.png')
    plt.show()

obj_degradacao = gerar_degradacoes.Degradacoes(imagem)
degradacao = 'Median_Blurring'
intensidades = [1, 3, 5, 9, 11, 13, 15]

imagens_processadas = [cv2.cvtColor(obj_degradacao.img_original, cv2.COLOR_BGR2RGB)]

for intensidade in intensidades:
    if intensidade == 0:
        imagens_processadas.append(cv2.cvtColor(obj_degradacao.img_original, cv2.COLOR_BGR2RGB))
    else:
        imagens_processadas.append(cv2.cvtColor(obj_degradacao.Median_Blurring(intensidade), cv2.COLOR_BGR2RGB))

mostrar_imagens(degradacao, intensidades, imagens_processadas)
