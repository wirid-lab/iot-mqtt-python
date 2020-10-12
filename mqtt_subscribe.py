import paho.mqtt.client as mqtt
import ssl

def on_connect(client, userdata, flags, rc):
  global connected, MAIN_TOPIC, BROKER_URL
  print("Connected:  result code "+str(rc))
  if rc == 0:
    print("Connected to "+ BROKER_URL)
    client.subscribe(MAIN_TOPIC, qos=2)

def on_message(client, userdata, msg):
    print("Topic: "+ msg.topic+" | Message:  "+str(msg.payload.decode("utf-8")))

def on_subscribe(client, userdata, mid, granted_qos):
  print("Subscribed code " + str(mid) + " - QoS " + str(granted_qos))


connected = False
BROKER_URL="mqtt.wiridlab.site"
BROKER_PORT=8883
WIRID_LAB_AUTH_TOKEN="<YOUR_TOKEN>"
MAIN_TOPIC ="iot/<YOUR_EMAIL>/#"
CLIENT_ID ="<NODE_ID>"

client = mqtt.Client(CLIENT_ID)
client.on_subscribe = on_subscribe
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(WIRID_LAB_AUTH_TOKEN, "")
client.tls_set("root.pem", tls_version=ssl.PROTOCOL_TLSv1_2)
client.tls_insecure_set(True)
client.connect(BROKER_URL, BROKER_PORT, 30)
client.loop_forever()
