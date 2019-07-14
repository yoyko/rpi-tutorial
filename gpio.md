GPIO
====

RPi má vyvedené vstupy a výstupy (general purpose input/outpu), ku ktorým je
možné pripájať rôzne zariadenia, podobne ako k arduinu. V tejto časti si ukážeme
ako s nimi môžeme z linuxu pracovať. Skúsime však
[niečo zaujímavejšie](https://www.youtube.com/results?search_query=floppy+music)
ako svietiť LEDkami.



Trocha histórie: disketová mechanika
------------------------------------

[Diskentové (floppy) mechaniky](https://sk.wikipedia.org/wiki/Disketov%C3%A1_jednotka)
ukladajú a čítajú dáta na/z diskety s plastovým kotúčom s magnetickou vrstvou.
Dáta sú uložené v sústredných kružniciach -- "stopách" a čítacia/zapisovacia
hlava sa medzi nimi posúva pomocou krokového motorčekmi.

Budeme chcieť hýbať hlavou v správnom rytme, na čo nás budú na disketovej mechaníke
zaujímať piny DIRECTION a STEP: https://www.google.com/search?q=floppy+pinout.

Identifikácia GPIO pinov
------------------------

Praktický obrázok a popis, ktorý pin je ktorý na RPi, možno nájsť na stránke:

https://pinout.xyz/

GPIO piny sa zvyčajne identifikujú ich číslom v procesore (BCM ...)
a nie fyzickým poradím na RPi.

Chceme nejaké dva GPIO pripojiť na DIRECTION a STEP disketovej mechaniky
(zbytok tohoto návodu predpokladá BCM 23 a 24) a niektorý 5v a Ground pripojiť
na napájanie a zem.


Ovládanie GPIO
--------------

Nastavíme, že chceme používať GPIO 24 (BCM číslovanie) a chceme ho mať ako výstup:

```sh
echo "24" > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio24/direction
```

Teraz možeme nastavovať výstup na 0 alebo 1:
```sh
echo "0" > /sys/class/gpio/gpio24/value
...
echo "1" > /sys/class/gpio/gpio24/value
```

Pin 24 by sme mali mať pripojený na STEP na disketovej mechanike, a keď ho zmeníme z 0 na 1, tak by
sa hlava disketovej mechaniky mala posunúť o jeden krok.

Môžeme to skúsiť aj o viac:

```sh
for((i=0; i<80; ++i)) ; do echo "0" > /sys/class/gpio/gpio24/value ; sleep 0.1 ; echo "1" > /sys/class/gpio/gpio24/value; sleep 0.1 ; done
```

Hlava ale čoskoro "narazí" na kraj.
Na zmenu smeru potrebujeme ovládať aj druhý pin pripojený na DIRECTION:

```sh
echo "23" > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio23/direction

# There
echo "0" > /sys/class/gpio/gpio23/value
for((i=0; i<80; ++i)) ; do echo "0" > /sys/class/gpio/gpio24/value ; sleep 0.01 ; echo "1" > /sys/class/gpio/gpio24/value; sleep 0.01 ; done
# and back again
echo "1" > /sys/class/gpio/gpio23/value
for((i=0; i<80; ++i)) ; do echo "0" > /sys/class/gpio/gpio24/value ; sleep 0.01 ; echo "1" > /sys/class/gpio/gpio24/value; sleep 0.01 ; done
```
