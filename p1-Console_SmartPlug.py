'''
Subscribes to states and publishes commands
'''

from tkinter import *
import paho.mqtt.client as mqtt
from project1.constants import *

""" Quitter proprement """
def fermer():
    print("Quitter proprement")
    client.loop_stop()
    client.disconnect()
    fen1.destroy()

def cmd_on():
    client.publish(TOPIC_COMMAND, SMARTPLUG1_CMD_ON)

def cmd_off():
    client.publish(TOPIC_COMMAND, SMARTPLUG1_CMD_OFF)

def on_message(client, userdata, message):
    print("received message: ", str(message.payload.decode("utf-8")))
    lblEtat.configure(text=str(message.payload.decode("utf-8")))
    
""" MQTT """
client = mqtt.Client(CLIENT_CONSOLE)
client.connect(MQTT_BROKER) 
client.loop_start()
client.subscribe(TOPIC_STATE)
client.on_message = on_message 

""" Interface Tk """
fen1 = Tk()
fen1.protocol("WM_DELETE_WINDOW", fermer)

lblEtat = Label(fen1, text="Etat", fg='red', font="Helvetica 20 bold")
lblEtat.grid(row = 0, column = 0, columnspan = 2)
btn1 = Button(fen1, text='ON', font="Helvetica 20 bold", command = cmd_on)
btn1.grid(row = 1, column = 0)
btn2 = Button(fen1, text='OFF', font="Helvetica 20 bold", command = cmd_off)
btn2.grid(row = 1, column = 1)

fen1.mainloop()
