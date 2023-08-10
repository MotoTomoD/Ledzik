
import RPi.GPIO as GPIO
import LedSwitch_pb2
import LedSwitch_pb2_grpc
import grpc
from concurrent import futures
import logging

def changeLedState(request):
    LED_PIN = 16
    GPIO.setmode(GPIO.BCM) #odwolywanie sie do GPIO poprzez numer GPIO a nie przez nr PINu
    GPIO.setup(LED_PIN, GPIO.OUT) #konfiguracja GPIO
    if request.LedState == True:
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)

class LedSwitchServicer(LedSwitch_pb2_grpc.LedSwitchServicer):
    def SendLedState(self, request, context): 
        changeLedState(request) #nie wiem czy moge dać requesta tutaj jak oargument, do sprawdzenia
        return LedSwitch_pb2.LedSwitchReply(message='Zeskanowano: %s' % request.LedState)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    LedSwitch_pb2_grpc.add_LedSwitchServicer_to_server(
        LedSwitchServicer(), server)
    server.add_insecure_port('0.0.0.0:50051') # 0.0.0.0:PORT powinno odbierać od wszystkich adresów
    server.start()
    server.wait_for_termination() #mozliwe ze ta linijka jest blokujaca, pozniej WYKOMENTOWAC
    
    
if __name__ == '__main__':
    logging.basicConfig()
    serve()

