import LedSwitch_pb2_grpc
import LedSwitch_pb2

import grpc
import logging

from pydantic_yaml import parse_yaml_raw_as, to_yaml_str, to_yaml_file
from pydantic import BaseModel

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button = 4
i = 0

GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)
led_on = False

class Address(BaseModel):
    ip: str
    port: int

class MyModel(BaseModel):
    address: Address

def MakeModelFromYAML(filename):
    with open(filename) as configFile:
        yml = configFile.read()
    ModelYAML = parse_yaml_raw_as(MyModel, yml)
    return ModelYAML

def toggleState(channel):
    global led_on 
    led_on = not led_on
    run()

def run():
    fullAddress = ModelYAML.address.ip + ':' + str(ModelYAML.address.port)
    print(fullAddress)

    GPIO.add_event_detect(4, GPIO.RISING, callback=toggleState, bouncetime=300)
    
    with grpc.insecure_channel(fullAddress) as channel:
        channel = grpc.insecure_channel(fullAddress)
        stub = LedSwitch_pb2_grpc.LedSwtichStub(channel)
        response = stub.SendLedState(LedSwitch_pb2.LedSwitchRequest(LedState = led_on))
  
if __name__ == '__main__':
    ModelYAML = MakeModelFromYAML("config.yaml")
    logging.basicConfig()
    run()