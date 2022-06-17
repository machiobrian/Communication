import random
import time

#import the Paho MQTT client
from paho.mqtt import client as mqtt_client


#set the parameter of the broker connection
#alias the mater connection parameter

broker = 'broker.emqx.io' #set the address
port = 1883 #set the port
topic = "/python/mqtt" #set the topic

#call a python function to randomly generate the MQTT client_id
client_id = f'python-mqtt-{random.randint(0, 1000)}'

username = 'emqx'
password = 'public'

#a connect call back function, called after connecting 
def connect_mqtt():
    def on_connect(client, userdata, flags, rc): #the rc is used to gauge for successful connecting
        if rc == 0:
            print('Connected to MQTT Broker')
        else:
            print('Failed to connect to MQTT, return Code %d\n', rc)

    #set-up the client id
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

#PUBLISH MESSAGE
#mqtt client to send message to the topic

def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg  = f"messages: {msg_count}"
        result = client.publish(topic, msg)

        #result: [0,1]
        status = result[0]
        if status == 0:
            print(f"send '{msg}' to topic '{topic}'")
        else:
            print(f"failed to send messsage to topic '{topic}'")
        msg_count += 1


#SUB MSG

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received '{msg.payload.decode()}' from '{msg.topic}' topic")

        client.subscribe(topic)
        client.on_message = on_message