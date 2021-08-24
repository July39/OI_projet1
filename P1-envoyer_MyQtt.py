'''
Created on 21 juin 2021

@author: https://medium.com/python-point/mqtt-basics-with-python-examples-7c758e605d4
'''
import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time

host          = "node02.myqtthub.com"
port          = 1883
clean_session = True
client_id     = "MonThermometre"
user_name     = "Thermo"
password      = "xxxxxx"

client = mqtt.Client(client_id = client_id, clean_session = clean_session)
client.username_pw_set (user_name, password)
client.connect (host, port) 

while True:
    randNumber = uniform(18.0, 24.0)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to topic TEMPERATURE")
    time.sleep(2)
