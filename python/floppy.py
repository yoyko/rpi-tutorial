#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

DIR=23
STEP=24

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

def step(direction, delay):
    GPIO.output(DIR, direction)
    GPIO.output(STEP, 0)
    time.sleep(delay)
    GPIO.output(STEP, 1)
    time.sleep(delay)

def play(freq, t):
    period = 1.0 / freq
    halfPeriod = period / 2
    d = 0
    endT = time.time() + t
    print("freq %d  period %f  halfPeriod %f" % (freq, period, halfPeriod))
    while time.time() < endT:
        d = 1 - d # "flip" direction
        step(d, halfPeriod)

def playNote(noteString):
    import note
    freq, duration = note.parse(noteString)
    print('Note: %.2f %.2f' % (freq, duration))
    if freq == 0:
        time.sleep(duration)
    else:
        play(freq, duration)

def playNotes(notes):
    for note in notes.split():
        playNote(note)

def reset():
    for i in range(40):
        step(0, 0.005)
    for i in range(20):
        step(1, 0.005)

def cleanup():
    print("done")
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        reset()
        playNotes('c/4 d/4 e/4')
    except KeyboardInterrupt:
        pass
    finally:
        cleanup()
