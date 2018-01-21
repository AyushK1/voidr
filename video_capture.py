from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
camera = PiCamera()

camera.resolution = (800, 600)
camera.framerate = 90
rawCapture = PiRGBArray(camera, size=(800, 600))

#Prepare camera
time.sleep(0.2)
#do setup
i = 0
dx = 0
currentPos = 0
prevPos = 0
criticalPos = 36
averageFaceWidth = 6.5
#0 is travel straight, 1 is avoid
state = 0

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port = True):
	image = frame.array

	faceCascade = cv2.CascadeClassifier("classifiers/haarcascade_frontalface_default.xml")

	key = cv2.waitKey(1) & 0xFF

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	#Apply classifier
	faces = faceCascade.detectMultiScale(
    		gray,
    		scaleFactor=1.2,
    		minNeighbors=5,
    		minSize=(30, 30),
    		flags = cv2.cv.CV_HAAR_SCALE_IMAGE
	)
	#Draw bounding boxes
	if (len(faces) != 0):
		x, y, w, h = faces[0]
		cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)
		currentPos = (2714 * averageFaceWidth)/w
		dx = currentPos - prevPos
		if (currentPos <= criticalPos):
			state = 1;
		prevPos = currentPos

	if (state == 1):
		#
	else:
		#



	i+=1

	rawCapture.truncate(0)
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.resolution = (1600, 900)
camera.framerate = 90
rawCapture = PiRGBArray(camera, size=(1600, 900))

time.sleep(0.2)

i = 0;
dx = [0,0]
prev = []

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port = True):
	image = frame.array

	faceCascade = cv2.CascadeClassifier("classifiers/haarcascade_frontalface_default.xml")

	key = cv2.waitKey(1) & 0xFF

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	#Apply classifier
	faces = faceCascade.detectMultiScale(
    		gray,
    		scaleFactor=1.2,
    		minNeighbors=5,
    		minSize=(30, 30),
    		flags = cv2.cv.CV_HAAR_SCALE_IMAGE
	)
	#Draw bounding boxes
	if (len(faces) != 0):
		x, y, w, h = faces[0]
		cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)

	cv2.imwrite("vid/test"+str(i)+".jpg", image)

	i+=1

	rawCapture.truncate(0)

	if key==ord("q"):
		break;
