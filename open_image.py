import cv2 

img = cv2.imread('DATA/00-puppy.jpg')

while True: 
    
    cv2.imshow('Puppy',img)
   
    # if wait 1 second & Esc key pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.waitKey()