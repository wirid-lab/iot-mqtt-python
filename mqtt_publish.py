import paho.mqtt.client as mqtt
import time
import ssl

def on_connect(client, userdata, flags, rc):
  global connected , MAIN_TOPIC, BROKER_URL
  if connected == False:
    if rc == 0:
      print("Connected to "+ BROKER_URL)
      connected = True  # Signal connection
      #client.subscribe(MAIN_TOPIC, qos=2)
    else:
      print("Connection failed")
  elif connected == True:
    if rc == 0:
      connected = True  # Signal connection
      #client.subscribe(MAIN_TOPIC, qos=2)
    else:
      connected = False


def on_message(client, userdata, msg):
    print("Topic: "+ msg.topic+" | Message:  "+str(msg.payload.decode("utf-8")))


def on_subscribe(client, userdata, mid, granted_qos):
  print("Subscribed code " + str(mid) + " - QoS " + str(granted_qos))

connected = False
BROKER_URL="mqtt.wiridlab.site"
BROKER_PORT=8883
WIRID_LAB_AUTH_TOKEN="<YOUR_TOKEN>"
MAIN_TOPIC ="iot/<YOUR_EMAIL>/#"
PUB_TOPIC ="iot/<YOUR_EMAIL>/test"
CLIENT_ID ="<NODE_ID>"



client = mqtt.Client(CLIENT_ID)
client.on_subscribe = on_subscribe
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(WIRID_LAB_AUTH_TOKEN, "")
client.tls_set("root.pem", tls_version=ssl.PROTOCOL_TLSv1_2)
client.tls_insecure_set(True)
client.connect(BROKER_URL, BROKER_PORT, 30)


#client.loop_forever()
client.loop_start()
while connected != True:  # Wait for connection
  time.sleep(0.1)

try:
  while True:
    value = input('Enter the message:')
    client.publish(PUB_TOPIC, value, qos=1)

except KeyboardInterrupt:

  client.disconnect()
  client.loop_stop()
