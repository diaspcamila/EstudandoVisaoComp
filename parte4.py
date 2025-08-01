# operacao aritmetica
import cv2

Bob = cv2.imread("imagem1.png")
cv2.imshow("Bob", Bob)

# adiçao: p/ adiçao as duas imagens tem que ter a mesma dimensao e tipo (8bits por exemplo)
# a cor de cada pixel é em 8 bits, logo valor maximo é 255 p/ n causar overflow

Patrick = cv2.imread("imagem2.png")
cv2.imshow("Patrick", Patrick)

print('Tipo imagem1:', Bob.dtype)
print('Tipo imagem2:', Patrick.dtype)

soma = cv2.add(Bob, Patrick)
cv2.imshow("soma", soma)

# subtraçao
subtracao = cv2.subtract(soma, Patrick)
cv2.imshow("Soma s/ Patrick", subtracao)

# mistura
mistura = cv2.addWeighted(Bob, 0.5, Patrick, 1, 0)
cv2.imshow("mistura", mistura)

#multiplicaçao - nao mt usada
multiplicacao = cv2.multiply(Patrick, Bob)
cv2.imshow("multiplicacao", multiplicacao)

# divisao - ajuste de contraste - vertificar se sao identicas - nao mt usada

cv2.waitKey(0)
cv2.destroyAllWindows()

