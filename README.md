# pyFBI
A Python FBI client to install .cia files to 3DS via network

__Only support FBI 2.0 and above.__
## Usage
```
usage: pyfbi.py [-h] [-p PORT] ip [file [file ...]]

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

Or if you prefer GUI instead of CLI, you can use `pyfbi-gui.py`. Note that you need to have install `PyQt` in order to use it.
![](https://i.imgur.com/udidSEh.png)

Binary files are released [here](https://github.com/XIAZY/pyFBI/releases)

## License
Copyright 2016 XIAZY

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.