import cv2 as cv
import numpy as np

img = cv.imread('../images/lenna.png')
cv.imshow('lenna', img)
cv.waitKey(0)

img_copy = img.copy()

# ROI - Region of Interest (İlgilenilen Bölge)

roi = img[100:400, 100:400]
cv.imshow('ROI', roi)
cv.waitKey(0)


img[0:300, 0:300] = roi
cv.imshow('Modified Image', img)
cv.waitKey(0)

res = cv.resize(roi,None,fx=0.5,fy=0.5,interpolation=cv.INTER_CUBIC)
cv.imshow('Resized ROI', res)
cv.waitKey(0)


