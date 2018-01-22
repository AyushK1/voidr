import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

channels = [5, 6, 13, 26]

GPIO.setup(channels, GPIO.OUT)

GPIO.output(channels, 1)
