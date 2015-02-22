from ws2812arduino import Ws2812Arduino
import colorsys
import time

class Light:
	"""Light handling

	Adds color and intensity handling on top of the hardware provided in 'light_hardware'. 
	"""
	def __init__(self, light_hardware):
		self.color = (1, 1, 1)
		self.intensity = 0.0
		self.hw = light_hardware
		self.refresh()

	def __dim(self, rgb_color, intensity):
		""" Dim color.

		Calculate a new color based on a base color and an intensity.
		@param rgb_color	Base color
		@param intensity	Intensity which to 'scale' base_color with. 0.0=min intensity, 1.0=maximum intensity.
		"""
		hsv = colorsys.rgb_to_hsv(rgb_color[0], rgb_color[1], rgb_color[2])
		v = hsv[2]
		hsv = (hsv[0], hsv[1], v * intensity)
		return colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2])

	def refresh(self):
		""" Update the light with the set color and intensity
		"""
		# Mix intensity and color and then update the led strip.
		dimmed_color = self.__dim(self.color, self.intensity)
		print("Dimming to %d  (%f, %f, %f)" % (tuple([int(self.intensity*100)]) + dimmed_color))
		self.hw.set_all(dimmed_color)
		self.hw.refresh()
		time.sleep(1.0)

	def set_color(self, rgb_color):
		""" Set the light color.

		@param rgb_color	RGB color as a tuple (r, g, b), where 0.0 <= component <= 1.0.
		"""
		self.color = rgb_color

	def set_intensity(self, intensity):
		""" Set the light intensity.

		@param intensity	Value between 0.0 and 1.0 where 1.0 is the brightest.
		"""
		self.intensity = intensity
