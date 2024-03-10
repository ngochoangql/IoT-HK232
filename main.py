import sys
from Adafruit_IO import MQTTClient
from uart import writeData
AIO_FEED_IDs = ["button1","button2"]
AIO_USERNAME = "hoangdoan2408bk"
AIO_KEY = "aio_pCIm40uEpfqgUjNBLic7BMaNwSC0"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs :
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)
    if feed_id == "button1" :
        if payload == "on" :
            writeData("Button1 On")
        elif payload == "off":
            writeData("Button1 Off")
    if feed_id == "button2" :
        if payload == "on" :
            writeData("Button2 On")
        elif payload == "off":
            writeData("Button2 Off") 
client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    pass