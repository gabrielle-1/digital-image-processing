import numpy as np
import cv2 as cv

# Gradient Basic
def gradiant(x, y, img):
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
def gradiant_prewitt(x, y, img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    grad_x = cv.filter2D(gray, -1, x)
    grad_y = cv.filter2D(gray, -1, y)

    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)    

    # grad = cv.addWeighted(abs_grad_x, 0.7, abs_grad_y, 0.2, 0)
    grad_mid = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

    flipped_img = cv.flip(grad_mid, 0)

    return flipped_img


img = cv.imread('C:\\opencv\\sources\\doc\\images\\lena.png')

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

# Module Derivate parcial x Prewittt
x_prewit = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
]);

# Module Derivate parcial y Prewitt
y_prewit = np.array([
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
]);

grad = gradiant(x, y, img)
grad_roberts = gradiant(x_roberts, y_roberts, img)
grad_sobel = gradiant_sobel(img)
grad_prewitt = gradiant_prewitt(x_prewit, y_prewit)

cv.imshow('image prewitt', grad_prewitt)
# cv.imshow('image sobel', grad_sobel)
# cv.imshow('image', grad)
# cv.imshow('image roberts', grad_roberts)

while True:
    ch = cv.waitKey()
    if ch == 27:
        break
