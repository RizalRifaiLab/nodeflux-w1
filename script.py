#!/usr/bin/env python
# coding: utf-8

# In[13]:


import cv2
# Create a video capture object, in this case we are reading the video from a file

#if using webcam as input
#vid_capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#if using vidio as input
vid_capture = cv2.VideoCapture("test.mp4")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

if (vid_capture.isOpened() == False):  
  print("Error opening the video file")
  # Read fps and frame count
else:
    # Get frame rate information
    # You can replace 5 with CAP_PROP_FPS as well, they are enumerations
    fps = vid_capture.get(5)
    print('Frames per second : ', fps,'FPS')
    # Get frame count
    # You can replace 7 with CAP_PROP_FRAME_COUNT as well, they are enumerations
    frame_count = vid_capture.get(7)
    print('Frame count : ', frame_count)
 
while(vid_capture.isOpened()):
  # vid_capture.read() methods returns a tuple, first element is a bool
  # and the second is frame
  ret, frame = vid_capture.read()
  warna = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
  face = face_cascade.detectMultiScale(warna,2,5)
  if ret == True:
    for (x,y,w,h) in face :
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 3)
        muka = warna[y : y+h, x: x+w]
    cv2.imshow('Frame',frame)
    # 20 is in milliseconds, try to increase the value, say 50 and observe
    key = cv2.waitKey(1)
    if key == ord('q'):
      break
  else:
    break
 
# Release the video capture object
vid_capture.release()
cv2.destroyAllWindows()


# In[14]:


help(face_cascade.detectMultiScale)


# In[ ]:




