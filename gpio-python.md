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

BTW, je dobré na začiatku "vycentrovať" hlavu, aby nebola na kraji
(3.5" mechaniky majú 80 stôp, takže sa dá napríklad posunúť 80 krokov jedným
smerom a potom 40 krokov naspäť `;-)`)

Odbočka: noty
-------------

V súbore [`note.py`](python/note.py) je mini "knižnica" na rozpoznávanie
textovo zapísaných nôt: napríklad `C/4` rozpozná ako štvrtinovú notu C,
`Db3/8.` ako osminovú notu D z tretej oktávy s bodkou zníženú o poltón atď.

Funkcia `parse` vráti dvojicu: frequenciu a dĺžku noty (v sekundách).

```
>>> import note
>>> note.parse('e4/4')
(329.62755691286986, 0.5)
>>> note.parse('a4/4')
(440.0, 0.5)
>>> note.parse('a4/4')
(440.0, 0.5)
>>> note.parse('c#/1.')
(277.18263097687196, 2.0)
```

Najľahšie je v pythone túto dvojicu rovno priradiť do dvoch premenných:

```python
frequency, duration = note.parse(noteString)
```

S využitím predchádzajuúcej funkcie `play` môžeme spraviť:

```python
def playNote(noteString):
    import note
    freq, duration = note.parse(noteString)
    print('Note: %.2f %.2f' % (freq, duration))
    if freq == 0:
        time.sleep(duration)
    else:
        play(freq, duration)
```
