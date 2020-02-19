"""
In this Problem,Actually if you look at the data closey,the max value is 8.00 and for each
value which is above 4,the value is always eight and if the value is below 4,the battery life is always twice
the charging time.
"""

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == "__main__":
    timeCharged = float(input())

    if timeCharged > 4:
        print("8.00")
    else:
        charged_battery = round(float(2 * timeCharged), 2)
        print(charged_battery)
