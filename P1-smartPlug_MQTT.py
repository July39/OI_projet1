'''
Created on 21 juin 2021

@author: gills
'''
from RPiSim import GPIO
import paho.mqtt.client as mqtt
import time
import sys
import signal

def terminer(signum, frame):
    print("Terminer")
    GPIO.output(18, GPIO.LOW)
    GPIO.cleanup()
    sys.exit(0)

def event_17(channel):
    print("event_17: Bouton poussoir")
    if GPIO.input(18):
        GPIO.output(18, GPIO.LOW)
        print("DEL Off")
        client.publish("Gills/Etats", "off")
    else:
        GPIO.output(18, GPIO.HIGH)
        print("DEL On")
        client.publish("Gills/Etats", "on")

def on_message(client, userdata, message):
    print("received message: " , str(message.payload.decode("utf-8")))
    commande = str(message.payload.decode("utf-8"))
    if commande == "on":
        GPIO.output(18, GPIO.HIGH)
        print("DEL On")
        client.publish("Gills/Etats", "on")
    elif commande == "off":
        GPIO.output(18, GPIO.LOW)
        print("DEL Off")
        client.publish("Gills/Etats", "off")

""" Les GPIO  """
signal.signal(signal.SIGINT, terminer)
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    """ Bouton poussoir on/off """
    GPIO.setup(17,GPIO.MODE_IN,pull_up_down = GPIO.PUD_UP) 
    GPIO.add_event_detect(17, GPIO.FALLING, callback=event_17)
    """ Lumière """
    GPIO.setup(18,GPIO.MODE_OUT, initial=GPIO.LOW)
except Exception:
    print("Problème avec les GPIO")

""" MQTT """
#mqttBroker ="mqtt.eclipseprojects.io" #Utilise le port 80
mqttBroker ="127.01.01.1" #Utilise le port 80

client = mqtt.Client("SmartPlug1")
client.connect(mqttBroker) 
client.loop_start()
client.subscribe("Gills/Commandes")
client.on_message=on_message 
    
while True:
    time.sleep(0.5)
    
