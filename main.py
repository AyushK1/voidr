from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 90
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.2)

i = 0;

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
	for (x, y, w, h) in faces:
		cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)

	cv2.imwrite("vid/test"+str(i)+".jpg", image)

	i+=1

	rawCapture.truncate(0)

	if key==ord("q"):
		break;
