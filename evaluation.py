import os
from urllib import request
import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def compute_psnr(img1, img2):
    img1 = img1.astype(np.float64) / 255.
    img2 = img2.astype(np.float64) / 255.
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return 100
    return 10 * math.log10(1. / mse)

count = 0;

files = os.listdir("prvas")
files.sort()
ref_image = "prvas/referenca.png"
x = list()
y = list()
for file in files:
    if (file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))):
        filepath = os.path.join("prvas", file)
        count = count + 1;

        if (count == 280):
            break;

        with open(filepath, 'rU') as f:
            x.append(count)
            print(filepath)
            img1 = cv2.imread(filepath).astype(np.float64)
            img2 = cv2.imread(ref_image).astype(np.float64)
            print(compute_psnr(img1, img2))
            y.append(compute_psnr(img1, img2))

plt.plot(x, y, color='b', label='simple')
"""
count = 0;

files = os.listdir("zdvema")
files.sort()
ref_image = "zdvema/referenca.png"
x = list()
z = list()
for file in files:
    if (file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))):
        filepath = os.path.join("zdvema", file)
        count = count + 1;


        if (count == 300):
            break;

        with open(filepath, 'rU') as f:
            x.append(count)
            print(filepath)
            img1 = cv2.imread(filepath).astype(np.float64)
            img2 = cv2.imread(ref_image).astype(np.float64)
            print(compute_psnr(img1, img2))
            z.append(compute_psnr(img1, img2))

plt.plot(x, z, color='r', label='compex')
count = 0;

files = os.listdir("brezvsega")
files.sort()
ref_image = "brezvsega/referenca.png"
x = list()
t = list()
for file in files:
    if (file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))):
        filepath = os.path.join("brezvsega", file)
        count = count + 1;


        if (count == 300):
            break;

        with open(filepath, 'rU') as f:
            x.append(count)
            print(filepath)
            img1 = cv2.imread(filepath).astype(np.float64)
            img2 = cv2.imread(ref_image).astype(np.float64)
            print(compute_psnr(img1, img2))
            t.append(compute_psnr(img1, img2))

plt.plot(x, t, color='g', label='none')
"""

plt.xlabel('frame number')
plt.ylabel('PSNR')


plt.title('PSNR for different transfer functions')

plt.legend()
plt.show()
