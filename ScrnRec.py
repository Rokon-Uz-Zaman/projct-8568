import cv2
import numpy as np
from PIL import ImageGrab


while True:
    shot=ImageGrab.grab(bbox=(0,0,1280,720))
    imgNp=np.array(shot)
    cv2.imshow("shotImg",imgNp)
    cv2.waitKey(10)