import datetime
import os.path

def ReadFromFile(filename):
    with open(filename, 'r') as f:
        return f.read()