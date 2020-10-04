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

im = np.loadtxt('test_helper/a.txt')
a,b,c = sobel(im)