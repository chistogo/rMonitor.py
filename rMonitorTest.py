#!/usr/bin/env python3

import time
from RMonitor import *

uuid = "80c50779d3a7436284f7e526bbbea5d4"


def main():
    monitor = RMonitor(6, "http://qiime.digibara.com/handlers/usage.php", uuid)
    while(True):
       pass

if __name__ == "__main__":
    main()
