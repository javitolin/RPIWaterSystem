from Consts import LocalConfigurationFile, RemoteConfigurationFile
from IOHelper import ReadFromFile
import urllib.request
import json

def GetConfiguration():
    #f = urllib.request.urlopen(RemoteConfigurationFile)
    #mybytes = f.read()
    #configurationFileContent = mybytes.decode("utf8")
    defaultReturn = (None, None, None)
    configurationFileContent = ReadFromFile(LocalConfigurationFile)
    try:
        fromJson = json.loads(configurationFileContent)
    except:
        raise
        return defaultReturn

    isActive = fromJson["IsActive"]
    if (isActive not in ["true", "True"]):
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

