import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    #Capture frame by fream
    ret, frame = cap.read()

	
    #if frame is read correctly, ret is True
    if not ret:
    	print("Cannot receive frame. Exiting...")
    	break
    #The operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
    	break

#When everything is done, release the capture
cap.release()
cv.destroyAllWindows()

#taking the input from the webcam
vid = cv2.VideoCapture(0)

#running while loop just to make sure that
#our program keep running until we stop it
while True:
    #capturing the current frame
    _, frame = vid.read()

    #displaying the current frame
    cv2.imshow("frame", frame)

    #setting values for base colors
    b = frame[:, :, :1]
    g = frame[:, :, 1:2]







