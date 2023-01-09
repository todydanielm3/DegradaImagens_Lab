# Description:
# ------------------------------------------------------------

import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats.kde import gaussian_kde
import random


class Degradacoes:
    def __init__(self,caminho):
        self.caminho = caminho
        self.img_original = cv2.imread(self.caminho)


    def Gaussian_Blurring(self, k):
        imagem = cv2.GaussianBlur(self.img_original,(k,k),0)
        return imagem


    def Median_Blurring(self,k):

        imagem = cv2.medianBlur(self.img_original,k)
        return imagem


    def Brightness(self,parametros):
        a = parametros[0]
        b = parametros[1]
        # a -  alpha [1.0 - 3.0]
        # b -  beta  [0 - 99]

        imagem = cv2.convertScaleAbs(self.img_original,a,b)
        return imagem


    def Darkening_Brightness(self,g):
        gamma = -5
        invGamma = 1 /(gamma * g)

        table = np.array([((i/255)**invGamma)*255 for i in np.arange(0,256)])

        imagem = cv2.LUT(self.img_original.astype(np.uint8),table.astype(np.uint8))

        return imagem

    def Contrast(self,k):
        lab= cv2.cvtColor(self.img_original, cv2.COLOR_BGR2LAB)
        l_channel, a, b = cv2.split(lab)

        clahe = cv2.createCLAHE(clipLimit=2.0 + k, tileGridSize=(8,8))

        cl = clahe.apply(l_channel)

        # merge the CLAHE enhanced L-channel with the a and b channel
        limg = cv2.merge((cl,a,b))

        # Converting image from LAB Color model to BGR color spcae
        imagem = cv2.cvtColor(limg,cv2.COLOR_LAB2BGR)
        return imagem

    def Downsampled(self,k):
        imagem = cv2.pyrDown(self.img_original,k)
        return imagem

   def Downsampled2(self, scale_percent):
        img = self.img_original
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)

        # resize image
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_CUBIC)
        #print(dim)
        #resized = cv2.resize(resized, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_CUBIC)
        #(212, 212)         (175, 175)        (137, 137)        (100, 100)        (62, 62)        (25, 25)

        return resized 

    def Motion_Blur(self,k):
        #esses parametros serão passados para o arquivo de parametros
        # k = [0-30]

        k_v = np.zeros((k,k))
        #k_h = np.copy(k_v) #borramento horizontal

        k_v[:,int((k-1)/2)] = np.ones(k)
        #k_h[int((k-1)/2),:] = np.ones(k)

        k_v /= k
        #k_h /= k

        #--------------------#

        # Specify the kernel size.
        # The greater the size, the more the motion.

        imagem = cv2.filter2D(self.img_original,-1,k_v)
        return imagem


    def Gaussian_noise(self, k):
        image = self.img_original.astype(np.float32)
        shape = image.shape[:2]

        
        var = random.uniform(0,0.1)
        sigma = var ** 0.5
        gamma = 0.25
        alpha = 0.75
        beta = 1 - alpha

        gaussian = np.random.normal(loc=k, scale = sigma, size = (shape[0], shape[1], 1)).astype(np.float32)
        gaussian = np.concatenate((gaussian, gaussian, gaussian), axis = 2)
        #gaussian_img = image * 0.75 + 0.25 * gaussian + 0.25
        gaussian_img = cv2.addWeighted(image, alpha, beta * gaussian, beta, gamma)

        return gaussian_img

    # noise_sigma = 0.01
    # h = image.shape[0]
    # w = image.shape[1]
    # noise = np.random.randn(h, w) * noise_sigma

    # noisy_image = np.zeros(image.shape, np.float64)
    # if len(image.shape) == 2:
    #     noisy_image = image + noise
    # else:
    #     noisy_image[:,:,0] = image[:,:,0] + noise
    #     noisy_image[:,:,1] = image[:,:,1] + noise
    #     noisy_image[:,:,2] = image[:,:,2] + noise

    # """
    # print('min,max = ', np.min(noisy_image), np.max(noisy_image))
    # print('type = ', type(noisy_image[0][0][0]))
    # """

    # return noisy_image

    def JPEG_Compression(self,k):
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY),k]
        result , encimg = cv2.imencode('.jpg',self.img_original,encode_param)

        decimg = cv2.imdecode(encimg,1)
        return result
