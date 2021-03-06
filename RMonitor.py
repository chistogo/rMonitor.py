#Monitor.py is a script that attempts to abstracts some of the work to poll for
#system resources.

#TODO: Add Locks

import os
import re
import subprocess
import threading
import time
import requests

class RMonitor:

    def __init__(self,fivSecIntervalsBuffer = None, url = None,uuid = None):

        self.__howmany = 6
        self.__url = url
        self.__uuid = uuid
        try:
            if not(fivSecIntervalsBuffer is None):
                self.__howmany = fivSecIntervalsBuffer;
        except:
            self.__howmany = 6

        self.lock = threading.Lock()
        self.__adverageCPUData = []
        thread = threading.Thread(target=self.__threadUpdateHandler, args = ())
        thread.start()

    def getAdvCPU(self):
        sum = 0.0
        for i in self.__adverageCPUData:
            sum = sum + i
        
        returnMe = 0

        try:
            returnMe  = sum / float(len(self.__adverageCPUData))
        except:
            pass

        return returnMe

    def __threadUpdateHandler(self):
        lastTime = time.time()
        while True:
            if len(self.__adverageCPUData) != self.__howmany:
                self.__adverageCPUData.append(RMonitor.getCurrentCPUUsage())
            else:
                self.__adverageCPUData.pop(0)
                self.__adverageCPUData.append(RMonitor.getCurrentCPUUsage())
            #print(self.__adverageCPUData)
            if(not(self.__url is None)):
                r = requests.head(self.__url, params={'cpu': self.getAdvCPU(), 'free': free(), 'totalRam': totalRam(),'usedSpace':usedSpace(),"totalSpace":totalSpace(),"uuid":self.__uuid}, headers={'Connection':'close'},allow_redirects=False)
                print(r.url)
                r.close()
            time.sleep(1)


                
    def getCurrentCPUUsage():
        cmd = """top -b -n2 -p 1 | fgrep "Cpu(s)" | tail -1 | awk -F'id,' -v prefix="$prefix" '{ split($1, vs, ","); v=vs[length(vs)]; sub("%", "", v); printf "%s%.1f%%", prefix, 100 - v }' """
        result = subprocess.Popen([cmd],shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        return float((result.communicate()[0].decode('UTF-8').replace("%","")))
        
    def getMemoryUsage():
        output = subprocess.check_output(['free','-m'])
        output = output.decode('UTF-8')
        output = output.split("\n")[1]
        output = re.sub(' +',' ',output).split()
        return(float(output[2])/float(output[1]) * 100)

    def free():
        output = subprocess.check_output(['free','-m'])
        output = output.decode('UTF-8')
        output = output.split("\n")[1]
        output = re.sub(' +',' ',output).split()
        return(float(output[3]))
    def totalRam():
        output = subprocess.check_output(['free','-m'])
        output = output.decode('UTF-8')
        output = output.split("\n")[1]
        output = re.sub(' +',' ',output).split()
        return(float(output[1]))
        
    def totalSpace():
        cmd = """df -h --total | grep total"""
        result = subprocess.Popen([cmd],shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        return(result.communicate()[0].decode('UTF-8').split()[1])

    def usedSpace():
        cmd = """df -h --total | grep total"""
        result = subprocess.Popen([cmd],shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        return(result.communicate()[0].decode('UTF-8').split()[2])

    def spaceUsage():
        cmd = """df -h --total | grep total"""
        result = subprocess.Popen([cmd],shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        return(result.communicate()[0].decode('UTF-8').split()[4])




def getCurrentCPUUsage():
        cmd = """top -b -n2 -p 1 | fgrep "Cpu(s)" | tail -1 | awk -F'id,' -v prefix="$prefix" '{ split($1, vs, ","); v=vs[length(vs)]; sub("%", "", v); printf "%s%.1f%%", prefix, 100 - v }' """
        result = subprocess.Popen([cmd],shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        return float((result.communicate()[0].decode('UTF-8').replace("%","")))
        
def getMemoryUsage():
    output = subprocess.check_output(['free','-m'])
    output = output.decode('UTF-8')
    output = output.split("\n")[1]
    output = re.sub(' +',' ',output).split()
    return(float(output[2])/float(output[1]) * 100)

def free():
    output = subprocess.check_output(['free','-m'])
    output = output.decode('UTF-8')
    output = output.split("\n")[1]
    output = re.sub(' +',' ',output).split()
    return(float(output[3]))
def totalRam():
    output = subprocess.check_output(['free','-m'])
    output = output.decode('UTF-8')
    output = output.split("\n")[1]
    output = re.sub(' +',' ',output).split()
    return(float(output[1]))
    
def totalSpace():
    cmd = """df -h --total | grep total"""
    result = subprocess.Popen([cmd],shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    return(result.communicate()[0].decode('UTF-8').split()[1])

def usedSpace():
    cmd = """df -h --total | grep total"""
    result = subprocess.Popen([cmd],shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    return(result.communicate()[0].decode('UTF-8').split()[2])

def spaceUsage():
    cmd = """df -h --total | grep total"""
    result = subprocess.Popen([cmd],shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    return(result.communicate()[0].decode('UTF-8').split()[4])
