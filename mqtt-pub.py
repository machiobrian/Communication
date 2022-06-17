import os
from paho import mqtt_client as paho

client = paho.Client()

if client.connect("localhost", 1883, 60) != 0:
    print("Not Connected to Mqtt broker")
    os.exit(-1)

client.publish("test/status", "Hello machio from pao-mqtt", 0) #QoS=0
client.disconnect()

