# filtros

import cv2

imagem = cv2.imread("imagem1.png")
cv2.imshow("Imagem", imagem)

# adiçao de filtro - blur
desfocada = cv2.blur(imagem, (5,5))
cv2.imshow("Desfocada", desfocada)

# filtro gaussiano - parametro c/ grau de suavizaçao
gaussiano = cv2.GaussianBlur(imagem, (5, 5), 0)
cv2.imshow("Gaussiano", gaussiano)

# filtro de mediana - 2o parametro eh valor impar inteiro e positivo
mediana = cv2.medianBlur(imagem, 5)
cv2.imshow("Mediana", mediana)

#filtro bilateral - preserva bordas
bilateral = cv2.bilateralFilter(imagem, 9, 75, 75)
cv2.imshow("Bilateral", bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()



