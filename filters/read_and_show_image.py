import numpy as np
import cv2 as cv

def main():
    
    img = cv.imread('C:/opencv/sources/doc/images/fruits.png')
    if img is None:
        print('Não localizei a imagem:', img)
        sys.exit(1)

    while True:
        ch = cv.waitKey()
        if ch == 27:
            break
        cv.imshow('Ler e Exibir Imagem', img)
        
if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()
