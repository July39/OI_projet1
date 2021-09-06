

from tkinter import *
import paho.mqtt.client as mqtt
import json
from project1.constants import *
from project1.eventlog import *


def fermer():
    print('Quitter proprement')
    client.loop_stop()
    client.disconnect()
    fen1.destroy()

def sys_alarm_cmd_on():
    print('salarm ystem off by console')
    client.publish(TOPIC_COMMAND, SYSALARM_CMD_ON)

def sys_alarm_cmd_off():
    """ turn off alarm system using MQTT """
    print('alarm system off by console')
    client.publish(TOPIC_COMMAND, SYSALARM_CMD_OFF)


def turn_smartplug_on():

    # ============================
    # turn on smartplug using MQTT
    # ============================
    print('smart plug on by console')
    msg = {}
    msg['id'] = CLIENT_CONSOLE
    msg['cmd'] = SMARTPLUG1_CMD_ON
    client.publish(TOPIC_COMMAND, json.dumps(msg))


def turn_smartplug_off():

    # =============================
    # turn off smartplug using MQTT
    # =============================
    msg = {}
    msg['id'] = CLIENT_CONSOLE
    msg['cmd'] = SMARTPLUG1_CMD_OFF
    client.publish(TOPIC_COMMAND, json.dumps(msg))


def light_cmd_on():
    pass


def light_cmd_off():
    pass


def show_history():

    fen2 = Tk()
    fen2.title("Historique")
    resultat = Text(fen2)
    resultat.config(width = 40, height = 10, font="Helvetica")

    # ======================================
    # fill up the widget with all the events
    # ======================================
    col = get_events()
    for event in col.find():
        resultat.insert(INSERT, event["date"] + "\t" + event["time"] + "\t" + event["state"] + "\n")

    resultat.grid(row = 0, column = 0, columnspan = 3)
    Button(fen2, text = "Quitter", font="Helvetica 15", command =show_history)
    fen2.mainloop()


def on_message(client, userdata, message):

    # ==================================================
    # decode the event and logs it into mongodb database
    # ==================================================
    msg = json.loads(str(message.payload.decode("utf-8")))
    print("received event: ", msg['id'], msg['cmd'])
    log_event(msg['cmd'])

    # =================================
    # update user interface accordingly
    # =================================
    if msg['id'] == CLIENT_SMARTPLUG1:
        if msg['cmd'] == SMARTPLUG1_STATE_OFF:
            pass
        elif msg['cmd'] == SMARTPLUG1_STATE_ON:
            pass
    elif msg['id'] == CLIENT_SMARTPLUG1:
        pass
    elif msg['id'] == CLIENT_SYSALARM:
        pass


# ====================================
# setup MQTT to subscribes to states
# ===================================
client = mqtt.Client(CLIENT_CONSOLE)
client.connect(MQTT_BROKER) 
client.loop_start()
client.subscribe(TOPIC_STATE)
client.on_message = on_message

# ==========================================
# create the main window
# ==========================================
fen1 = Tk()
fen1.protocol("WM_DELETE_WINDOW", fermer)
fen1.title("Console de controle")

# =================================================================
# alarm widgets
# =================================================================
lblEtat = Label(fen1, text="Alarme", fg='black', font="Helvetica 20 bold")
lblEtat.grid(row = 0, column = 0, columnspan = 2)
btn1 = Button(fen1, text='ON', fg='green', font="Helvetica 20 bold", command = sys_alarm_cmd_on)
btn1.grid(row = 1, column = 0)
btn2 = Button(fen1, text='OFF',fg='red', font="Helvetica 20 bold", command = sys_alarm_cmd_off)
btn2.grid(row = 1, column = 1)

# =================================================================
# light widgets
# =================================================================
lblEtat = Label(fen1, text="Lumiere entrée", fg='black', font="Helvetica 20 bold")
lblEtat.grid(row = 2, column = 0, columnspan = 2)
btn3 = Button(fen1, text='ON',fg='green', font="Helvetica 20 bold", command = light_cmd_on)
btn3.grid(row = 3, column = 0)
btn4 = Button(fen1, text='OFF',fg='red', font="Helvetica 20 bold", command = light_cmd_off)
btn4.grid(row = 3, column = 1)

# =================================================================
# smartplug widgets
# =================================================================
lblEtat = Label(fen1, text="Smartplug", fg='black', font="Helvetica 20 bold")
lblEtat.grid(row = 4, column = 0, columnspan = 2)
btn5 = Button(fen1, text='ON',fg='green', font="Helvetica 20 bold", command = turn_smartplug_on)
btn5.grid(row = 5, column = 0)
btn6 = Button(fen1, text='OFF',fg='red', font="Helvetica 20 bold", command = turn_smartplug_off)
btn6.grid(row = 5, column = 1)

# ================================================================
# log history widgets
# ================================================================
lblEtat = Label(fen1, text="Historique", fg='black', font="Helvetica 20 bold")
lblEtat.grid(row = 6, column = 0, columnspan = 2)
btn6 = Button(fen1, text='Afficher',fg='blue', font="Helvetica 20 bold", command = show_history)
btn6.grid(row = 7, column = 0)

fen1.mainloop()
