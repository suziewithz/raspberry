#!/usr/bin/python
import sys
import time
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

class Steps:
    def __init__(self, first, second, third, fourth):
        self.pin_map = {"in1": first, "in2": second, "in3": third, "in4": fourth}
        self.sequence = [
                    {"in1": True, "in2": False, "in3": False, "in4": True},
                    {"in1": True, "in2": False, "in3": False, "in4": False},
                    {"in1": True, "in2": True, "in3": False, "in4": False},
                    {"in1": False, "in2": True, "in3": False, "in4": False},
                    {"in1": False, "in2": True, "in3": True, "in4": False},
                    {"in1": False, "in2": False, "in3": True, "in4": False},
                    {"in1": False, "in2": False, "in3": True, "in4": True},
                    {"in1": False, "in2": False, "in3": False, "in4": True}
                ]

    def do(self, sequence_num):
        step = self.sequence[sequence_num]
        for target_pin_name in step.keys():
            target_pin = self.pin_map[target_pin_name]
            target_pin.control(step[target_pin_name])

    def roll(self, clock_wise=False, wait_time=1):
        # Cannot be faster than this
        wait_time = int(wait_time)/float(1000)
        if clock_wise:
            for step in reversed(xrange(len(self.sequence))):
                self.do(step)
                time.sleep(wait_time)
        else:
            for step in xrange(len(self.sequence)):
                self.do(step)
                time.sleep(wait_time)

def main() :
    GPIO.setmode(GPIO.BCM)

    red = Pin(11, 17)
    orange = Pin(15, 22)
    white = Pin(16, 23)
    black = Pin(18, 24)

    sequence = Steps(red, orange, white, black)

    while True:
        sequence.roll(clock_wise=False, wait_time=1)

if __name__ == "__main__" :
    main()
