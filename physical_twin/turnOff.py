import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

GPIO.output(14, GPIO.LOW)
GPIO.output(15, GPIO.LOW)

print(GPIO.input(14))
print(GPIO.input(15))

GPIO.output(14, GPIO.HIGH)
GPIO.output(15, GPIO.HIGH)

print(GPIO.input(14))
print(GPIO.input(15))

GPIO.cleanup()