## General

1. Open Terminal

2. Login via SSH

```shell
ssh pi@raspberrypi.local
```

3. Update Dependencies and install the Updates

```shell
sudo apt-get update

sudo apt-get upgrade
```

## Install SQLite Database locally

This is used to store the data independent from network connection

1. Install lightweight SQLite Database

```shell
sudo apt-get install sqlite3
```

## Install Pip for Python 3

1. Install pip3 (brew for python) bc it was not installed

```shell
sudo apt-get install python3-pip
```

## Install Adafruit_DHT Module

1. Install the module to read from adafruit sensors

```shell
sudo pip3 install Adafruit_DHT
```

## Execution

1. Copy & Paste the Code from the repository files.

2. Run the Code

```shell
python temperature_humidity_sensor.py
```
