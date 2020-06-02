import datetime
import os.path
from Consts import DateTimeFormat

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
        return datetime.datetime.strptime(dateFromFile, DateTimeFormat)
    except:
        return datetime.datetime.min()

