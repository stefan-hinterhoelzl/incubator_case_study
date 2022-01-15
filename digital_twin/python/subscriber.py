import paho.mqtt.client as mqtt
import logging

MQTT_SERVER = "192.168.11.15"
MQTT_PATH_SUBSCRIBE = "data"
MQTT_PATH_PUBLISH = "commands"
LOWERBOUND = 25
HIGHERBOUND = 35


logging.basicConfig(filename="D:\Repos\incubator_case_study\incubator_case_study\digital_twin\python\subscriberdata.log", encoding="utf-8", level=logging.DEBUG)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe(MQTT_PATH_SUBSCRIBE)

def on_message(client, userdata, msg):
    logging.info(msg.topic + ": "+ msg.payload.decode())
    print(msg.topic + ": "+ msg.payload.decode())
    
    if (msg.payload.decode() < LOWERBOUND):
        client.publish(MQTT_PATH_PUBLISH, payload = "HEATER: ON", qos = 0, retain=False)
    elif (msg.payload.decode() > HIGHERBOUND):
        client.publish(MQTT_PATH_PUBLISH, payload = "HEATER: OFF", qos = 0, retain=False)
    

def on_publish(client, userdata, msg):
    print("command sent")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

client.username_pw_set(username = "admin", password = "admin")

client.connect(MQTT_SERVER, 1883, 60)

client.loop_forever()