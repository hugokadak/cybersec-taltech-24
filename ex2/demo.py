import time
import paho.mqtt.client as paho
broker="10.8.0.1"

# Define callback
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))

client= paho.Client("client-3") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")

# Bind function to callback
client.on_message=on_message

# Set username and password
client.username_pw_set(username = "iot_module3", password = "parool")

print("connecting to broker ",broker)
client.connect(broker)   # connect
client.loop_start()      # start loop to process received messages
print("subscribing ")
client.subscribe("class/iot03") #subscribe
time.sleep(2)

try:
        while True:
                    time.sleep(1)

except KeyboardInterrupt:
    print("exiting")
    client.disconnect() #disconnect
    client.loop_stop() #stop loop
