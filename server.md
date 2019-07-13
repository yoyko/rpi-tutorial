HTTP Server
===========

cherrypy
--------

```sh
sudo apt install python-cherrypy3
```

[Jednoduchý server](python/cherry.py)

floppyServer
------------

[floppyServer](python/floppyServer.py)

Systémová služba
----------------

`floppyServer.service`:

```
[Unit]
Description=My web server
After=network.target
Requires=floppyServer.socket

[Service]
ExecStart=/usr/bin/python -u floppyServer.py
WorkingDirectory=/home/pi/floppy
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```

`floppyServer.socket`:
```
[Unit]
Description=floppyServer socket

[Socket]
ListenStream=80
```

```
sudo cp floppyServer.service /etc/systemd/system/
sudo cp floppyServer.socket /etc/systemd/system/
sudo systemctl start floppyServer.service
```

```
sudo systemctl enable floppyServer.service
```
