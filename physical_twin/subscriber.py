import paho.mqtt.client as mqtt
import logging
from gpiozero import OutputDevice

MQTT_SERVER = "localhost"
MQTT_PATH = "commands"

heater = OutputDevice(27)
fan = OutputDevice(17)


logging.basicConfig(filename="home/pi/Documents/incubator_case_study/physical_twin/logging.log", encoding="utf-8", level=logging.DEBUG)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe(MQTT_PATH)

def on_message(client, userdata, msg):
    logging.info(msg.topic + ": "+ msg.payload.decode())

    message = msg.payload.decode()

    if (message == "HEATER: ON"):
        if (heater.value == 0):
            heater.on()

    
    elif (message == "HEATER: OFF"):
        if (heater.value == 1):
            heater.off()
       

client = mqtt.Client("client2")
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username = "admin", password = "admin")

client.connect(MQTT_SERVER, 1883, 60)

client.loop_forever()