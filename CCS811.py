import adafruit_ccs811
import busio
import board
import time

class sensor_CCS811:

    def __init__(self):
        # initialize sensor values
        self.temperature = 0.0
        self.eco2 = 0.0
        self.tvoc = 0.0

        # initialize i2c
        i2c = busio.I2C(board.SCL, board.SDA)
        adafruit_ccs811.setDriveMode(0x01)
        self.sensor = adafruit_ccs811.CCS811(i2c)
        print("waiting to initialize")
        # wait for the sensor to be ready and calibrate the thermistor
        while not self.sensor.data_ready:
            pass

        print("initialized")
        # assign temperature offset
        # temp = self.sensor.temperature
        # self.sensor.temp_offset = temp - 25.0


    def update_telemetry(self):
        self.temperature = self.sensor.temperature
        print("tempereatur: " , self.temperature)