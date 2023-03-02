"""
Write a python program which reminds you of drinking water every hour or two.
Your program can either beep or send desktop notifications for a specific operating system
"""

from plyer import notification

import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title="Drink Water",
        message="Drinking water will always keep you Hydrated",

        # displaying time
        timeout=2
    )
    # waiting time
    time.sleep(4)