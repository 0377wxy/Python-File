from machine import Pin
import time

LED = Pin(2, Pin.OUT)

while True:
    LED.value(1)
    time.sleep(1)
    LED.value(0)
    time.sleep(1)
