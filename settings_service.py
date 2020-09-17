import csv
import os

class Settings:
  def __init__(self, path):
    self.path = path
    self.read()

  def read(self):
    csvFile = open(self.path)
    self.list = list(csv.reader(csvFile))
    csvFile.close()

  def write(self):
    tempPath = "tempSettings.csv"
    tempCsvFile = open(tempPath, "w")
    csv.writer(tempCsvFile).writerows(self.list)
    tempCsvFile.close()
    os.rename(tempPath, self.path)
    self.read()

applicationSettings = Settings("applicationSettings.csv")
defaultSettings = Settings("defaultSettings.csv")
