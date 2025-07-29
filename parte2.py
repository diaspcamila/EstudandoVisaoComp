# pre processamento de imagens / manipulaçao das imagens
import cv2

imagem = cv2.imread("imagem1.png")
cv2.imshow("Imagem", imagem)

# conversao de cor: bom lembrar que sempre as imagens chegam em BGR
imagemGRAY = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
imagemRGB = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

cv2.imwrite("imagemGRAY.png", imagemGRAY) # salva as imagens
cv2.imwrite("imagemRGB.png", imagemRGB)

cv2.imshow("Gray", imagemGRAY)
cv2.imshow("RGB", imagemRGB)

# binarizacao: transforma a imagem para apenas duas cores a sua escolha

_, imagemBinarizada = cv2.threshold(imagemGRAY, 0, 255, cv2.THRESH_BINARY_INV)

cv2.imwrite("imagemBinarizada.png", imagemBinarizada)
cv2.imshow("Binarizada", imagemBinarizada)

# redimensionamento da imagem
imagemRed = cv2.resize(imagem, (200, 200))
cv2.imshow("Imagem Redimensionada", imagemRed)
# pag 101 mostra mais parametros que podem ser usados no resize

cv2.waitKey(0)
cv2.destroyAllWindows()