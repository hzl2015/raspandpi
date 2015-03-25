class MockLight:
	"""Mock light module.

	Outputs color in RGB to stdout.
	"""
	def __init__(self):
		"""



		"""
		self.led_count = 1
		self.colors = [(0, 0, 0)] * self.led_count

	def set_led(self, led_nr, color):
		"""Set the color of a specific led.

		@param led_nr 	Which LED to set. First led is 0. 
		@param color	RGB tuple. 0.0 <= component <= 1.0.
		"""
		if (led_nr <= self.led_count):
			self.color = color

	def set_all(self, color):
		"""Set the color of all leds.

		@param led_nr 	Which LED to set. First led is 0. 
		@param color	RGB tuple. 0.0 <= component <= 1.0.
		"""
		for i in range(0, len(self.colors)):
			self.colors[i] = color

	def refresh(self):
		print("* Light rgb: %.2f, %.2f, %.2f" % (self.colors[0][0], self.colors[0][1], self.colors[0][2]))

	def getLedCount(self):
		return self.led_count
