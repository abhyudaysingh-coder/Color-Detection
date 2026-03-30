import numpy as np
import cv2

def get_limits(color):
    #convert bgr into 3d array
    c = np.uint8([[color]])
    #convert bgr array into hsv
    hsvc = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    #defining the upper and lower limits
    hue = hsvc[0][0][0]

    lowerLimit = (max(hue - 10, 0), 50, 50)
    upperLimit = (min(hue + 10, 179), 255, 255)
    #converting python tuple into array of uint8
    lower = np.array(lowerLimit , dtype=np.uint8)
    upper = np.array(upperLimit , dtype=np.uint8)
    return lower, upper

    