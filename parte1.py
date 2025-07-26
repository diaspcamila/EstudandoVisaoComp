# mini capcitaçao open cv

import cv2

imagem = cv2.imread("imagem1.png")
cv2.imshow("Imagem", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()

# imread le a imagem
# imshow exibe a imagem

# manipulaçao de imagens (pre processamento)

# conversao de cor: bom lembrar que sempre as imagens chegam em BGR
cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# binarizacao: transforma a imagem para apenas duas cores

cv2.threshold(imagem, 0, 255, cv2.THRESH_BINARY_INV)
# preto e branco

cv2.GaussianBlur() # ou cv2.medianBlur() remoçao de ruido

cv2.Canny() # detecçao de bordas

cv2.resize() # redimensionamento da imagem

cv2.imwrite("imagem2.png", imagem) # salva a imagem
cv2.imshow("nova imagem", imagem)

# detecçao de formas e regioes



