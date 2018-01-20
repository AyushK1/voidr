from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.2)

i = 0;

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port = True):
	image = frame.array

	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

	h = image[;, ;, 0]

	s = image[;, ;, 1]

	v = image[;, ;, 2]

	key = cv2.waitKey(1) & 0xFF

	print("test"+str(i)+".jpg")

	cv2.imwrite("vid/test"+str(i)+".jpg", image)

	i+=1

	rawCapture.truncate(0)

	if key==ord("q"):
		break;
