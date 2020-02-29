import os
from pathlib import Path

def getDBfiles():
    dbFiles = []
    curPath = os.getcwd()
    dataPath = Path("resources")
    for root, directories, files in os.walk(dataPath):
        for fileName in files:
            if fileName.endswith('.crypt12'):
                dbFiles.append(fileName)

    return dbFiles