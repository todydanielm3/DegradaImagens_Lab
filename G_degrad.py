import gerar_degradacoes
import cv2 
from matplotlib import pyplot as plt

imagem = r'lenna.png'

def mostrar_imagens(degradacao, intensidades, i1,i2,i3,i4,i5,i6,i7):
    fig,(ax1,ax2,ax3,ax4,ax5,ax6,ax7) = plt.subplots(nrows=1,
                                                        ncols=7,
                                                        figsize=(30,5),
                                                        sharex=True,
                                                        sharey=True)
    fig.suptitle(degradacao,fontsize=16)

    ax1.imshow(i1)
    ax1.set_title('Imagem Original')

    ax2.imshow(i2,cmap='gray')
    ax2.set_title(f'Intensidade:{intensidades[1]}')

    ax3.imshow(i3,cmap='gray')
    ax3.set_title(f'Intensidade:{intensidades[2]}')

    ax4.imshow(i4,cmap='gray',vmin=0,vmax=255)
    ax4.set_title(f'Intensidade:{intensidades[3]}')

    ax5.imshow(i5,cmap='gray',vmin=0,vmax=255)
    ax5.set_title(f'Intensidade:{intensidades[4]}')

    ax6.imshow(i6,cmap='gray',vmin=0,vmax=255)
    ax6.set_title(f'Intensidade:{intensidades[5]}')

    ax7.imshow(i7,cmap='gray',vmin=0,vmax=255)
    ax7.set_title(f'Intensidade:{intensidades[6]}')

    plt.tight_layout()
    plt.savefig(f'./graficos/{degradacao}.png')
    plt.show()

obj_degradacao = gerar_degradacoes.Degradacoes(imagem)
imagens_processadas=[]
degradacao = 'Median_Blurring'
intensidades = [1,3,5,9,11,13,15]


for i, intensidade in enumerate(intensidades):
    if intensidade == 0:
        imagens_processadas.append(cv2.cvtColor(obj_degradacao.img_original, cv2.COLOR_BGR2RGB))
    else:
        imagens_processadas.append(cv2.cvtColor(obj_degradacao.Median_Blurring(intensidade), cv2.COLOR_BGR2RGB))


mostrar_imagens(degradacao, intensidades,imagens_processadas[0], imagens_processadas[1], imagens_processadas[2],
                imagens_processadas[3], imagens_processadas[4], imagens_processadas[5],
                imagens_processadas[6])
