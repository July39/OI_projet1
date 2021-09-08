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
import json


PORTE_PIN = 5
BOUTON_PIN = 17
SIRENE_PIN = 18
DEL_PIN = 23


# ===============================================================
# helper function used to publish new IoT object state using MQTT
# ===============================================================
def publish_state(state):
    msg = {}
    msg['id'] = CLIENT_SYSALARM
    msg['cmd'] = state
    client.publish(TOPIC_STATE, json.dumps(msg))

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

def setEtat(event,commande = ''):
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

            # ====================================
            # publish the new state; alaram is off
            # ====================================
            publish_state(SYSALARM_STATE_OFF)
            
            # Affficher ecran armé
        elif etat == Etat.DELAI_S:
            print ("Desarmer")
            etat = Etat.OFF
            #thread.stop()
            GPIO.output(DEL_PIN, GPIO.LOW)

            # ====================================
            # publish the new state; alaram is off
            # ====================================
            publish_state(SYSALARM_STATE_OFF)

            # Affficher ecran armé  
        elif etat == Etat.SIRENE:
            print ("Desarmer")
            etat = Etat.OFF
            GPIO.output(DEL_PIN, GPIO.LOW)
            GPIO.output(SIRENE_PIN, GPIO.LOW)

            # ====================================
            # publish the new state; alaram is off
            # ====================================
            publish_state(SYSALARM_STATE_OFF)
 
            # Affficher ecran armé  
        elif etat == Etat.DELAI_E:
            print ("Desarmer")
            etat = Etat.OFF
            #thread.stop()
            GPIO.output(DEL_PIN, GPIO.LOW)

            # ====================================
            # publish the new state; alaram is off
            # ====================================
            publish_state(SYSALARM_STATE_OFF)

            # Affficher ecran armé                  
    elif event == Event.finDelais:
        if etat == Etat.DELAI_S:
            print ("Armer")
            etat = Etat.ARME
            GPIO.output(DEL_PIN, GPIO.HIGH)

            # ===================================
            # publish the new state; alaram is on
            # ===================================
            publish_state(SYSALARM_STATE_ON)
            
            # Afficher ecran Désarmé
        elif etat == Etat.DELAI_E:
            print("Sirene")
            etat = Etat.SIRENE
            GPIO.output(SIRENE_PIN, GPIO.HIGH)

            # =================================
            # publish the new state; intruder!!
            # =================================
            publish_state(SYSALARM_INTRUDER)
            
    elif event == Event.porte:
        if etat == Etat.ARME:
            print("Ouverture d'une porte")
            etat = Etat.DELAI_E
            thread = Thread(target=blinkDEL, args=())
            thread.start()
            """Si on lit 2 fois de suite systeme on, remet l'état à on"""

    if event == Event.boutonInterface:
        if commande == 'ON':
            print("Armeture systeme")
            etat = Etat.ARME
            GPIO.output(DEL_PIN, GPIO.HIGH)

            # ===================================
            # publish the new state; alaram is on
            # ===================================
            publish_state(SYSALARM_STATE_ON)

        else :
            print("Désarmé systeme alarme")
            etat = Etat.OFF
            GPIO.output(DEL_PIN, GPIO.LOW)
            GPIO.output(SIRENE_PIN, GPIO.LOW)

            # ====================================
            # publish the new state; alaram is off
            # ====================================
            publish_state(SYSALARM_STATE_OFF)

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

    # ==========================================
    # unmarshall the object from the sent string
    # ========================================== 
    print("received message: ", str(message.payload.decode("utf-8")))
    msg = json.loads(str(message.payload.decode("utf-8")))

    # =========================================================
    # dispatch the command if it is intended to this IoT object
    # =========================================================
    if msg['id'] == CLIENT_SYSALARM or msg['id'] == CLIENT_ALL:

        if msg['cmd'] == SYSALARM_CMD_ON:

            # =============================================================
            # turn on the alarm system and publish the new state using MQTT
            # =============================================================
            print("systeme armé par console")
            setEtat(Event.boutonInterface,'ON')

        elif msg['cmd'] == SYSALARM_CMD_OFF:

            # ==============================================================
            # turn off the alarm system and publish the new state using MQTT
            # ==============================================================
            print("systeme desarme par la console")
            setEtat(Event.boutonInterface,'OFF')

        elif msg['cmd'] == ALL_CMD_GET_STATUS:

            # ===============================
            # publish the object's state only
            # ===============================
            if etat == Etat.OFF:
                state = SYSALARM_STATE_OFF
            elif etat == Etat.ARME:
                state = SYSALARM_STATE_ON
            elif etat == Etat.SIRENE:
                state = SYSALARM_INTRUDER
            publish_state(state)

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
    
    