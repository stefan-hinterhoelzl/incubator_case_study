from asyncio.streams import _ClientConnectedCallback
import paho.mqtt.client as mqtt
import time
from CCS811 import sensor_CCS811
import json
from datetime import datetime
from gpiozero import OutputDevice




MQTT_SERVER = "localhost"
MQTT_PATH_PUBLISH = "data"
MQTT_PATH_SUBSCRIBE = "commands"
TIMEOUT = 5
sensor = sensor_CCS811()
heater = OutputDevice(27)
fan = OutputDevice(17)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe(MQTT_PATH_SUBSCRIBE)
    publishData(client)


def publishData(client):
    data = {}
    data["temp"] = sensor.update_telemetry()
    data["H"] = heater.value
    data["L"] = fan.value
    json_data = json.dumps(data)

    print(json_data)

    client.publish(MQTT_PATH_PUBLISH, payload = json_data, qos = 0, retain=False)


def on_message(client, userdata, msg): 
    m_in = json.loads(msg.payload.decode())
    print(m_in)
    #Maybe still change logic of commands here, lets see

    if (m_in["H"] == 1):
        if (heater.value == 0):
            heater.on()
    
    elif (m_in["H"] == 0):
        if (heater.value == 1):
            heater.off()
    
    
    
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