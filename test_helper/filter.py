import cv2,os
from scipy import signal
import numpy as np

def sobel(im):
    sobelGx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobelGy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    x_grad = signal.correlate2d(im.copy(),sobelGx,mode='valid')
    y_grad = signal.correlate2d(im.copy(),sobelGy,mode='valid')    
    f = abs(x_grad) + abs(y_grad)
    return x_grad, y_grad, f

def sobelDiagonal(im):
    sobelGx = np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]])
    sobelGy = np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]])
    x_grad = signal.correlate2d(im.copy(),sobelGx,mode='valid')
    y_grad = signal.correlate2d(im.copy(),sobelGy,mode='valid')    
    f = abs(x_grad) + abs(y_grad)
    return x_grad, y_grad, f

def prewitt(im):
    prewittGx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    prewittGy = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
    x_grad = signal.correlate2d(im.copy(),prewittGx,mode='valid')
    y_grad = signal.correlate2d(im.copy(),prewittGy,mode='valid')    
    f = abs(x_grad) + abs(y_grad)
    return x_grad, y_grad, f

def prewittDiagonal(im):
    prewittGx = np.array([[0, 1, 1], [-1, 0, 1], [-1, -1, 0]])
    prewittGy = np.array([[-1, -1, 0], [-1, 0, -1], [0, 1, 1]])
    x_grad = signal.correlate2d(im.copy(),prewittGx,mode='valid')
    y_grad = signal.correlate2d(im.copy(),prewittGy,mode='valid')    
    f = abs(x_grad) + abs(y_grad) 
    return x_grad, y_grad, f

def laplacian(im):
    laplacianGx = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    laplacianGy = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    res1 = signal.correlate2d(im.copy(),sobelGx,mode='valid')
    res2 = signal.correlate2d(im.copy(),sobelGy,mode='valid')    
    return res1, res2

def LoG(im):
    LoG = np.array([[0, 0, -1, 0, 0], [0, -1, -2 -1, 0], [-1, -2, 16, -2, -1], [0, -1, -2, -1, 0], [0, 0, -1, 0, 0]])
    res = signal.correlate2d(im.copy(),LoG,mode='valid')
    return res

im = np.loadtxt('test_helper/a.txt')
a,b,c = sobel(im)
