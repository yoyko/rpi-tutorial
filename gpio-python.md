GPIO - python
=============

GPIO knižnica

```
import RPi.GPIO as GPIO
```

Nastavíme piny na výstup

```
DIR=23
STEP=24

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
```

Jeden krok:
```python
def step(direction, delay):
    GPIO.output(DIR, direction)
    GPIO.output(STEP, 0)
    time.sleep(delay)
    GPIO.output(STEP, 1)
    time.sleep(delay)
```

(`time.sleep` potrebuje `import time`.)


Teraz môžeme skúsiť zahrať "tón":
```python
def play(freq, t):
    period = 1.0 / freq
    halfPeriod = period / 2
    d = 0
    endT = time.time() + t
    print("freq %d  period %f  halfPeriod %f" % (freq, period, halfPeriod))
    while time.time() < endT:
        d = 1 - d # "flip" direction
        step(d, halfPeriod)
```

A použíť to vieme ako

```
play(220, 0.5)
```

BTW, je dobré na začiatku "vycentrovať" hlavu, aby nebola na kraji...
