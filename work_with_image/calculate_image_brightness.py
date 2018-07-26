# Подсчет яркости изображения
# Загрузите цветное изображение из файла img.png.
# Подсчитайте яркость этого изображения и сохраните в файл out_img.png.
# Результирующее изображение должно быть одноканальным.
# Для подсчета яркости используйте формулу Y=0.2126⋅R+0.7152⋅G+0.0722⋅B,
# не забудьте сначала перевести изображение в вещественные числа (функция img_as_float),
# а затем в целые числа (функция img_as_ubyte).

from skimage.io import imread, imshow, imsave
from skimage import img_as_float
from skimage import img_as_ubyte

img = imread('img.png')
img_f   = img_as_float(img)

y = 0.2126*img_f[:, :, 0] + 0.7152*img_f[:, :, 1] + 0.0722*img_f[:, :, 2]

img_new_byte = img_as_ubyte(y)

imsave ('out_img.png', img_new_byte)
