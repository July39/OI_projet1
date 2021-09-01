'''
Subscribes to commands and publishes states
'''

from RPiSim import GPIO
import paho.mqtt.client as mqtt
import time
import sys
import signal
from project1.constants import *

BOUTON_PIN = 17
LUMIERE_PIN = 18
DEL_PIN = 23

def terminer(signum, frame):
    print("Terminer")
    GPIO.output(LUMIERE_PIN, GPIO.LOW)
    GPIO.cleanup()
    sys.exit(0)

def event_bouton(channel):
    print("event_17: Bouton poussoir")
    if GPIO.input(LUMIERE_PIN):
        GPIO.output(LUMIERE_PIN, GPIO.LOW)
        print("DEL Off")
        client.publish(TOPIC_STATE, SMARTPLUG1_STATE_OFF)
    else:
        GPIO.output(LUMIERE_PIN, GPIO.HIGH)
        print("DEL On")
        client.publish(TOPIC_STATE, SMARTPLUG1_STATE_ON)
        
def on_message(client, userdata, message):
    print("received message: " , str(message.payload.decode("utf-8")))
    commande = str(message.payload.decode("utf-8"))
    if commande == SMARTPLUG1_CMD_ON:
        GPIO.output(LUMIERE_PIN, GPIO.HIGH)
        print("DEL On")
        client.publish(TOPIC_STATE, SMARTPLUG1_STATE_ON)
    elif commande == SMARTPLUG1_CMD_OFF:
        GPIO.output(LUMIERE_PIN, GPIO.LOW)
        print("DEL Off")
        client.publish(TOPIC_STATE, SMARTPLUG1_STATE_OFF)

""" Les GPIO  """
signal.signal(signal.SIGINT, terminer)
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    """ Bouton poussoir on/off """
    GPIO.setup(BOUTON_PIN,GPIO.MODE_IN,pull_up_down = GPIO.PUD_UP) 
    GPIO.add_event_detect(BOUTON_PIN, GPIO.FALLING, callback=event_bouton)
    """ Lumière """
    GPIO.setup(LUMIERE_PIN,GPIO.MODE_OUT, initial=GPIO.LOW)
except Exception:
    print("Problème avec les GPIO")

""" MQTT """
client = mqtt.Client(CLIENT_SMARTPLUG1)
client.connect(MQTT_BROKER) 
client.loop_start()
client.subscribe(TOPIC_COMMAND)
client.on_message = on_message 
    
while True:
    time.sleep(0.5)
    

