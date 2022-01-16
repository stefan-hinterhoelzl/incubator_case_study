import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

GPIO.output(17, GPIO.LOW)
GPIO.output(27, GPIO.LOW)

print(GPIO.input(17))
print(GPIO.input(27))

GPIO.output(17, GPIO.HIGH)
GPIO.output(27, GPIO.HIGH)

print(GPIO.input(17))
print(GPIO.input(27))