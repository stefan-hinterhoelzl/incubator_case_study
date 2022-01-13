import paho.mqtt.client as mqtt
import sys

MQTT_SERVER = "localhost"
MQTT_PATH = "commands"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe(MQTT_PATH)

def on_message(client, userdata, msg):
    #print(msg.topic + ": "+ msg.payload.decode())
    sys.stdout.write(msg.topic + ": "+ msg.payload.decode())
    sys.stdout.flush()
    #Low Level Driver calls here

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username = "admin", password = "admin")

client.connect(MQTT_SERVER, 1883, 60)

client.loop_forever()