#!/usr/bin/env python3

import time
from RMonitor import *

uuid = "sercretkey"


def main():
    monitor = RMonitor(6, "http://example.com/handlers/usage.php", uuid)
    while(True):
        print("waiting...")
        time.sleep(5)

if __name__ == "__main__":
    main()
