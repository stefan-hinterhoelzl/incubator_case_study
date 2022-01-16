import paho.mqtt.client as mqtt
import time
from CCS811 import sensor_CCS811
import json
from datetime import datetime
#from gpiozero import OutputDevice
import RPi.GPIO as GPIO

#GPIO Stuff
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)



MQTT_SERVER = "localhost"
MQTT_PATH_PUBLISH = "data"
MQTT_PATH_SUBSCRIBE = "commands"
TIMEOUT = 5
sensor = sensor_CCS811()



def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe(MQTT_PATH_SUBSCRIBE)
    publishData(client)


def publishData(client):
    heater_is_on = GPIO.input(27)
    fan_is_on = GPIO.input(17)

    print(heater_is_on)
    print(fan_is_on)

    data = {}
    data["temp"] = sensor.update_telemetry()
    data["H"] = GPIO.input(27)
    data["L"] = GPIO.input(17)
    json_data = json.dumps(data)

    print(json_data)

    client.publish(MQTT_PATH_PUBLISH, payload = json_data, qos = 0, retain=False)


def on_message(client, userdata, msg): 
    m_in = json.loads(msg.payload.decode())
    print(m_in)
    #Maybe still change logic of commands here, lets see

    if (m_in["H"] == 1):
        if (GPIO.input(27) == 0):
            GPIO.output(27, GPIO.HIGH)
    
    elif (m_in["H"] == 0):
        if (GPIO.input(27) == 1):
           GPIO.output(27, GPIO.LOW)
    
    

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