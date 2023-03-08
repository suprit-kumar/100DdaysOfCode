"""
Write a python program which reminds you of drinking water every hour or two.
Your program can either beep or send desktop notifications for a specific operating system
"""

import os
import time

REPEAT_INTERVAL = 60  # Repeat frequency in seconds

while True:
    command = "osascript -e \'say \"Hey Harry drink water\"\'; osascript -e \'display alert \"Hey Harry, Drink water\"\'"
    os.system(command)
    time.sleep(REPEAT_INTERVAL)
