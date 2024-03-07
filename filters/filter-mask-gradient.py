import numpy as np
import cv2 as cv

# Gradient Basic
def gradiant(img):

    # Module Derivate parcial x
    x = np.array([
        [0, 0, 0],
        [0, 1, -1],
        [0, 0, 0]
    ]);
    
    # Module Derivate parcial y
    y = np.array([
        [0, 0, 0],
        [0, 1, 0],
        [0, -1, 0]
    ]);
            
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    grad_x = cv.filter2D(gray, -1, x)
    grad_y = cv.filter2D(gray, -1, y)

    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)

    # grad = cv.addWeighted(abs_grad_x, 0.7, abs_grad_y, 0.2, 0)
    grad_mid = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    return grad_mid

# Gradient Sobel
def gradiant_sobel(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ddepth = cv.CV_16S
    grad_sobel_x = cv.Sobel(gray, ddepth, 1, 0, 3)
    grad_sobel_y = cv.Sobel(gray, ddepth, 0, 1, 3)

    abs_grad_x = cv.convertScaleAbs(grad_sobel_x)
    abs_grad_y = cv.convertScaleAbs(grad_sobel_y)

    # You can change alpha and beta values
    # grad_sobel = cv.addWeighted(abs_grad_x, 0.2, abs_grad_y, 0.7, 0)
    grad_sobel = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    return grad_sobel

# Gradient Prewitt
def gradiant_prewitt(img):    

    # Module Derivate parcial x Prewittt
    x = np.array([
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ]);

    # Module Derivate parcial y Prewitt
    y = np.array([
        [-1, -1, -1],
        [0, 0, 0],
        [1, 1, 1]
    ]);

    grad_x_flip = cv.flip(x, 1)
    grad_y_flip = cv.flip(y, 0)

    # grad_x_flip = x;

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    grad_x = cv.filter2D(gray, -1, grad_x_flip)
    grad_y = cv.filter2D(gray, -1, grad_y_flip)        

    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)  
  
    # grad = cv.addWeighted(abs_grad_x, 0.7, abs_grad_y, 0.2, 0)
    grad_mid = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)    

    return grad_mid

def translation() :
    o_heigth, o_width = img.shape[:2]
    o_dim = (o_width, o_heigth)

    matrix_translation = np.float64([[1,0,100], [0,1,50]])
    translated_img = cv.warpAffine(img, matrix_translation, o_dim)
    cv.imshow('translation', translated_img)

def rotation() :
    #Definy what is the fixed point(center)
    o_heigth, o_width = img.shape[:2]
    o_dim = (o_width, o_heigth)
    scale = 1
    center = (o_width / 2, o_heigth / 2)
    matrix_rotation = cv.getRotationMatrix2D(center, 180, scale)
    rotated_img = cv.warpAffine(img, matrix_rotation, o_dim)
    cv.imshow('rotation', rotated_img)

img = cv.imread('C:\\opencv\\sources\\doc\\images\\lena.png')

# Module Derivate parcial x Roberts
x_roberts = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, -1]
]);

# Module Derivate parcial y Roberts
y_roberts = np.array([
    [0, 0, 0],
    [0, 0, 1],
    [0, -1, 0]
]);


grad = gradiant(img)
grad_roberts = gradiant(img)
grad_sobel = gradiant_sobel(img)
grad_prewitt = gradiant_prewitt(img)

rotation()
# translation()
# cv.imshow('image prewitt', grad_prewitt)
# cv.imshow('image sobel', grad_sobel)
# cv.imshow('image', grad)
# cv.imshow('image roberts', grad_roberts)

while True:
    ch = cv.waitKey()
    if ch == 27:
        break
