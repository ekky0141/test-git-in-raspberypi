import cv2 as cv
import numpy as np;
import time

font = cv.FONT_HERSHEY_SIMPLEX

img = cv.imread('cat.jpg')
h,w,c = img.shape
print(h)
print(w)
print(c)
digit = 2

text = "data = "+" xx = " + str(digit)
print(text)
cv.putText(img, text, (int(w/2),int(h/2)), font, 0.5, (0, 0, 255), 2)

cv.imshow('Mechatronics Frame',img)

cv.imwrite('test.jpg',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imwrite('test.jpg',gray)
cv.imshow('Mechatronics Frame1',gray)


cv.waitKey(0)
cv.destroyAllWindows()