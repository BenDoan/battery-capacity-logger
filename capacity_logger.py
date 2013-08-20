#!/usr/bin/env python3
import os
import sys
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, SCRIPT_PATH + "/livia-client")

import livia
import subprocess

LOGGER = "http://localhost:5000"
DATATYPE = "batteryLogger"

def get_capacity():
    """ gets the battery capacity percentage using acpi """
    return subprocess.getstatusoutput("acpi -i")[1].split("\n")[1].split("=")[1][1:-1]

if __name__ == "__main__":
    capacity = get_capacity()
    l = livia.logger(LOGGER, DATATYPE)
    l.log(capacity)
