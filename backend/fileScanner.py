import os
from pathlib import Path

curPath = os.getcwd()
dataPath = os.path.dirname(os.path.dirname(curPath)) # to go 2 directories up
dataPath = Path("Databases")
for root, directories, files in os.walk(dataPath):
    for fileName in files:
        if fileName.endswith('.crypt12'):
            print(fileName)
