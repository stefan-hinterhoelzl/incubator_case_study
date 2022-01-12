from CCS811 import sensor_CCS811


print("Hello World!")


sensor = sensor_CCS811()
print("I am done with the sensor")
counter = 0
while counter < 10:
    sensor.update_telemetry()
    counter = counter + 1