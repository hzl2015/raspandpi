#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import ConfigParser
import time
import datetime

class Settings:
    def __init__(self, pathname=""):
        if not pathname:
            self.pathname = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini")
        self.read()
            
    def read(self):
        config = ConfigParser.ConfigParser()
        config.read(self.pathname)
        self.start_time = self._parse_time(config.get("Start", "Time"))
        self.start_intensity = config.getfloat("Start", "Intensity")
        self.wakeup_time = self._parse_time(config.get("Wakeup", "Time"))
        self.wakeup_intensity = config.getfloat("Wakeup", "Intensity")
        self.stop_time = self._parse_time(config.get("Stop", "Time"))
        self.stop_intensity = config.getfloat("Stop", "Intensity")

    def _parse_time(self, time_):
        struct = time.strptime(time_, "%H:%M")
        dt = datetime.datetime.fromtimestamp(time.mktime(struct))
        return dt
    
def set_lighting(settings):
    now = datetime.datetime.now().replace(year=1900, month=1, day=1)
    if settings.start_time <= now < settings.wakeup_time:
        print("{}    Increasing intensity...".format(now))
        # We want a certain color
        # The intensity should increase linearly between start and wakeup
        # Set LEDs
    elif settings.wakeup_time <= now < settings.stop_time:
        print("{}    Maximum brightness. Wake up!".format(now))
        # Set LEDs to
        settings.wakeup_intensity
    else:
        print("{}    Off.".format(now))
        # Set LEDs to off
        settings.stop_intensity
        
if __name__ == "__main__":
    settings = Settings()
    set_lighting(settings)
    
