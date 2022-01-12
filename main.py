from CCS811 import sensor_CCS811
import time

print("Hello World!")


sensor = sensor_CCS811()
print("I am done with the sensor")
#hallo

for x in range(10):
    sensor.update_telemetry()
    time.sleep(1)