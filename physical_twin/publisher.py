import paho.mqtt.client as mqtt
import logging
import time
from CCS811 import sensor_CCS811


MQTT_SERVER = "localhost"
MQTT_PATH = "data"
sensor = sensor_CCS811()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    message = sensor.update_telemetry()
    print(message)
    client.publish(MQTT_PATH, payload = message, qos = 0, retain=False)


def on_publish(client, userdata, msg):
    print("message_sent")

client = mqtt.Client("client1")
client.on_connect = on_connect
client.on_publish = on_publish

client.username_pw_set(username = "admin", password = "admin")

client.connect(MQTT_SERVER, 1883, 60)

client.loop_forever()