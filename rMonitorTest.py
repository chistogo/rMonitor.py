#!/usr/bin/env python3

import time
from RMonitor import *

uuid = "uuidstring"


def main():
    monitor = RMonitor(6, "http://example.com/handlers/usage.php", uuid)
    while(True):
       pass

if __name__ == "__main__":
    main()
