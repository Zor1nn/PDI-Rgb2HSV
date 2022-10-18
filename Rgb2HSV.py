from asyncio.windows_events import NULL
import numpy as np
import cv2 as cv
import os

DIRNAME = os.path.dirname(__file__)

def main():
    nome = input("Insira o nome com o tipo da imagem que deseja trabalhar: ")
    matiz = int(input("Insira uma matiz entre 0 e 359: "))
    x = int(input("Insira um valor inteiro x para  definir o intervalo das matizes: "))

    img = cv.imread(DIRNAME + "\\" + nome) # lê a imagem e coloca em BGR
    # imgAux = img.astype(np.int32)  # converte para 32 pois pode acontecer de perder informações se trabalhar com apenas 8 bits

    # tratando estouro de intervalo
    if (matiz  - x) < 0:
        menor = 359 +  (matiz  - x)
    else:
        menor = matiz - x

    maior = (matiz + x) % 359

    if menor > maior:
        aux = menor
        menor = maior
        maior = aux

    intervalo = [menor, maior]

    print(intervalo)

    # transformando de RGB para HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h, s, v = cv.split(hsv)

    # h[np.clip(h, menor, maior)] = (h[np.clip(h, menor, maior)] + 180) % 359

    #h[menor > h > maior] = (h[menor > h > maior] + 180 ) % 360

    print(h[h in np.clip(h, menor, maior)])
    
    # h[h <= lim] += value

    # lim = 255 - 10
    # v[v > matiz] = 255
    # v[v < matiz] = 0


    print((h[h in np.clip(h, menor, maior)] + 180 ) % 359)
    final_hsv = cv.merge((h, s, v))
    img = cv.cvtColor(final_hsv, cv.COLOR_HSV2BGR)

    # imgAux = imgAux.astype(np.uint8) #converte de volta para 8 bits

    cv.imshow("Img Out",img)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
	main()