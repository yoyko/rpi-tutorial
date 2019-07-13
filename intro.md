Zoznámenie sa s RPi
===================

https://www.raspberrypi.org/downloads/raspbian/  -> Raspbian Buster Lite

Anglický návod: https://www.raspberrypi.org/documentation/installation/installing-images/linux.md

TODO zistiť device (lsblk, fdiks -l)

```sh
wget http://..../
unzip 2019-07-10-raspbian-buster-lite.zip
sudo dd if=2019-07-10-raspbian-buster-lite.img of=/dev/XYZ bs=1M
```

Mala by sa automaticky pripojiť boot partícia. Ak nie, tak by malo stačiť vybrať a znovu vložiť kartu.

Zistíme, kde je pripojená boot partícia z SD karty
```sh
mount | grep boot
```

```sh
touch /run/media/boot/ssh
```

### Sieťové pripojenie cez USB

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
