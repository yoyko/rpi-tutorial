Zoznámenie sa s RPi
===================

Anglický návod: https://www.raspberrypi.org/documentation/installation/installing-images/linux.md

Operačný systém pre RPi (Raspian, založený na Debian linuxe) chceme potrebujeme najskôr stiahnúť a nahrať
na SD kartu, ktorú potom vložíme do RPi.

Najnovší Raspbian možno stiahnuť na stránke https://www.raspberrypi.org/downloads/raspbian/ odkiaľ
cheme *Raspbian Buster Lite*, čo je relatívne malý systém bez grafického prostredia atď.

**"Relatívne malý" je stále dosť veľký na zahltenie wifi `;-)`, takže si ho stiahnite radšej napríklad z nasledovnej
url:**

http://mbpro.local/rpi/2019-07-10-raspbian-buster-lite.zip

Z príkazového riadku napríklad:

```sh
wget http://bionic.local/rpi/2019-07-10-raspbian-buster-lite.zip
```

Je to zip archív, ktorý musíme najskôr rozbaliť:

```sh
unzip 2019-07-10-raspbian-buster-lite.zip
```

Teraz už máme aj samotný `.img` súbor s "obrazom" operačného systému, ktorý chceme nahrať na SD kartu.
```
yoyo@bionic:~/rpi$ ls -l
total 2562580
-rw-r--r-- 1 yoyo yoyo 2197815296 júl 10 02:21 2019-07-10-raspbian-buster-lite.img
-rw-rw-r-- 1 yoyo yoyo  426250971 júl 14 22:05 2019-07-10-raspbian-buster-lite.zip

```

Zariadenie zodpovedajúce SD karte
---------------------------------

Linux rôzne pomenovavá rôzne zariadnie ako napríklad disky a čítačky SD kariet.
Aby sme vedeli nahrať stianutý obraz na správnu kartu (a nie na náš disk `;-)`),
potrebujeme zistiť pod akým menom našu kartu pozná linux.

Jeden spôsob je použiť príkaz `lsblk` ktorý vypíše všetky zariadenia zodpovedajúce diskom
v počítačí. Najjednoduchšie je pustiť ho raz predtým ako vložíme kartu do počítača a ešte raz
po tom čo ju vložíme: zariadenie ktoré pribudlo je to, ktoré reprezentuje našu kartu.

```
yoyo@bionic:~$ lsblk
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
loop0    7:0    0  34,6M  1 loop /snap/gtk-common-themes/818
...
sda      8:0    0    10G  0 disk
└─sda1   8:1    0    10G  0 part /
sr0     11:0    1  82,6M  0 rom
```

Vložíme SD kartu...

```
yoyo@bionic:~$ lsblk
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
loop0         7:0    0  34,6M  1 loop /snap/gtk-common-themes/818
...
sda           8:0    0    10G  0 disk
└─sda1        8:1    0    10G  0 part /
sr0          11:0    1  82,6M  0 rom
mmcblk0     179:0    0  14.9G  0 disk 
└─mmcblk0p1 179:1    0  14.9G  0 part 
```

Zaujíma nás celý `disk` a nie `part`ície na ňom (`mmcblko` vs `mmcblk0p1`).
Ak máme notebook so zabudovanou čítačkou kariet, tak to bude pravdepodovne `mmbcblk0`.

Keď už vieme, ktoré zariadenie je naša SD karta, môžeme na ňu nahrať Raspbian:

```sh
sudo dd if=2019-07-10-raspbian-buster-lite.img of=/dev/XYZ bs=1M
```

pričom `XYZ` nahradíme menom nášho zariadenia s SD kartou.

### Nastavenie SD karty

Naše RPi nebude mať pripojenú klávesnicu a monitor, ale budeme sa naň chcieť prípojiť
*na diaľku* (pomocou ssh). Na to potrebujeme dve veci:
- zabezpečiť aby na ňom bežal SSH server,
- zabezpečiť aby sa RPi buď pripojilo na WiFi, alebo aby malo sieťové spojenie
  s naším počítačom cez USB kábel.

Keď `dd` skončí, mala by sa automaticky pripojiť boot partícia. Ak nie, tak by
malo stačiť vybrať a znovu vložiť kartu.

Zistíme, kde je pripojená boot partícia z SD karty
```sh
mount | grep boot
```

#### SSH server

Stačí na karte  v boot partícii vyrobiť súbor s názvom `ssh` (je úplne jedno čo v ňom je / či je prázdný):

```sh
touch /run/media/boot/ssh
```

(`/run/media/boot` treba zameniť za cestu k boot partícii, ktorú sme zistili v predchádzajúcom kroku.)


#### Sieťové pripojenie cez USB

```sh
nano /run/media/boot/config.txt
```
a pridáme na koniec
```
dtoverlay=dwc2
```

Podobne
```sh
nano /run/media/boot/cmdline.txt
```
a za `rootwait` pridáme `modules-load=dwc2,g_ether`, teda malo by to vyzerať približne:
```
... fsck.repair=yes rootwait modules-load=dwc2,g_ether
```

### Zapnúť a pripojiť

```sh
ssh pi@raspberrypi.local
```
Heslo je `raspberry`

Aby sme nemuseli stále zadávať heslo, vyrobíme si ssh kľúč (ešte na vašom počítači):
```sh
ssh-keygen -t rsa -b 4096
ssh-add
ssh-copy-id  pi@raspberrypi.local
```

Teraz by už `ssh pi@raspberrypi.local` nemalo pýtať heslo `;-)`

**Ďalšie inštrukcie už predpokladajú, že sme pripojený na RPi a všetky popisované príkazy púštame na ňom.**
