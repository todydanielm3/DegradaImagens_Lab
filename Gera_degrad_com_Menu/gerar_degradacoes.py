import cv2
import numpy as np

class Degradacoes:
    def __init__(self, caminho):
        self.caminho = caminho
        self.img_original = cv2.imread(self.caminho)

    def Gaussian_Blurring(self, k):
        imagem = cv2.GaussianBlur(self.img_original, (k, k), 0)
        return imagem

    def Median_Blurring(self, k):
        imagem = cv2.medianBlur(self.img_original, k)
        return imagem

    def Brightness(self, parametros):
        a, b = parametros[0], parametros[1]
        imagem = cv2.convertScaleAbs(self.img_original, a, b)
        return imagem

    def Darkening_Brightness(self, g):
        gamma = -5
        invGamma = 1 / (gamma * g)
        table = np.array([((i / 255) ** invGamma) * 255 for i in np.arange(0, 256)])
        imagem = cv2.LUT(self.img_original.astype(np.uint8), table.astype(np.uint8))
        return imagem

    def Contrast(self, k):
        lab = cv2.cvtColor(self.img_original, cv2.COLOR_BGR2LAB)
        l_channel, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=2.0 + k, tileGridSize=(8, 8))
        cl = clahe.apply(l_channel)
        limg = cv2.merge((cl, a, b))
        imagem = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
        return imagem

    def Downsampled(self, k):
        imagem = cv2.pyrDown(self.img_original, k)
        return imagem

    def Motion_Blur(self, k):
        k_v = np.zeros((k, k))
        k_v[:, int((k - 1) / 2)] = np.ones(k)
        k_v /= k
        imagem = cv2.filter2D(self.img_original, -1, k_v)
        return imagem

    def Gaussian_noise(self, k):
        image = self.img_original.astype(np.float32)
        shape = image.shape[:2]
        var = np.random.uniform(0, 0.1)
        sigma = var ** 0.5
        gamma = 0.25
        alpha = 0.75
        beta = 1 - alpha
        gaussian = np.random.normal(loc=k, scale=sigma, size=(shape[0], shape[1], 1)).astype(np.float32)
        gaussian = np.concatenate((gaussian, gaussian, gaussian), axis=2)
        gaussian_img = cv2.addWeighted(image, alpha, beta * gaussian, beta, gamma)
        return gaussian_img

    def JPEG_Compression(self, k):
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), k]
        result, encimg = cv2.imencode('.jpg', self.img_original, encode_param)
        decimg = cv2.imdecode(encimg, 1)
        return result

def menu_degradacoes():
    print("Escolha uma degradação:")
    print("1 - Desfoque Gaussiano")
    print("2 - Desfoque Mediano")
    print("3 - Ajuste de Brilho")
    escolha = int(input("Digite o número da degradação desejada: "))
    return escolha

def aplicar_degradacao(escolha):
    imagem = r'lenna.png'
    obj_degradacao = Degradacoes(imagem)

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

def mostrar_imagem(imagem):
    plt.imshow(imagem, cmap='gray')
    plt.axis('off')
    plt.show()
