# import RPi.GPIO as GPIO
from gpiozero import OutputDevice
import time
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.setup(18,GPIO.OUT)
# print("LED on")
# GPIO.output(18,GPIO.HIGH)
# time.sleep(3)
# print("LED off")
# GPIO.output(18,GPIO.LOW)

print("running")
heater = OutputDevice(27)
print("heater on:")
heater.on()
print("sleeping...")
time.sleep(30)
print("heater off:")
heater.off()