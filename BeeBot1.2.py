#!/usr/bin/env python
import Adafruit_DHT as DHT
import RPi.GPIO as GPIO
import PCF8591 as ADC

import logging
logging.basicConfig(filename='HiveBot1.0.log',level=logging.INFO)

Sensor = 11
humiture1 = 17
humiture2 = 27
#humiture3 = 22
#humiture4 = 15
#humiture5 = 4
#humiture6 = 3

def setup():
	print 'Setting up, please wait...'
	ADC.setup(0x48)

def loop():
	while True:
		humidity1, temperature1 = DHT.read_retry(Sensor, humiture1)
		humidity2, temperature2 = DHT.read_retry(Sensor, humiture2)
		sound_level = ADC.read(0)
		
		if humidity1 is not None and temperature1 is not None:
			import time
			ts = time.time()

			import datetime
			st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
			
			print st + ' : T1={0:0.1f}*C  H1={1:0.1f}%'.format(temperature1, humidity1) + ' : T2={0:0.1f}*C  H2={1:0.1f}%'.format(temperature2, humidity2) + ' : S1=' + format(sound_level)
			logging.info(st + ' : T1={0:0.1f}*C  H1={1:0.1f}%'.format(temperature1, humidity1) + ' : T2={0:0.1f}*C  H2={1:0.1f}%'.format(temperature2, humidity2) + ' : S1=' + format(sound_level))
			
			time.sleep(3600) # delays in seconds (1 hours)
			
		else:
			print 'Failed to get reading. Try again!'

def destroy():
	GPIO.cleanup()
	ADC.write(0)

if __name__ == "__main__":
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
