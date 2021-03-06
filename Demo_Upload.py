# -*- coding: utf-8 -*-
"""
Created on Mon May 18 14:11:20 2020

@author: Grover
"""

import os
from skimage import io

os.chdir(r'filepath') #將當前路徑轉至圖片所在的資料夾

outputpath = 'outputfilepath' #合併後的圖要放的路徑以及格式  如：C:\\Users\\username\\output.png

#change

img_1 = io.imread('1st_img_name') #要合併的上圖
img_2 = io.imread('2nd_img_name') #要合併的下圖

img = np.vstack((img_1, img_2)) #合併圖（垂直合併）

io.imsave(outputpath, img) #輸出合併後的圖