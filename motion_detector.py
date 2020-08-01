#motion detector
import cv2
# import pandas
# from datetime import datetime# calc time
first_frame = None
# status_list = [None,None] # calc time
# time = [] # calc time
# df = pandas.DataFrame(columns=["start","end"]) # calc time
# video =cv2.VideoCapture("C:\\Users\\rbsathish\Desktop\\THE GODFATHER Theme   CELLO COVER.mp4")
video = cv2.VideoCapture(0)

while True:
    check,frame = video.read()
    # status = 0 # calc time
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(21,21),0)
    if first_frame is None:
        first_frame = blur
        continue
    
    delta_frame = cv2.absdiff(first_frame,gray)
    threshold   = cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_dilate = cv2.dilate(threshold,None,iterations=0)
    (_,cnts,_) = cv2.findContours(thresh_dilate.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    
    for contours in cnts:
        if cv2.contourArea(contours)<10000:
            continue
        # status = 1  # calc time
        (x,y,w,h) = cv2.boundingRect(contours)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    
    # status_list.append(status) # calc time
    
    # status_list = status_list[-2:] # calc time
    
    # if status_list[-1]==1 and status_list[-2]==0:   #calc time
    #     time.append(datetime.now())
        
    # if status_list[-1]==0 and status_list[-2]==1:   #calc time
        # time.append(datetime.now())
        

       
    
    cv2.imshow("frames",frame)
    
    # cv2.imshow("gary",gray)
    
    # cv2.imshow("blur",blur)
    
    # cv2.imshow("thresh_dialate",thresh_dilate)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    
# print(status_list) #calc time
# print(time)    #calc time

# for i in range(0,len(time),2): #CALC TIME   
    # df = df.append({"start":time[i],"end":time[i+1]},ignore_index=True)
# df.to_csv("Times.csv")
video.release()
cv2.destroyAllWindows()    