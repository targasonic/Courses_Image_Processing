# Гауссовская фильтрация.
# Профильтруйте изображение гауссовским ядром с $\sigma=0.66$.
# Для подсчета ядра используйте функцию из предыдущего задания. 
# При подсчете новых значений изображения не забывайте обрезать их с помощью numpy.clip. 
# Дополнять изображение не нужно (т.е. изображение после фильтрации уменьшится). 
# Изображение прочитайте из файла img.png, результат сохраните в файл out_img.png.


from skimage.io import imread, imsave, imshow
from math import pi, exp
import numpy as np
from numpy import array
from scipy.signal import convolve2d

def gauss(x, y):
    return 1 / (2 * pi * 0.66 ** 2) * exp((-x ** 2 - y ** 2) / (2 * 0.66 ** 2))

k            = 5     # size of filter core
gauss_kernel = np.array([[gauss(i-k//2, j-k//2) for j in range(k)] for i in range(k)])
gauss_kernel = (gauss_kernel / gauss_kernel.sum())

img      = imread('img.png')

img_new = convolve2d(img, gauss_kernel / gauss_kernel.sum(), mode='valid').astype('uint8')

imsave ('out_img.png', img_new)

