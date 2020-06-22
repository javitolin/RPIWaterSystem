from Consts import LocalConfigurationFile, RemoteConfigurationFile
from IOHelper import *
from Configuration import *
import urllib.request
import json

def GetConfiguration():
    try:
        if IOHelper.IsInRaspberry():
            f = urllib.request.urlopen(RemoteConfigurationFile)
            mybytes = f.read()
            configurationFileContent = mybytes.decode("utf8")
        else:
            configurationFileContent = ReadFromFile(LocalConfigurationFile)
        configuration = Configuration.from_json(json.loads(configurationFileContent))
        return configuration
    except:
        raise
        return None
