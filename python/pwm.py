#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

DIR=23
STEP=24

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

pDir = GPIO.PWM(DIR, 220)
pStep = GPIO.PWM(STEP, 440)

#pDir.start(50)
#time.sleep(1.0 / 440)
#pStep.start(50)
#
#time.sleep(1)
#
#pDir.ChangeFrequency(110)
#pStep.ChangeFrequency(220)
#
#time.sleep(1)
#
#pDir.stop()
#pStep.stop()
#

def sound(hz):
    pDir.stop()
    pStep.stop()
    if hz == 0:
        return
    pDir.ChangeFrequency(hz / 2.0)
    pStep.ChangeFrequency(hz)
    pDir.start(50)
    time.sleep(0.001)
    pStep.start(50)


if __name__ == '__main__':
    s = pow(2.0, 1.0/12)
    sound(440)
    time.sleep(0.5)
    sound(440*s*s)
    time.sleep(0.5)
    sound(440*s*s*s*s)
    time.sleep(0.5)
    sound(0)

    GPIO.cleanup()
