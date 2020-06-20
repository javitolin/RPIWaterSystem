import datetime
import os.path
import platform

def ReadFromFile(filename):
    with open(filename, 'r') as f:
        return f.read()

def IsInRaspberry():
    platform_name = platform._syscmd_uname('-a')
    if platform_name == '':
        return False
    return True