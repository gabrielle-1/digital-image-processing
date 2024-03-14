import cv2 as cv
import numpy as np

dados=np.array([1,2,2,3,4,5,5])

img = cv.imread('C:\\opencv\\sources\\samples\\data\\mergulhador.jpg')
height, width = img.shape[:2] 

print("The height of the image is: ", height) 
print("The width of the image is: ", width) 
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #converte P&B
pixels_img = {};

for y in range(0, height):
 for x in range(0, width):
    pixel = img[x,y]
    pixels_img[pixel] = pixel
    # img[y, x] = (255,255,255)

cv.imshow("Imagem modificada", img)
print(pixels_img)
while True:
    ch = cv.waitKey()
    if ch == 27:
        break




