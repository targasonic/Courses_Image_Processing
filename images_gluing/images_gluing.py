from skimage.io import imread, imsave, imshow
from skimage.transform import resize
import numpy as np
from numpy.fft import fft2, fftshift
import matplotlib.pyplot as plt
from math import pi, exp
from numpy import array
from scipy.signal import convolve2d
from skimage import img_as_ubyte

#-----------------------------
sigma   = 0.66
k       = round(6 * sigma) + 1
n_layer = 5
#-----------------------------
def gauss(x, y, sigma):
    return 1 / (2 * pi * sigma ** 2) * exp((-x ** 2 - y ** 2) / (2 * sigma ** 2))
gauss_kernel = np.array([[gauss(i-k//2, j-k//2, sigma) for j in range(k)] for i in range(k)])
#-----------------------------
def add_borders(img):
   w       = int((k-1)/2)
   border  = np.array([[img[w-i,j] for j in range(img.shape[1])] for i in range(w)])
   border2 = np.array([[img[img.shape[0]-1-i,j] for j in range(img.shape[1])] for i in range(w)])
   img     = np.vstack((np.vstack((border, img)), border2))      
   border  = np.array([[img[i,w-j] for j in range(w)] for i in range(img.shape[0])])
   border2 = np.array([[img[i,img.shape[1]-1-j] for j in range(w)] for i in range(img.shape[0])])
   img     = np.hstack((np.hstack((border, img)), border2))   
   return img
#-----------------------------
def gauss_pyramid (img, sigma, n_layer):
    i_g   = []
    i_g.append(img)
    for i in range (1, n_layer+1, 1):
        i_g.append(convolve2d(add_borders(i_g[i-1]), gauss_kernel / gauss_kernel.sum(), mode='valid'))
    return i_g
#-----------------------------
def img_freq (img):
    return np.log(1 + abs(fftshift(fft2(img))))
#-----------------------------
def laplas_pyramid (img, sigma, n_layer):
    i_g = gauss_pyramid(img , sigma, n_layer)
    i_l = []
    for i in range (0, n_layer, 1):
        i_l.append(i_g[i] - i_g[i+1])
    i_l.append(i_g[n_layer])
    return i_l
#-----------------------------
def prinf_pyramid (pyr):
    for i in range (0, len(pyr), 1):
        fig, (ax0, ax1) = plt.subplots(1, 2)
        ax0.imshow(pyr[i], cmap='gray')
        ax1.imshow(img_freq(pyr[i]), cmap ='gray')
#-----------------------------
def generate_new_img_layers (img1_l, img2_l, img_mask_g, n_layer):
    img_new_layers = []
    for i in range (0, n_layer+1, 1):
        img_new_layers.append(img_mask_g[i+1]*img1_l[i] + (1- img_mask_g[i+1])*img2_l[i])
    return img_new_layers
#----------------------------
def generate_new_img (img_new_layers):
    img_new = img_new_layers[0]
    for i in range (1, len(img_new_layers), 1):
        img_new = img_new + img_new_layers[i]
    return img_new
#----------------------------
def img_merger (img1, img2, img_mask):
    img_mergered = []
    img1_l      = laplas_pyramid (img1, sigma, n_layer)
    img2_l      = laplas_pyramid (img2, sigma, n_layer)
    img_mask_g  = gauss_pyramid(img_mask, sigma, n_layer+1)
    img_new_layers  = generate_new_img_layers (img1_l, img2_l, img_mask_g, n_layer)
    img_mergered.append(generate_new_img (img_new_layers))
    for i in range (1, len(img_new_layers), 1):
         img_mergered.append(img_new_layers[i])
    return img_mergered
    

img1   = imread('a.png')
img2   = imread('b.png')
img_mask  = imread('mask.png').astype(np.uint8) #(np.float32)
img1  = img1[:,:,0]
img2  = img2[:,:,0]
img_mask  = img_mask[:,:,0]

fig, (ax0, ax1, ax2) = plt.subplots(1, 3)
ax0.imshow(img1, cmap='gray')
ax1.imshow(img_mask, cmap ='gray')
ax2.imshow(img2, cmap ='gray')


img_new = img_merger (img1, img2, img_mask)
#prinf_pyramid (img_new)

fig, (ax0, ax1, ax2) = plt.subplots(1, 3)
ax0.imshow(img_new, cmap='gray')
ax1.imshow(img_mask, cmap ='gray')
ax2.imshow(img2, cmap ='gray')
