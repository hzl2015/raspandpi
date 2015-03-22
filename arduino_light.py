import serial
import time

class ArduinoLight:
	"""Communicates with the experimental Arduino light module.

	Set the color of the lamp/LED/LEDs that are connected to the Arduino.
	"""
	def __init__(self, hw_interface):
		"""


		@param hw_interface		A serial port object controlling the serial port which the Arduino is connected to.
		"""
		self.led_count = 144
		self.ser = hw_interface
		# Making sure DTR is not resetting the arduino.
		self.ser.setDTR(False)
		# Sleep to allow the arduino to boot.
		time.sleep(3)

	def set_led(self, led_nr, color):
		"""Set the color of a specific led.

		@param led_nr 	Which LED to set. First led is 0. 
		@param color	RGB tuple. 0.0 <= component <= 1.0.
		"""
		r = int(color[0]*255)
		g = int(color[1]*255)
		b = int(color[2]*255)
		led_string = "%d,%d,%d,%d\n" % (led_nr + 1, r, g, b)
		print("Writing: " + led_string)
		self.ser.write(led_string)

	def set_all(self, color):
		"""Set the color of all leds.

		@param led_nr 	Which LED to set. First led is 0. 
		@param color	RGB tuple. 0.0 <= component <= 1.0.
		"""
		r = int(color[0]*255)
		g = int(color[1]*255)
		b = int(color[2]*255)
		led_string = "%d,%d,%d,%d\n" % (-1, r, g, b)
		print("Writing: " + led_string)
		self.ser.write(led_string)

	def refresh(self):
		led_string = "0, 0, 0, 0\n"
		print("Writing: " + led_string)
		self.ser.write(led_string)

	def getLedCount(self):
		return self.led_count
