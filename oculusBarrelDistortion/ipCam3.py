import cv2
import urllib 
import numpy as np

stream=urllib.urlopen('http://robot:robot1234@192.168.1.160:80/mjpg/video.mjpg')
bytes=''
while True:
    bytes+=stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        print(type(i))
        cv2.imshow('i',i)
        if cv2.waitKey(1) ==27:
            exit(0)   
