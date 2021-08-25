

__all__ = ["MQTT_BROKER", 
           "CLIENT_CONSOLE", 
           "CLIENT_SMARTPLUG1",
           "CLIENT_SYSALARM",
           "TOPIC_STATE",
           "TOPIC_COMMAND",
           "SYSALARM_STATE_OFF",
           "SYSALARM_STATE_ON",
           "SYSALARM_CMD_OFF",
           "SYSALARM_CMD_ON",
           "SMARTPLUG1_STATE_OFF",
           "SMARTPLUG1_STATE_ON",
           "SMARTPLUG1_CMD_OFF",
           "SMARTPLUG1_CMD_ON"]

"""MQTT broker"""
MQTT_BROKER = "127.00.00.01"

"""MQTT clients"""
CLIENT_CONSOLE    = "Console"
CLIENT_SMARTPLUG1 = "SmartPlug1"
CLIENT_SYSALARM = "SysAlarm"


"""MQTT topics"""
TOPIC_STATE = "Gills/Etats"
TOPIC_COMMAND = "Gills/Commandes"

"""SmartPlug1 states"""
SMARTPLUG1_STATE_OFF = "off"
SMARTPLUG1_STATE_ON  = "on"

"""SmartPlug1 commands"""
SMARTPLUG1_CMD_OFF = "off"
SMARTPLUG1_CMD_ON = "on"

"""System alarm states"""
SYSALARM_STATE_OFF = "off"
SYSALARM_STATE_ON  = "on"

"""System alarm commands"""
SYSALARM_CMD_OFF = "off"
SYSALARM_CMD_ON = "on"


