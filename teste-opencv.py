from pickle import TRUE
import cv2
import numpy as np

def empty(a):
    pass

def controleHSV():
    cv2.namedWindow('HSV')
    cv2.resizeWindow('HSV', 640, 240)
    cv2.createTrackbar("HUE min", "HSV", 0, 179, empty)
    cv2.createTrackbar("HUE max", "HSV", 179, 179, empty)
    cv2.createTrackbar("SAT min", "HSV", 0, 255, empty)
    cv2.createTrackbar("SAT max", "HSV", 255, 255, empty)
    cv2.createTrackbar("VALUE min", "HSV", 0, 255, empty)
    cv2.createTrackbar("VALUE max", "HSV", 255, 255, empty)

imagem = cv2.imread('molde-foguete.jpg', cv2.IMREAD_COLOR)
#cv2.namedWindow('Teste_1')
print("Dimensoes da imagem: ",imagem.shape)
#Redimensionando a janela
largura = int(imagem.shape[1] * 15 / 100)
altura = int(imagem.shape[0] * 15 / 100)
dim = (largura, altura)
img = cv2.resize(imagem, dim, interpolation=cv2.INTER_AREA)
print("Dimensoes da imagem: ",img.shape)

controleHSV()

#Imagem em HSV
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
fator_escala = 255/360
lvermelho = np.array([0 *fator_escala, 100 *fator_escala, 100 *fator_escala])
uvermelho = np.array([0 *fator_escala, 10 *fator_escala, 100 *fator_escala])


while TRUE:
    h_min = cv2.getTrackbarPos("HUE min","HSV")
    h_max = cv2.getTrackbarPos("HUE max","HSV")
    s_min = cv2.getTrackbarPos("SAT min","HSV")
    s_max = cv2.getTrackbarPos("SAT max","HSV")
    v_min = cv2.getTrackbarPos("VALUE min","HSV")
    v_max = cv2.getTrackbarPos("VALUE max","HSV")

    lowerValue = np.array([h_min, s_min, v_min])
    upperValue = np.array([h_max, s_max, v_max])

    mascara = cv2.inRange(img2, lowerValue, upperValue)
    final = cv2.bitwise_and(img, img, mask = mascara)

    hstack = np.hstack([final, img])
    #cv2.imshow("imagem",img)
    #cv2.imshow("mascara", mascara)
    #cv2.imshow("resultado", final)
    cv2.imshow("Ambos", hstack)
    #print(h_min)
    if cv2.waitKey(1)==27:
        break
#Criando mascara de cores
#masc1 = cv2.inRange(img2, lvermelho,uvermelho)
#cv2.imshow('Teste_1', img)
#cv2.imshow('mascara', masc1)
#cv2.imshow('Teste_3', img2)


key = cv2.waitKey(0)
if (key == 27):
    cv2.destroyAllWindows()

