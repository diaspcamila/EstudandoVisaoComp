# mini capcitaçao open cv
#leitura e mostrando a imagem

import cv2

imagem = cv2.imread("imagem1.png")
cv2.imshow("Imagem", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()

# imread le a imagem
# imshow exibe a imagem



