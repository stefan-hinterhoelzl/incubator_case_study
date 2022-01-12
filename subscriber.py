import paho.mqtt.client as mqtt

MQTT_SERVER = "localhost"
MQTT_PATH = "commands"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe(MQTT_PATH)

def on_message(client, userdata, msg):
    print(msg.topic + " "+ str(msg.payload))
    #Low Level Driver calls here

client = mqtt.client()
client.on_connect = on_connect
client.on_messages = on_message

client.connect(MQTT_SERVER, 1883, 60)

client.loop_forever()