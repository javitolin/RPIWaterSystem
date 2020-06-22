from Consts import LocalConfigurationFile, RemoteConfigurationFile
import IOHelper
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
            configurationFileContent = IOHelper.ReadFromFile(LocalConfigurationFile)
        configuration = Configuration.from_json(json.loads(configurationFileContent))
        return configuration
    except:
        raise
        return None
