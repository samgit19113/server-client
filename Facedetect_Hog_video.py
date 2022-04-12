# import the opencv library
from inspect import formatargvalues
import cv2
import dlib


# define a video capture object
# vid = cv2.VideoCapture('http://admin:idt12345@192.168.1.250/cgi-bin/snapshot.cgi?chn=0&u=admin&p=idt12345')
vid = cv2.VideoCapture("rtsp://admin:idt12345@192.168.0.224:554/cam/realmonitor?channel=1&subtype=1")
    
hogFaceDetector = dlib.get_frontal_face_detector()

def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = hogFaceDetector(gray, 2)
    
    for (i, rect) in enumerate(faces):
        x = rect.left()
        y = rect.top()
        w = rect.right() - x
        h = rect.bottom() - y
        #draw a rectangle
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    return img


while(True):
	
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    img = detect_face(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow('s',img)

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
