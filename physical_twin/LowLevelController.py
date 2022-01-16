import paho.mqtt.client as mqtt
import time
from CCS811 import sensor_CCS811
import json
from datetime import datetime
#from gpiozero import OutputDevice
import RPi.GPIO as GPIO

try:

    #GPIO Stuff
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)



    MQTT_SERVER = "localhost"
    MQTT_PATH_PUBLISH = "data"
    MQTT_PATH_SUBSCRIBE = "commands"
    TIMEOUT = 5
    sensor = sensor_CCS811()
    HEATER_IS_ON = 0
    FAN_IS_ON = 0



    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        client.subscribe(MQTT_PATH_SUBSCRIBE)
        publishData(client)


    def publishData(client):

        data = {}
        data["temp"] = sensor.update_telemetry()
        data["H"] = HEATER_IS_ON
        data["L"] = FAN_IS_ON
        json_data = json.dumps(data)

        print(json_data)

        client.publish(MQTT_PATH_PUBLISH, payload = json_data, qos = 0, retain=False)


    def on_message(client, userdata, msg): 
        m_in = json.loads(msg.payload.decode())
        print(m_in)
        
        global HEATER_IS_ON
        global FAN_IS_ON

        if (m_in["H"] == 1):
            if (HEATER_IS_ON == 0):
                GPIO.output(15, GPIO.HIGH)
                HEATER_IS_ON = 1
        
        elif (m_in["H"] == 0):
            if (HEATER_IS_ON == 1):
                GPIO.output(15, GPIO.LOW)
                HEATER_IS_ON = 0
        
        

        time.sleep(TIMEOUT)
        publishData(client)


    def on_publish(client, userdata, msg):
        pass




    client = mqtt.Client("client1")
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish = on_publish

    client.username_pw_set(username = "admin", password = "admin")

    client.connect(MQTT_SERVER, 1883, 60)

    client.loop_forever()

except KeyboardInterrupt:
    print("Programm was manually stopped")

finally:
    GPIO.cleanup()