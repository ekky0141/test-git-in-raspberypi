import cv2 as cv
import numpy as np;
##import time
img = cv.imread('football.jpg')
h,w,c=img.shape
font = cv.FONT_HERSHEY_SIMPLEX
text = 'Mtt'
cv.putText(img,text,(int(w/2),int(h/2)),font,0.5,(0,0,255),2)
cv.putText(img,'Kmutnb',(100,50),font,1,(255,0,0),2)
cv.imshow('jhjjj',img)
cv.waitKey(0)




cv.destroyAllWindows()
