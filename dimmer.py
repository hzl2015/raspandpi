#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import ConfigParser
import time
import datetime
from arduino_light import ArduinoLight
from mock_light import MockLight
from light import Light
import serial

class Settings:
    def __init__(self, pathname=""):
        if not pathname:
            self.pathname = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini")
        self.read()
            
    def read(self):
        config = ConfigParser.ConfigParser()
        config.read(self.pathname)
        self.weekdays = self._parse_weekdays(config.get("Schedule", "Weekdays"))
        self.start_time = self._parse_time(config.get("Start", "Time"))
        self.start_intensity = config.getfloat("Start", "Intensity")
        self.wakeup_time = self._parse_time(config.get("Wakeup", "Time"))
        self.wakeup_intensity = config.getfloat("Wakeup", "Intensity")
        self.stop_time = self._parse_time(config.get("Stop", "Time"))
        self.stop_intensity = config.getfloat("Stop", "Intensity")

    def _parse_time(self, time_):
        struct = time.strptime(time_, "%Y-%m-%d %H:%M")
        dt = datetime.datetime.fromtimestamp(time.mktime(struct))
        return dt

    def _parse_weekdays(self, weekdays_):
        converted_weekdays = []
        for weekday in weekdays_.split(","):
            converted_weekday = time.strptime(weekday.strip(), "%a").tm_wday
            converted_weekdays.append(converted_weekday)
        return converted_weekdays

def setup_light_hardware(serial_port):
    hw = ArduinoLight(serial_port)
    light = Light(hw)
    return light

def set_lighting(light, settings):
    now = datetime.datetime.now().replace(year=1970, month=1, day=1)
    if datetime.datetime.now().weekday() in settings.weekdays:
        if settings.start_time <= now < settings.wakeup_time:
            print("{}    Increasing intensity...".format(now))
            # We want a certain color
            # The intensity should increase linearly between start and wakeup
            # Set LEDs
            light.set_color((1.0, 1.0, 1.0))	
            light.set_intensity(settings.wakeup_intensity * intensity_scaling)
            light.refresh()# TODO: Blend color between start_color and wakeup_color-
            si = settings.start_intensity
            wi = settings.wakeup_intensity
            st = time.mktime(settings.start_time.timetuple())
            wt = time.mktime(settings.wakeup_time.timetuple())
            n = time.mktime(now.timetuple())
            intensity_scaling = (wi - si) / (wt - st) * (n - st) + si
            light.set_intensity(settings.wakeup_intensity * intensity_scaling)
            light.refresh()
        elif settings.wakeup_time <= now < settings.stop_time:
            print("{}    Maximum brightness. Wake up!".format(now))
            # Set LEDs to
            light.set_color((1.0, 1.0, 1.0))
            light.set_intensity(settings.wakeup_intensity)
            light.refresh()
        else:
            print("{}    Off.".format(now))
            # Set LEDs to off
            light.set_color((1.0, 1.0, 1.0))
            light.set_intensity(settings.stop_intensity)
            light.refresh()
    else:
        print("{}    Nothing scheduled for today.".format(now))

if __name__ == "__main__":
    settings = Settings()
    if "--mock_light" in sys.argv:
    	light = Light(MockLight())
    else:
    	serial_port = "/dev/ttyACM0"
    	serial_speed = 9600
    	light = setup_light_hardware(serial.Serial(serial_port, serial_speed))
    set_lighting(light, settings)
    
