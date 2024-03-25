import numpy as np
import cv2 as cv
import sys

def get_limiar(image_array: list) -> float:
    t_ref = 0

    # Select an estimated value for T (midpoint between the minimum and maximum values of an image)
    levels = np.unique(image_array)
    t_value = (levels[0] + levels[-1]) / 2
    t_value_ant = t_ref

    iterations = 0

    while ((t_value - t_value_ant) != t_ref):
        # Segment the image using T
        left = []
        rigth = []

        for line in range(0, len(image_array)):
            for col in range(0, len(image_array[line])):
                if (image_array[line][col] < t_value).any():
                    left.append(image_array[line][col])
                else:
                    rigth.append(image_array[line][col])

        # Calculate the average of the pixel intensities in each region
        mean_left = np.mean(left) if left else 0
        mean_rigth = np.mean(rigth) if rigth else 0

        # Calculate the new value of T
        t_value_ant = t_value
        t_value = (mean_left + mean_rigth) / 2

        iterations +=1
        print(f"Iteration: {iterations}, T Value: {t_value}, Mean Left: {mean_left}, Mean Rigth: {mean_rigth}")
    
    return t_value


def main():
    
    img = cv.imread('C:\\opencv\\sources\\samples\\data\\ancora.jpg')
    if img is None:
        print('Não localizei a imagem:', img)
        sys.exit(1)    

            
    while True:
        ch = cv.waitKey()
        if ch == 27:
            break

        cv.imshow('Image Original', img)

        limiar = get_limiar(img)
        for row in range(img.shape[0]):
            for col in range(img.shape[1]):
                if (img[row][col] > limiar).any():
                    img[row][col] = 255
                else:
                    img[row][col] = 0

        cv.imshow('Image Segmentation', img)

        
if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()
