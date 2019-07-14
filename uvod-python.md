Python
======

Python je interpretovaný programovací jazyk, takže si môžeme rovno pustiť
interpreter:

```
pi@raspberrypi:~ $ python
Python 2.7.16 (default, Apr  6 2019, 01:42:57)
[GCC 8.2.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

a zadávať príkazy:

```
>>> print('Ahoj')
Ahoj
>>> print(2+2)
4
```

Väčšie programy je samozrejme jednoduchšie písať do súboru:

```
nano mojprogram.py
```

```
print('Ahoj)'
```

Ukončíme nano (`^X Y Enter`) a pustíme program:

```
pi@raspberrypi:~ $ python mojprogram.py
Ahoj
```

Telá funkcií, cyklov a podmienok musia byť v pythone odsadené:

```python
def pozdravSkoroVsetkych():
    for kto in [ 'Jozko', 'Misko', 'Peto']:
        if kto != 'Jozko':
            print("Ahoj " + kto)

pozdravSkoroVsetkych()
```
