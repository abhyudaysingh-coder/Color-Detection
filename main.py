import cv2
from PIL import Image
from util import get_limits
#color in BGR format
#purple - (255, 0, 255)
#green - (0, 255, 0)
color = (0, 255, 0)
#starting the webcam
cam = cv2.VideoCapture(0)
#loop to get continous frames 
while True:
    #reading a spontaneous frame 
    ret , frame = cam.read()
    #converting frame from BGR to HSV
    hsvframe = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
    #ysing our custom function for lower and upper limits for the color
    lower , upper = get_limits(color)
    # creating a binary mask from hsv
    mask = cv2.inRange(hsvframe , lower , upper)
    #converting mask into PIL for bounding box
    mask_real = Image.fromarray(mask)
    #creating the bounding box
    bbox = mask_real.getbbox()
    if bbox is not None:
        # left top right bottom
        x1, y1, x2, y2 = bbox
        # plot the box on the frame
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imshow('color detector' , frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#releasing the webcam and closing all windows
cam.release()
cv2.destroyAllWindows()
