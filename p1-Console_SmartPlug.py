'''
Created on 21 juin 2021

@author: gills
Référence: https://support.asplhosting.com/t/working-myqtthub-com-python-paho-examples/43
'''
from tkinter import *
import paho.mqtt.client as mqtt 

""" Quitter proprement """
def fermer():
    print("Quitter proprement")
    client.loop_stop()
    client.disconnect()
    fen1.destroy()

def cmd_on():
    client.publish("Gills/Commandes", "on")

def cmd_off():
    client.publish("Gills/Commandes", "off")
    
def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))
    lblEtat.configure(text=str(message.payload.decode("utf-8")))
    
""" MQTT """
#mqttBroker ="mqtt.eclipseprojects.io" +
mqttBroker =  "127.01.01.1"

client = mqtt.Client("Console")
client.connect(mqttBroker) 

client.loop_start()

client.subscribe("Gills/Etats")
client.on_message=on_message 

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