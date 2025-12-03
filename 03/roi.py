import cv2 as cv

src = cv.imread('../images/lenna.png')

h, w = src.shape[:2]

# ROI - Region of Interest (İlgilenilen Bölge)

img  = src.copy()
roi = img[250:280, 200:400, :]

roi.shape[:2]

cv.imshow('ROI', roi)
cv.waitKey(0)