Bluetooth pripojenie (na serial zariadenie)
===========================================


Nastavenie bluetooth služby
---------------------------

`sdptool`/`rfcomm` nefunguje v bluez 5, pokiaľ nie je zapnutý compatibility mód:

```
sudo nano /etc/systemd/system/dbus-org.bluez.service
```

Pridáme `-C` k `ExecStart=/usr/lib/bluetooth/bluetoothd` a ešte celý nový riadok
s `ExecStartPost=/usr/bin/sdptool add SP`:

```
...
ExecStart=/usr/lib/bluetooth/bluetoothd -C
ExecStartPost=/usr/bin/sdptool add SP
...
```

Samozrejme musíme teraz reštartnúť bluetooth službu.

```
sudo systemctl daemon-reload
sudo systemctl restart dbus-org.bluez.service
```

Nájdenie zariadenia, párovanie
------------------------------

Pustíme `bluetoothctl`:

```sh
sudo bluetoothctl
```

nasledovné príkazy zadávame v ňom.

Zapneme bluetooth, agenta na zadávanie pinu:

```
power on
agent on
default-agent
```

Vyhľadáme zariadenia:

```
scan on
```

Postupne sa objavia správy o nájdených zariadeniach.
Príkaz `devices` zobrazí všetky doteraz nájdené zariadenia.

### Párovanie

Párovanie sa začne príkazom `pair <adresa>`, ak zariadenie potrebuje pin, tak ho bude treba zadať:

```
[bluetooth]# pair 00:11:22:33:44:55
Attempting to pair with 00:11:22:33:44:55
[CHG] Device 00:11:22:33:44:55 Connected: yes
Request PIN code
[agent] Enter PIN code: 1234
[CHG] Device 00:11:22:33:44:55 UUIDs: 00001101-0000-1000-8000-00805f9b34fb
[CHG] Device 00:11:22:33:44:55 ServicesResolved: yes
[CHG] Device 00:11:22:33:44:55 Paired: yes
Pairing successful
```

Nastavíme tiež zariadenie ako trusted.

```
[bluetooth]# trust trust 00:11:22:33:44:55
```

Sériové pripojenie
------------------

Sériový port cez bluetooth si pripojíme príkazom `sudo rfcomm connect hci0 <adresa>`:

```
pi@raspberrypi $ sudo rfcomm connect hci0 00:11:22:33:44:55
Connected to /dev/rfcomm0 to 00:11:22:33:44:55 on channel 1
Press CTRL-C for hangup
```

`Ctrl-C` potom ukončí spojenie.

V novom termináli sa môžeme pripojiť no novovytvorený seriový port
napríklad pomocou `picocom`-u

```
apt install picocom
picocom /dev/rfcomm0
```

Python
------

TODO
