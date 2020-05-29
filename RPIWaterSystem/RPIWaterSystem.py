import urllib.request
import json
import datetime
import os.path
from time import sleep

lastTimeOpenFile = "lastTimeOpen"
link = "https://raw.githubusercontent.com/javitolin/RPIWaterSystem/master/RPIWaterSystem/Configuration.info"
localConfigurationPath = "C:\\Projects\\RPIWaterSystem\\RPIWaterSystem\\Configuration.info"
dateTimeFormat = '%Y-%m-%d %H:%M:%S.%f'

sleepBetweenIterations = 2
lastTimeOpen = datetime.datetime.min
seconds_in_day = 24 * 60 * 60

def ReadFromFile(filename):
    with open(filename, 'r') as f:
        return f.read()

def WriteToFile(filename, content):
    with open(filename, 'w') as f:
        return f.write(content)

def GetLastTimeFromFile():
    if not os.path.isfile(lastTimeOpenFile):
        return datetime.datetime.min()
    dateFromFile = ReadFromFile(lastTimeOpenFile)
    try:
        return datetime.datetime.strptime(dateFromFile, dateTimeFormat)
    except:
        return datetime.datetime.min()

def GetConfiguration():
    #f = urllib.request.urlopen(link)
    #mybytes = f.read()
    #configurationFileContent = mybytes.decode("utf8")
    defaultReturn = (None, None, None)
    configurationFileContent = ReadFromFile(localConfigurationPath)
    try:
        fromJson = json.loads(configurationFileContent)
    except:
        return defaultReturn

    isActive = fromJson["IsActive"]
    if (isActive not in ["true", "True"]):
        # log
        isActive = None
    
    minutesBetweenRuns = None
    try:
        minutesBetweenRuns = int(fromJson["MinutesBetweenRuns"])
    except:
        return defaultReturn

    secondsToOpen = None
    try:
        secondsToOpen = int(fromJson["SecondsToOpen"])
    except:
        return defaultReturn

    return (isActive, minutesBetweenRuns, secondsToOpen)

if __name__ == '__main__':
    while(True):
        sleep(sleepBetweenIterations)
        (isActive, minutesBetweenRuns, secondsToOpen) = GetConfiguration()
        if isActive == None or minutesBetweenRuns == None or secondsToOpen == None:
            # log
            continue

        now = datetime.datetime.now()
        difference = now - lastTimeOpen
        minutesFromLastTime = divmod(difference.days * seconds_in_day + difference.seconds, 60)[0]
        if minutesFromLastTime <= minutesBetweenRuns:
            # log
            continue

        # Need to run!
        # OPEN THE VALVE
        sleep(secondsToOpen)
        # CLOSE THE VALVE
        lastTimeOpen = datetime.datetime.now()
        WriteToFile(lastTimeOpenFile, now.strftime(dateTimeFormat))