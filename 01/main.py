# Renk uzaylarının değiştirilmesi

import cv2 as cv
import numpy as np

img = cv.imread('../images/lenna.png')
cv.imshow('lenna', img)
cv.waitKey(0)


# to gray

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
cv.waitKey(0)


hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)
cv.waitKey(0)


# Geometrik Dönüşümler

rows, cols, channels = img.shape
print(rows)
print(cols)
print(channels)


# shifting


M = np.float32([[1, 0, 300], [0, 1, 90]])
shifted = cv.warpAffine(img, M, (cols, rows))
cv.imshow('shifted', shifted)
cv.waitKey(0)


# rotation

M = cv.getRotationMatrix2D((cols/2, rows/2), 90, 1)
rotated = cv.warpAffine(img, M, (cols, rows))
cv.imshow('rotated', rotated)
cv.waitKey(0)


# scaling

res = cv.resize(img,None, fx=0.4, fy=0.4, interpolation=cv.INTER_CUBIC)
cv.imshow('res', res)
cv.waitKey(0)

rows, cols, channels = res.shape
M = cv.getRotationMatrix2D((cols/2, rows/2), 90, 1)
rotated = cv.warpAffine(res, M, (cols, rows))
cv.imshow('rotated_res', rotated)
cv.waitKey(0)

