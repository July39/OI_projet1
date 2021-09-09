

__all__ = ["DATE_FORMAT",
           "TIME_FORMAT",
           "MQTT_BROKER", 
           "MONGODB_URI",
           "CLIENT_CONSOLE", 
           "CLIENT_SMARTPLUG1",
           "CLIENT_SYSALARM",
           "CLIENT_LIGHT",
           "CLIENT_ALL",
           "TOPIC_STATE",
           "TOPIC_COMMAND",
           "ALL_CMD_GET_STATUS",
           "SYSALARM_STATE_OFF",
           "SYSALARM_STATE_ON",
           "SYSALARM_CMD_OFF",
           "SYSALARM_CMD_ON",
           "SYSALARM_INTRUDER",
           "SMARTPLUG1_STATE_OFF",
           "SMARTPLUG1_STATE_ON",
           "SMARTPLUG1_CMD_OFF",
           "SMARTPLUG1_CMD_ON",
           "LIGHT_STATE_OFF",
           "LIGHT_STATE_ON",
           "LIGHT_CMD_OFF",
           "LIGHT_CMD_ON"]


"""date/time format"""
DATE_FORMAT = "%Y/%m/%d"
TIME_FORMAT = "%H:%M"

"""MQTT broker"""
MQTT_BROKER = "127.00.00.01"

MONGODB_URI = "localhost"

"""MQTT clients"""
CLIENT_CONSOLE    = "Console"
CLIENT_SMARTPLUG1 = "SmartPlug1"
CLIENT_SYSALARM = "SysAlarm"
CLIENT_LIGHT = "Light"
CLIENT_ALL = "All IoT"

"""MQTT topics"""
TOPIC_STATE = "Gills/Etats"
TOPIC_COMMAND = "Gills/Commandes"

"""All IoT commands"""
ALL_CMD_GET_STATUS = "Get Status"

"""SmartPlug1 states"""
SMARTPLUG1_STATE_OFF = "off"
SMARTPLUG1_STATE_ON  = "on"

"""SmartPlug1 commands"""
SMARTPLUG1_CMD_OFF = "off"
SMARTPLUG1_CMD_ON  = "on"

"""System alarm states"""
SYSALARM_STATE_OFF = "off"
SYSALARM_STATE_ON  = "on"
SYSALARM_INTRUDER  = "panic"

"""System alarm commands"""
SYSALARM_CMD_OFF = "off"
SYSALARM_CMD_ON  = "on"

"""Light states"""
LIGHT_STATE_OFF = "off"
LIGHT_STATE_ON  = "on"

"""Light commands"""
LIGHT_CMD_OFF = "off"
LIGHT_CMD_ON  = "on"

