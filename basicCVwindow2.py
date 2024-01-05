import numpy as np
import cv2 as cv
import time
cap = cv.VideoCapture(0)
font = cv.FONT_HERSHEY_SIMPLEX

if not cap.isOpened():
    print("Cannot open camera")
    exit()

digit =0    
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    h,w,c = frame.shape
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    #cv.imshow('frame', gray)
    
    digit = digit+1
    print(digit)
    text="data = "+str(digit)
    cv.putText(frame,text,(50,int(h/2)),font,1,(0,0,255),2)
    #time.sleep(1)
    
    
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
