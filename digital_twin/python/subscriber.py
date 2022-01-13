import paho.mqtt.client as mqtt
import logging

MQTT_SERVER = "192.168.11.15"
MQTT_PATH = "data"

logging.basicConfig(filename="D:\Repos\incubator_case_study\incubator_case_study\digital_twin\python\subscriberdata.log", encoding="utf-8", level=logging.DEBUG)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe(MQTT_PATH)

def on_message(client, userdata, msg):
    logging.info(msg.topic + ": "+ msg.payload.decode())
    print(msg.topic + ": "+ msg.payload.decode())

    
    #Low Level Driver calls here

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username = "admin", password = "admin")

client.connect(MQTT_SERVER, 1883, 60)

client.loop_forever()