# coding=utf-8
import time
import RPi.GPIO as GPIO


class LED(object):
    def __init__(self, pin):
        self.pin = pin
        self.status = False
    
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin ,GPIO.OUT)
        
    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)
        self.status = True

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)
        self.status = False

    def flash(self, delay, r):
        for i in range(r):
            self.off()
            time.sleep(delay)
            self.on()
            time.sleep(delay)

    def get_status(self):
            return self.status
