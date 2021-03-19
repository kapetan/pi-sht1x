********
MicroPython-sht1x
********
The MicroPython-sht1x package is a MicroPython library used to communicate and control the Sensirion SHT1x series of temperature and humidity sensors. Forked from [pi-sht1x](https://github.com/drohm/pi-sht1x).

SHT1x (including SHT10, SHT11 and SHT15) is Sensirion's family of surface mountable relative humidity and temperature sensors. The sensors integrate sensor elements plus signal processing on a tiny foot print and provide a fully calibrated digital output. A unique capacitive sensor element is used for measuring relative humidity while temperature is measured by a band-gap sensor.

The package was tested using the Raspberry Pi Pico.

This library provides the following functionality:

* Taking temperature measurements
* Taking humidity measurements
* Make dew point calculations
* Change the supplied voltage (5V, 4V, 3.5V, 3V, 2.5V)
* Enable or disable CRC checking
* Reading the Status Register
* Writing to the Status Register, provides the following functionality:
* Turn ``otp_no_reload`` on (will save about 10ms per measurement)
* Turn on the internal heater element (for functionality analysis, refer to the data sheet list above for more information)
* Change the resolution of measurements, High (14-bit temperature and 12-bit humidity) or Low (12-bit temperature and 8-bit humidity)

Usage
=====
When instantiating a SHT1x object, the following default values are used if not specified:

::

    vdd:              3.5V
    resolution:       HIGH (14-bit temperature & 12-bit humidity)
    heater:           False
    otp_no_reload:    False
    crc_check:        True

Import the library, create the sensor object and take measurements:

.. code-block:: python

    from sht1x import SHT1x
    from machine import Pin

    data_pin = Pin(10)
    sck_pin = Pin(11)
    sensor = SHT1x(data_pin, sck_pin)

    temp = sensor.read_temperature()
    humidity = sensor.read_humidity(temp)
    sensor.calculate_dew_point(temp, humidity)
    print(sensor)

This will create the SHT1x object using ``data_pin=10`` and ``sck_pin=11`` and default values for ``vdd`` (3.5V), ``resolution`` (HIGH), ``heater`` (False), ``otp_no_reload`` (False), and ``crc_check`` (True). The output will look something like this:

::

    Temperature: 24.05*C [75.25*F]
    Humidity: 22.80%
    Dew Point: 1.38*C

Credits
=======
This module was done for fun and to learn how to communicate with serial devices using Python and the Raspberry Pi. I referred to the following projects from time to time when I hit a stumbling block (there were many...):

* `Jonathan Oxer`_
* `Luca Nobili`_

.. _RPi.GPIO: http://pypi.python.org/pypi/RPi.GPIO
.. _issue: https://github.com/drohm/pi-sht1x/issues
.. _virtualenv: https://pypi.python.org/pypi/virtualenv
.. _Jonathan Oxer: https://github.com/practicalarduino/SHT1x
.. _Luca Nobili: https://bitbucket.org/lunobili/rpisht1x
