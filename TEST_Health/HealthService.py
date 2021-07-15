import psutil
import time

class SystemHealth:
    pass


counter = 1

while counter < 10:
    print(psutil.cpu_percent())
    time.sleep(1)
    counter += 1
"""
0.0
13.3
9.8
10.7
5.5
6.4
4.4
5.7
8.6
"""

counter = 1

while counter < 100:
    print(psutil.virtual_memory().percent)
    time.sleep(1)
    counter += 1
