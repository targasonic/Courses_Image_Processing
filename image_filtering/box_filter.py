# Box-фильтр.
# Реализуйте box-фильтрацию изображения окном 5×5 пикселей. 
# Дополнять изображение не нужно (т.е. изображение после фильтрации уменьшится).
# Прочитайте изображение из файла img.png и сохраните результат фильтрации в файл out_img.png. 

from skimage.io import imread, imsave
#from numpy import shape
import numpy as np
img = imread('img.png')

#img_new = img[ 0:img.shape[0]-4 , 0:img.shape[1] - 4 ]

img_new = np.zeros((img.shape[0]-4, img.shape[1]-4), dtype=np.int)

for i in range (img.shape[0]-4):
    for j in range (img.shape[1]-4):
        
        a = 0
        for k in range (5):
            for n in range (5):
                a = a + img[i + k, j + n]

        img_new [i, j] = int (a / 25)

# Результат сохраните в файл out_img.png.
imsave ('out_img.png', img_new)
