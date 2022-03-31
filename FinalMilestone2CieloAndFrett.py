import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    #Capture frame by fream
    ret, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    #if frame is read correctly, ret is True
    if not ret:
    	print("Cannot receive frame. Exiting...")
    	break
    #The operations on the frame come here
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #Display the resulting frame
    cv.imshow('frame', frame)
    #setting values for base colors
    b = frame[:,:,:1]
    g = frame[:,:,1:2]
    r = frame[:,:,2:]

    #computing the mean
    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)

    #make the camera track red objects
    sensitivity = 15
    lower_red_0 = np.array([0, 100, 100]) 
    upper_red_0 = np.array([sensitivity, 255, 255])
    lower_red_1 = np.array([180 - sensitivity, 100, 100]) 
    upper_red_1 = np.array([180, 255, 255])
    
    mask_0 = cv.inRange(hsv, lower_red_0 , upper_red_0);
    mask_1 = cv.inRange(hsv, lower_red_1 , upper_red_1 );

    mask = cv.bitwise_or(mask_0, mask_1)
    res = cv.bitwise_and(frame,frame, mask= mask)

    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    
    #displaying the most prominent color
    """if (b_mean > g_mean and b_mean > r_mean):
        print("Blue")
    if (g_mean > r_mean and g_mean > b_mean):
        print("Green")
    else:
        print("Red")"""
    if cv.waitKey(1) == ord('q'):
    	break

#When everything is done, release the capture
cap.release()
cv.destroyAllWindows()


    
