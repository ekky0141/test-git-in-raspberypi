import cv2 as cv
import numpy as np;
##import time
img = cv.imread('football.jpg')
h,w,c=img.shape
font = cv.FONT_HERSHEY_SIMPLEX
text = 'Mtt'
cv.putText(img,text,(int(w/2),int(h/2)),font,0.5,(0,0,255),2)
cv.putText(img,'Kmutnb',(100,50),font,1,(255,0,0),2)
#cv.imshow('jhjjj',img)



digit =0

digit = digit+1
print(digit)
img = cv.imread('football.jpg')
h,w,c = img.shape
print(h)
print(w)
print(c)
text = "data = "+" xx = " + str(digit)
print(text)
cv.putText(img, text, (int(w/2),int(h/2)), font, 0.5, (0, 0, 255), 2)
p0=10,10
p1=int(w/2),int(h/2)
cv.line(img,p0,p1,(255, 0, 255),2)
    
p2=int(w/2),int(h/2)
p3=int(w/2)+50,int(h/2)+50
cv.rectangle(img,p2,p3,(255, 0, 25),cv.FILLED)
#cv.imshow('before',img)
cv.imshow('after',img)
    
while(True):   
    k=cv.waitKey(0)
   
   
   
   
   
   
   
    if k == ord('q'):
        break
    
    elif k == ord('v'):
        img = cv.flip(img,1) 
        
      
    elif k == ord('h'):
        img = cv.flip(img,0) 
       
    
    cv.imshow('after',img)
    # cv.imwrite('test.jpg',img)
    # gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    # cv.imwrite('test.jpg',gray)
    # cv.imshow('Mechatronics Frame1',gray)
cv.waitKey(0)
cv.destroyAllWindows()
#time.sleep(5)
