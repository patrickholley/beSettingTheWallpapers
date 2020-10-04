import csv
import os
import sys


class Settings:
    def __init__(self, path):
        self.path = path
        self.read()

    def read(self):
        csvFile = open(self.path)
        self.list = list(csv.reader(csvFile))
        csvFile.close()

    def write(self):
        tempPath = f"{sys.argv[0]}/settings.temp.csv"
        tempCsvFile = open(tempPath, "w")
        csv.writer(tempCsvFile).writerows(self.list)
        tempCsvFile.close()
        os.rename(tempPath, self.path)
        self.read()


applicationSettings = Settings(f"{sys.argv[0]}/applicationSettings.csv")
defaultSettings = Settings(f"{sys.argv[0]}/defaultSettings.csv")
