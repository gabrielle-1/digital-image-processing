import sys
import cv2 as cv

def main():
    
    img = cv.imread('C:\\opencv\\sources\\samples\\data\\fruits.jpg')
    if img is None:
        print('Não localizei a imagem:', img)
        sys.exit(1)    

    mf = cv.blur(img, ksize = (5,5))    
            
    while True:
        ch = cv.waitKey()
        if ch == 27:
            break

        mb = cv.medianBlur(img, 9)                

        for i in range(3):
            mb = cv.medianBlur(mb, 9)                
            cv.imshow('Median Blur' + str(i), mb)

        cv.imshow('Image Original', img)
        cv.imshow('Mid Image', mf)
        
if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()
