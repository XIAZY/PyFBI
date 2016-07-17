# pyFBI
A Python FBI client to install .cia files to 3DS via network

__Only support FBI 2.0 and above.__
## Usage
```
usage: python3 pyfbi.py [-h] [-p PORT] ip [file [file ...]]

A Python FBI client to install .cia files to 3DS via network

positional arguments:
  ip                    Destination 3DS IP address with FBI listening
  file                  CIA file to be sent

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Custom FBI listening port, default to be 5000
```

Example:

![](https://i.imgur.com/n6ONM8y.png)