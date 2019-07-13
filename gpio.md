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
hlava sa medzi nimi posúva pomocou krokového motorčeka.


Ovládanie GPIO
--------------


```sh
echo "24" > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio24/direction
echo "0" > /sys/class/gpio/gpio24/value
...
echo "1" > /sys/class/gpio/gpio24/value
```

```sh
for((i=0; i<80; ++i)) ; do echo "0" > /sys/class/gpio/gpio24/value ; sleep 0.1 ; echo "1" > /sys/class/gpio/gpio24/value; sleep 0.1 ; done
```

Smer

```sh
echo "23" > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio23/direction

echo "0" > /sys/class/gpio/gpio23/value
for((i=0; i<80; ++i)) ; do echo "0" > /sys/class/gpio/gpio24/value ; sleep 0.01 ; echo "1" > /sys/class/gpio/gpio24/value; sleep 0.01 ; done
echo "1" > /sys/class/gpio/gpio23/value
for((i=0; i<80; ++i)) ; do echo "0" > /sys/class/gpio/gpio24/value ; sleep 0.01 ; echo "1" > /sys/class/gpio/gpio24/value; sleep 0.01 ; done
```
