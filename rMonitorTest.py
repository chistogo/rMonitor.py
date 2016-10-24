#!/usr/bin/env python3

import time
from RMonitor import *

def main():
    monitor = RMonitor(6)
    while(True):
        print("Free Ram:", RMonitor.free())
        print("Totoal Ram:", RMonitor.totalRam())
        print("Memory Usage:", RMonitor.getMemoryUsage())
        #print("CPU Usage:", RMonitor.getCurrentCPUUsage())
        print("Adverage CPU Usage:", monitor.getAdvCPU())
        print("Disk Total:", RMonitor.totalSpace())
        print("Disk Usage:", RMonitor.usedSpace())
        print("Disk Percentage:", RMonitor.spaceUsage())
        time.sleep(5)

if __name__ == "__main__":
    main()
