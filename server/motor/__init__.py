import RPi.GPIO as GPIO

class Pin:
    def __init__(self, physical, gpio):
        self.physical = physical
        self.gpio = gpio
        self.setup()

    def setup(self):
        GPIO.setup(self.gpio, GPIO.OUT)
        self.control(False)

    def control(self, val):
        GPIO.output(self.gpio, val)
