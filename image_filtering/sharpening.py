# Повышение резкости изображения.
# Реализуйте повышение четкости изображения путём фильтрации изображения с ядром
# 110 ⎡ ⎣ ⎢−1−2−1−222−2−1−2−1⎤ ⎦ ⎥ .
# При подсчете новых значений изображения не забывайте обрезать их с помощью numpy.clip.
# Дополнять изображение не нужно (т.е. изображение после фильтрации уменьшится).
# Прочитайте изображение из файла img.png и сохраните результат фильтрации в файл out_img.png.

from numpy import array, clip
from skimage.io import imread, imsave

img = imread('img.png')
out_img = array([[[0] * img.shape[1]] * img.shape[0]], dtype='float')[0]

G = array([[-1, -2, -1], [-2, 22, -2], [-1, -2, -1]]) / 10

for i in range(3, img.shape[0] + 1):
    for j in range(3, img.shape[1] + 1):
        out_img[i - 3, j - 3] = (img[i-3: i, j-3: j] * G).sum()

imsave('out_img.png', clip(out_img[: - 2, : - 2], 0, 255).astype('uint8'))
