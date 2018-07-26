# Сопоставление фотографий Прокудина-Горского
# Напишите функцию align, которая сопоставляет изображения с фотографий Прокудина-Горского
# и возвращает координаты точек на синем и красном каналах,
# как это описано в видео, слайдах и описании задания.

# Прототип функции:
# def align(img, g_coord):
#     row_g, col_g = g_coord
#     # считаем сдвиги каналов
#     # сдвигаем точку на зеленом канале
#     # на другие каналы
#     return (row_b, col_b), (row_r, col_r)

from skimage import img_as_float, img_as_uint
import numpy as np

def align(img_, colrow):
    row_g, col_g = colrow[:]

    shift_max = 15    #максимальный сдвиг кадров
    border = 8         #размер рамки в %

    def corr_img(a, b):
    # функция корреляции
        return (a * b).sum()

    def get_shift2(a, b, shift_max):
    # нахождение оптимального свдига b относительно a 
        sh = {}
        for i0 in range(-shift_max, shift_max + 1):
            b1 = np.roll(b, i0, 0)
            for i1 in range(-shift_max, shift_max + 1):
                sh[i0, i1] = corr_img(a, np.roll(b1, i1, 1))
        return max(sh, key=sh.get)

    img = img_as_float(img_)

    img_y, img_x = img.shape    #размеры картинки
    img_y3 = int(img_y / 3)     #высота одного кадра
    brd_y = int(img_y3 * border / 100) #размеры рамки в пикс.
    brd_x = int(img_x * border / 100)

    # вырезаем каналы с учётом рамок из картинки
    b = img[brd_y:img_y3-brd_y, brd_x:img_x-brd_x]
    g = img[img_y3+brd_y:2*img_y3-brd_y, brd_x:img_x-brd_x]
    r = img[2*img_y3+brd_y:3*img_y3-brd_y, brd_x:img_x-brd_x]

    # считаем сдвиги
    gb = get_shift2(b, g, shift_max)
    gr = get_shift2(r, g, shift_max)
 
    return (row_g+gb[0]-img_y3, col_g+gb[1]), (row_g+gr[0]+img_y3, col_g+gr[1])
