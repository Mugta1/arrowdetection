import cv2 as cv
import numpy as np
import math

global frameWidth
frameWidth = 640
global frameHeight
frameHeight = 480

def nothing(x):
     pass

#a function to find distance
def dist(pt1, pt2):
     distance=((pt1[0]-pt2[1])**2+(pt1[0]+pt2[1])**2)**0.5
     return distance
     
#function to find angle

def FindAngle(pt1, pt2):
     y1=pt1[1]
     y2=pt2[1]
     x1=pt1[0]
     x2=pt2[0]
     

     angRadians = math.asin((y1-y2)/((((x1-x2)**2)+((y1-y2)**2))**0.5)) #mathematical formula

     angle = round(math.degrees(angRadians)) #convert angle from radians to degrees

     return angle


#reading the video and resizing it
vid=cv.VideoCapture(0)
vid.set(3, frameWidth) #sets width of frame as frameWidth(640)
vid.set(4, frameHeight) #sets height of frame as frameHeight(480)
vid.set(10,150) #brightness level


#create a trackerbar that can be used to change the thresholding(diff light conditions)
cv.namedWindow('Adjust')
cv.createTrackbar("min", "Adjust", 110, 255, nothing)
while True:
     ret ,frame = vid.read()
     frame = cv.resize(frame, (640,480), interpolation=cv.INTER_AREA)
     #image processing
     cropped = frame[100:400,100:500]
     temp = cropped
     cropped = cv.cvtColor(cropped, cv.COLOR_BGR2GRAY)
     mi = cv.getTrackbarPos("min","Adjust")
     _,threshold = cv.threshold(cropped,mi,255,cv.THRESH_BINARY)
     kernal = np.zeros([10,10],np.uint8)
     erode = cv.erode(threshold,kernal)
     cntrs,_=cv.findContours(threshold,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
     #detecting arrows
     for cnt in cntrs:
          area=cv.contourArea(cnt)
          if area>5000:  
            peri = cv.arcLength(cnt, True) #calculate perimeter of outline
            approx = cv.approxPolyDP(cnt, 0.01*peri, True) #gives corners of the mask
            objCor = len(approx)
            
            if objCor==7:
               hull = cv.convexHull(approx, returnPoints=True)
               x,y,w,h=cv.boundingRect(approx)
               cv.rectangle(temp,(x,y),(x+w,y+h),(0,255,255),4)
               difference = [x for x in approx if x not in hull]
               if len(difference)>=1:
                        
                    imp = np.concatenate(difference, axis=0)
                    if len(imp)==2:   
                         pt1=imp[0]
                         pt2=imp[1]
                         Anglefromvertical=FindAngle(pt1, pt2)                                       
                         print(Anglefromvertical)
                         cv.putText(temp, "Angle:"+str(Anglefromvertical), (frameWidth//4,frameHeight//4), cv.FONT_HERSHEY_COMPLEX,1.5,(255,255,0),2) #display angle
     cv.imshow('temp', temp)
     cv.imshow('processing', erode)
     if cv.waitKey(1) & 0xFF == ord('q'):
          break
     
vid.release()
cv.destroyAllWindows()
               
                    
               
               
                