WiFi
====

```sh
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

```
country=sk
ctrl_interface=/var/run/wpa_supplicant
network={
    ssid="pi"
    psk="malinocka"
}
```
Potom:
```sh
wpa_cli -i wlan0 reconfigure
```
Prípadne ak nezafunguje:
```sh
sudo systemctl restart wpa_supplicant
```
