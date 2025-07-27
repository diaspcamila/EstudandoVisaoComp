# operaçoes basicas com pixels
import cv2

imagem = cv2.imread("imagem1.png")
#cv2.imshow("Imagem", imagem)

valorPixel = imagem[100, 100]
print(valorPixel)

imagem2 = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
valorPixel2 = imagem2[100, 100]
print(valorPixel2)

print(imagem[100, 100])
imagem[100, 100] = [0, 0, 255]
print(imagem[100, 100])

cv2.imshow("Imagem Modificada", imagem)

print(imagem.shape)
print(imagem2.shape)

print(imagem.size)

#pagina 84 do livro, mostra como descobrir o histograma de uma imagem e plotar


cv2.waitKey(0)
cv2.destroyAllWindows()