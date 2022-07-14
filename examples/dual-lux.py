#!/usr/bin/env python

# Import modules for time and to access sensor
from smbus import SMBus
from bme280 import BME280
from ltr559 import LTR559
import time
import datetime
from datetime import date

# Initialise the BME280
bus = SMBus(1)

# on board BME280 (0x76)
bme280i = BME280(i2c_dev=bus)

# external BME280 (0x77)
bme280e = BME280(i2c_dev=bus, i2c_addr=0x77)

# on board LTR559 (0x23)
ltr559 = LTR559(i2c_dev=bus)

# Get data and disgard to avoid garbage first reading

# on board
int_temperature = bme280i.get_temperature()
int_pressure =bme280i.get_pressure()
int_humidity = bme280i.get_humidity()

# external
ext_temperature = bme280e.get_temperature()
ext_pressure = bme280e.get_pressure()
ext_humidity = bme280e.get_humidity()

time.sleep(1)	

while True:

    # get date and time and read the sensorss
    today = date.today()
    now = datetime.datetime.now().time()

    # on board BME280
    int_temperature = round(bme280i.get_temperature(),1)
    int_pressure = round(bme280i.get_pressure(),1)
    int_humidity = round(bme280i.get_humidity(),1)

    lux = ltr559.get_lux()

    # external BME280
    ext_temperature = round(bme280e.get_temperature(),1)
    ext_pressure = round(bme280e.get_pressure(),1)
    ext_humidity = round(bme280e.get_humidity(),1)

    # output to screen
    print(today)
    print(now)
    print('Internal: {}*C {}hPa {}% {}lux'.format(int_temperature, int_pressure, int_humidity, lux))
    print('External: {}*C {}hPa {}%'.format(ext_temperature, ext_pressure, ext_humidity))

    # wait for 1 minute (60 seconds)
    time.sleep(60)
