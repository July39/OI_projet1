

from enum import Enum


__all__ = ["MQTT_BROKER", 
           "CLIENT_CONSOLE", 
           "CLIENT_SMARTPLUG1",
           "TOPIC_STATE",
           "TOPIC_COMMAND",
           "SMARTPLUG1_STATE_OFF",
           "SMARTPLUG1_STATE_ON",
           "SMARTPLUG1_CMD_OFF",
           "SMARTPLUG1_CMD_ON"]

"""MQTT broker"""
MQTT_BROKER = "127.00.00.01"

"""MQTT clients"""
CLIENT_CONSOLE    = "Console"
CLIENT_SMARTPLUG1 = "SmartPlug1"

"""MQTT topics"""
TOPIC_STATE   = "Gills/Etats"
TOPIC_COMMAND = "Gills/Commandes"

"""SmartPlug1 states"""
SMARTPLUG1_STATE_OFF = "off"
SMARTPLUG1_STATE_ON  = "on"

"""SmartPlug1 commands"""
SMARTPLUG1_CMD_OFF = "off"
SMARTPLUG1_CMD_ON = "on"


