'''
Subscribes to commands and publishes states
'''

from RPiSim import GPIO
import paho.mqtt.client as mqtt
import time
import sys
import signal
import json
from project1.constants import *

# ======================
# module level constants
# ======================

BOUTON_PIN  = 17
LUMIERE_PIN = 18
DEL_PIN     = 23

# ===============================================================
# helper function used to publish new IoT object state using MQTT
# ===============================================================
def publish_state(state):
    msg = {}
    msg['id'] = CLIENT_SMARTPLUG1
    msg['cmd'] = state
    client.publish(TOPIC_STATE, json.dumps(msg))

# ====================================
# event handlers
# ====================================
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

        # =======================================
        # publish the new state; smartplug is off
        # =======================================
        publish_state(SMARTPLUG1_STATE_OFF)

    else:
        GPIO.output(LUMIERE_PIN, GPIO.HIGH)
        print("DEL On")

        # ======================================
        # publish the new state; smartplug is on
        # ======================================
        publish_state(SMARTPLUG1_STATE_ON)

def on_message(client, userdata, message):

    # ==========================================
    # unmarshall the object from the sent string
    # ========================================== 
    print("received message: ", str(message.payload.decode("utf-8")))
    msg = json.loads(str(message.payload.decode("utf-8")))

    # =========================================================
    # dispatch the command if it is intended to this IoT object
    # =========================================================
    if msg['id'] == CLIENT_SMARTPLUG1 or msg['id'] == CLIENT_ALL:

        if msg['cmd'] == SMARTPLUG1_CMD_ON:

            # ==========================================================
            # turn on the smartplug and publish the new state using MQTT
            # ==========================================================
            GPIO.output(LUMIERE_PIN, GPIO.HIGH)
            print("DEL On")
            publish_state(SMARTPLUG1_STATE_ON)

        elif msg['cmd'] == SMARTPLUG1_CMD_OFF:

            # ===========================================================
            # turn off the smartplug and publish the new state using MQTT
            # ===========================================================
            GPIO.output(LUMIERE_PIN, GPIO.LOW)
            print("DEL Off")
            publish_state(SMARTPLUG1_STATE_OFF)

        elif msg['cmd'] == ALL_CMD_GET_STATUS:

            # ===============================
            # publish the object's state only
            # ===============================
            if GPIO.input(LUMIERE_PIN):
                publish_state(SMARTPLUG1_STATE_ON)
            else:
                publish_state(SMARTPLUG1_STATE_OFF)


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

# ====================================
# setup MQTT to subscribes to commands
# ====================================
client = mqtt.Client(CLIENT_SMARTPLUG1)
client.connect(MQTT_BROKER) 
client.loop_start()
client.subscribe(TOPIC_COMMAND)
client.on_message = on_message 
    
while True:
    time.sleep(0.5)
    
