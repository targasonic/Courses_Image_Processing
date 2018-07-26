# Поменять местами каналы изображения
# Загрузите изображение из файла img.png.
# У этого изображения поменяйте местами каналы так,
# чтобы вместо порядка RGB каналы шли в порядке BRG.
# Сохраните изображение с измененными каналами в файл out_img.png.

from skimage.io import imread, imsave
import numpy as np
img = imread('img.png')
img[:,:, [0, 1, 2]] = img[:, :, [2, 0, 1]]
imsave('out_img.png', img)
