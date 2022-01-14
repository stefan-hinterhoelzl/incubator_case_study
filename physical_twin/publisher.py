import paho.mqtt.client as mqtt
import logging
import time
from CCS811 import sensor_CCS811


MQTT_SERVER = "localhost"
MQTT_PATH = "data"


logging.basicConfig(filename="home/pi/Documents/incubator_case_study/physical_twin/publish.log", encoding="utf-8", level=logging.DEBUG)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    while True:
        message = sensor_CCS811.update_telemetry()
        client.publish(MQTT_PATH, message)
        time.sleep(1)


def on_publish(client, userdata, msg):
    logging.info(msg.topic + ": "+ msg.payload.decode())

client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

client.username_pw_set(username = "admin", password = "admin")

client.connect(MQTT_SERVER, 1883, 60)

client.loop_forever()