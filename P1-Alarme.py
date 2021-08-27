'''
Created on 21 juin 2021

@author: gills
'''
from enum import Enum
from RPiSim import GPIO
import paho.mqtt.client as mqtt
from threading import Thread
from project1.constants import * 
import sys
import signal
import time

PORTE_PIN = 5
BOUTON_PIN = 17
SIRENE_PIN = 18
DEL_PIN = 23
   
class Etat(Enum):
    OFF = 1
    DELAI_E = 2
    ARME = 3
    DELAI_S = 4
    SIRENE = 5

etat = Etat.OFF

class Event(Enum):
    porte = 1
    btnArm = 2
    code = 3
    boutonInterface = 4
    finDelais = 5

###############################################
""" Les fonctions """
###############################################
    
def terminer(signum, frame):
    print("Terminer")
    GPIO.output(SIRENE_PIN, GPIO.LOW)
    GPIO.cleanup()
    sys.exit(0)

def event_btnArm(channel):
    print("event bouton arm")
    setEtat(Event.btnArm)

def event_porte(channel):
    print("event porte")
    setEtat(Event.porte)

def setEtat(event):
    global etat
    print("set etat")
    if event == Event.btnArm:
        if etat == Etat.OFF:
            print ("Delais de sortie")
            etat = Etat.DELAI_S
            thread = Thread(target=blinkDEL, args=())
            thread.start()
            # Afficher ecran Désarmé
        elif etat == Etat.ARME:
            print ("Desarmer")
            etat = Etat.OFF
            GPIO.output(DEL_PIN, GPIO.LOW)
            GPIO.output(SIRENE_PIN, GPIO.LOW)
            # Affficher ecran armé
        elif etat == Etat.DELAI_S:
            print ("Desarmer")
            etat = Etat.OFF
            #thread.stop()
            GPIO.output(DEL_PIN, GPIO.LOW)
            # Affficher ecran armé  
        elif etat == Etat.SIRENE:
            print ("Desarmer")
            etat = Etat.OFF
            GPIO.output(DEL_PIN, GPIO.LOW)
            GPIO.output(SIRENE_PIN, GPIO.LOW) 
            # Affficher ecran armé  
        elif etat == Etat.DELAI_E:
            print ("Desarmer")
            etat = Etat.OFF
            #thread.stop()
            GPIO.output(DEL_PIN, GPIO.LOW)
            # Affficher ecran armé                  
    elif event == Event.finDelais:
        if etat == Etat.DELAI_S:
            print ("Armer")
            etat = Etat.ARME
            GPIO.output(DEL_PIN, GPIO.HIGH)
            # Afficher ecran Désarmé
        elif etat == Etat.DELAI_E:
            print("Sirene")
            etat = Etat.SIRENE
            GPIO.output(SIRENE_PIN, GPIO.HIGH)
    elif event == Event.porte:
        if etat == Etat.ARME:
            print("Ouverture d'une porte")
            etat = Etat.DELAI_E
            thread = Thread(target=blinkDEL, args=())
            thread.start()
              

def blinkDEL():
    DELAI = 5
    delai = 0
    while delai <= DELAI:
        if etat == Etat.OFF:
            return
        if GPIO.input(DEL_PIN):
            GPIO.output(DEL_PIN, GPIO.LOW)
        else:
            GPIO.output(DEL_PIN, GPIO.HIGH)
        time.sleep(1)
        delai = delai + 1
    setEtat(Event.finDelais)


def on_message(client, userdata, message):
    print("received message: " , str(message.payload.decode("utf-8")))
    commande = str(message.payload.decode("utf-8"))
    if commande == SMARTPLUG1_CMD_ON:
        GPIO.output(18, GPIO.HIGH)
        print("DEL On")
        client.publish(TOPIC_STATE, SMARTPLUG1_STATE_ON)
    elif commande == SMARTPLUG1_CMD_OFF:
        GPIO.output(18, GPIO.LOW)
        print("DEL Off")
        client.publish(TOPIC_STATE, SMARTPLUG1_STATE_OFF)      


###################################            
""" Mon programme """
###################################

""" Configuration des GPIOs """
signal.signal(signal.SIGINT, terminer)
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    """ Bouton poussoir on/off """
    GPIO.setup(BOUTON_PIN,GPIO.MODE_IN,pull_up_down = GPIO.PUD_UP) 
    GPIO.add_event_detect(BOUTON_PIN, GPIO.FALLING, callback=event_btnArm)
    
    """ Porte """
    GPIO.setup(PORTE_PIN,GPIO.MODE_IN,pull_up_down = GPIO.PUD_UP) 
    GPIO.add_event_detect(PORTE_PIN, GPIO.FALLING, callback=event_porte)
    
    """ Sirene """
    GPIO.setup(SIRENE_PIN,GPIO.MODE_OUT, initial=GPIO.LOW)
    
    """ DEL """
    GPIO.setup(DEL_PIN,GPIO.MODE_OUT, initial=GPIO.LOW)
    
except Exception:
    print("Problème avec les GPIO")

""" MQTT """
client = mqtt.Client(CLIENT_SYSALARM)
client.connect(MQTT_BROKER) 
client.loop_start()
client.subscribe(TOPIC_COMMAND)
client.on_message = on_message 
    
while True:
    
    time.sleep(0.5)
    
    