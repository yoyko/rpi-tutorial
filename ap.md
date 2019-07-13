WiFi Access Point
=================

Staticka IP a DHCP/DNS server na wlan0
--------------------------------------

Nainštalujeme `hostapd` (wifi AP démon) a `dnsmaq` (DHCP A DNS server):

```sh
sudo apt install hostapd dnsmasq
```

Vypneme `wpa_supplicant`

```sh
sudo systemctl disable wpa_supplicant
sudo systemctl stop wpa_supplicant
```

Nastavíme dhcp klienta aby `wlan0` mala statickú ip:
```sh
sudo nano /etc/dhcpcd.conf
```
a na koniec pridáme
```
interface wlan0
    static ip_address=192.168.4.1/24
    nohook wpa_supplicant
```
potom
```sh
sudo systemctl restart dhcpcd
```

Odzálohujeme dnsmasq konfiguráciu (alebo aj nie)
```sh
sudo mv  /etc/dnsmasq.conf /etc/dnsmasq.conf_
```

```sh
sudo nano /etc/dnsmasq.conf
```

```sh
interface=wlan0
# adresy pre DHCP klientov
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
# na vsetky DNS requesty odpovedame nasou adresou
address=/#/192.168.4.1
no-resolv
```

```sh
sudo systemctl reload dnsmasq
```

hostapd (wifi AP)
-----------------

```sh
sudo nano /etc/hostapd/hostapd.conf
```

```
interface=wlan0
driver=nl80211
ssid=MojaWiFi
hw_mode=g
channel=7
wpa=2
wpa_passphrase=SuperTajneHeslo
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
```

```sh
sudo systemctl unmask hostapd
sudo systemctl start hostapd
```


