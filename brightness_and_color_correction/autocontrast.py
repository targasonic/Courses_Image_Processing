# Автоконтраст черно-белого изображения
# Прочитайте изображение из файла img.png.
# Примените к нему линейное выравнивание яркости: примените к каждому пикселю функцию

from skimage.io import *

img = imread('img.png')
x_min, x_max = img.min(), img.max()
img_out = ((img - x_min) * (255 / (x_max - x_min))).astype('uint8')
imsave('out_img.png',img_out)
