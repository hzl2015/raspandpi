#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import ConfigParser
import datetime

class Settings:
    def __init__(self, pathname=""):
        if not pathname:
            self.pathname = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini")
            
    def read():
        config = ConfigParser.ConfigParser()
        config.read(self.pathname)
        self.start_time = config.get("Start", "Time")
        self.start_intensity = config.getfloat("Start", "Intensity")
        self.wakeup_time = config.get("Wakeup", "Time")
        self.wakeup_intensity = config.getfloat("Wakeup", "Intensity")
        self.stop_time = config.get("Stop", "Time")

if __name__ == "__main__":
    settings = Settings()
    
