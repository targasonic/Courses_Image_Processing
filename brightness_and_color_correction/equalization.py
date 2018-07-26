# Выравнивание гистограммы
# Прочитайте изображение из файла img.png.
# Примените к нему выравнивание гистограммы по алгоритму, описанному в слайдах и видео.
# Работать достаточно в целых числах, помещающихся в байт
# (т.е. изображение конвертировать не нужно).
# Результат сохраните в файл out_img.png.

from skimage.io import imread, imsave
from numpy import histogram, vectorize

img         = imread('img.png')
values, _   = histogram(img, bins=range(257))
cdf         = [sum(values[i] for i in range(x + 1)) for x in range(256)]
cdfmin      = min(x for x in cdf if x > 0)

imsave('out_img.png', vectorize(lambda x: (cdf[x] - cdfmin) / (img.size - 1) * 255)(img).round().astype('uint8'))
